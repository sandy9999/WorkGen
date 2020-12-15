from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from collections import defaultdict
from openpyxl.writer.excel import save_virtual_workbook
from django.conf import settings

import logging
import datetime
import hashlib
import random
from docx import Document

from .utils.utils import (
    convert_question_bank,
    get_type_and_weightage,
    default_to_regular,
    convert_marker_data,
    get_allowed_questions,
    get_customized_paper,
    generate_dummy_tracker,
    generate_dummy_question_paper_format,
)
from .test_paper import (
    generate_test_or_generic_paper,
    generate_customized_paper,
)
from .models import (
    Mentor,
    Board,
    Grade,
    Questions,
    MCQOptions,
    Subject,
    GeneratedCustomizedPaper,
    GeneratedTestAndGenericPaper,
    SubjectSplit,
    Chapter
)

logger = logging.getLogger(__name__)


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def student_view(request):
    board_list = Board.objects.all().values_list('board', flat=True)
    board_list = list(board_list)
    return render(request, 'student_view.html', {'data': board_list})


def login_view(request):
    next_url = request.GET.get('next') if request.GET.get('next') else ''
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect('searchapp:mentor_view')
    else:
        if request.user.is_authenticated:
            return redirect('searchapp:mentor_view')
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'next': next_url})


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def mentor_view(request):
    return render(request, 'mentor_view.html')


@login_required
def chapter_and_split_view(request):
    board_list = Board.objects.all().values_list('board', flat=True)
    board_list = list(board_list)
    question_weightage_choices = Questions.QUESTION_WEIGHTAGE_CHOICES
    question_type_choices = Questions.QUESTION_TYPE_CHOICES
    return render(request, 'chapter_and_split_view.html', {'data': board_list, 'question_weightage_choices': question_weightage_choices, 'question_type_choices': question_type_choices})


def add_board(request):
    if request.method == 'POST':
        board = request.POST.dict()['board']
        try:
            board = Board.objects.get(board=board)
            return JsonResponse(dict(error='The board is already in the database'), status=401)
        except Board.DoesNotExist:
            Board.objects.create(board=board)
            return JsonResponse(dict(status='ok'))


def add_grade(request):
    if request.method == 'POST':
        data = request.POST.dict()
        board = Board.objects.get(board=data['board'])
        grade = int(data['grade'])
        try:
            grade = Grade.objects.get(grade=grade, board=board)
            return JsonResponse(dict(error=f'The grade is already included under the {board.board} board'), status=401)
        except Grade.DoesNotExist:
            Grade.objects.create(board=board, grade=grade)
            return JsonResponse(dict(status='ok'))


def get_grades(request):
    if request.method == 'GET':
        board = request.GET['board']
        grades = Grade.objects.filter(
            board__board=board).values_list('id', 'grade')
        json_data = {'grade_list': [
            {'grade_id': x[0], 'grade_name': x[1]} for x in grades]}
        return JsonResponse(json_data)


def get_subjects(request):
    if request.method == 'GET':
        grade = request.GET['grade']
        subjects = Subject.objects.filter(
            grade__id=grade).values_list('id', 'subject_name')
        json_data = {'subject_list': [
            {'subject_id': x[0], 'subject_name': x[1]} for x in subjects]}
        return JsonResponse(json_data)


@login_required
def add_questions_view(request):
    return render(request, 'question_upload_mentor.html')


@login_required
def download_customized_docx(request):
    token = request.GET['token']
    doc_obj = GeneratedCustomizedPaper.objects.get(
        mentor=request.user, token=token, is_ready=True)
    document = Document(settings.BASE_DIR + "/" + doc_obj.file_path)
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=workgen_document.docx'
    document.save(response)
    return response


def download_test_and_generic_docx(request):
    token = request.GET['token']
    doc_obj = GeneratedTestAndGenericPaper.objects.get(
        token=token, is_ready=True)
    document = Document(settings.BASE_DIR + "/" + doc_obj.file_path)
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=workgen_document.docx'
    document.save(response)
    return response


@login_required
def generated_documents_view(request):
    generated_data = GeneratedCustomizedPaper.objects.filter(
        mentor=request.user,
        is_ready=True).values_list(
        'token', 'submitted_date', 'file_path').order_by('-submitted_date').annotate(doc_count=Count('token'))
    generated_data = list(generated_data)
    unique_token = defaultdict(bool)
    data = []
    for item in generated_data:
        if not unique_token[item[0]]:
            unique_token[item[0]] = True
            data.append(item)
    return render(request, 'generated_documents.html', {'data': data})


@login_required
def add_questions(request):
    error = ""
    if request.method == 'GET':
        return redirect('/questions_upload')
    if request.method == 'POST':
        if request.FILES:
            file_obj = request.FILES['datafile']
            default_dict = convert_question_bank(file_obj)
            question_bank_dict = default_to_regular(default_dict)
            try:
                add_to_database(question_bank_dict, request.user)
                return render(request, 'mentor_view.html', {'pop': " the questions have been added successfully", 'flag': '0'})
            except Exception as e:
                logger.error(str(e))
                return render(request, 'question_upload_mentor.html', {'error': str(e), 'flag': '1'})
        else:
            return render(request, 'question_upload_mentor.html', {'error': "no file selected", 'flag': '1'})


def add_to_database(question_bank_dict, user):
    mentor = Mentor.objects.get(username=user.username)
    for board in question_bank_dict:
        try:
            board_object = Board.objects.get(board=board)
        except Board.DoesNotExist:
            raise Exception(
                "{} is not a valid board in the database. Please check for typos / entry in the database".format(
                    board))
            logger.error("No such board")
            return
        grade_to_question_dict = question_bank_dict[board]
        for grade in grade_to_question_dict:
            try:
                grade_object = Grade.objects.get(
                    grade=grade, board=board_object)
            except Grade.DoesNotExist:
                raise Exception(
                    "{} is not a valid grade in the database for {} board. Please check for typos / entry in the database".format(
                        grade,board))
                logger.error("No such grade")
                return
            subject_to_question_dict = grade_to_question_dict[grade]
            for subject_name in subject_to_question_dict:
                try:
                    subject_object = Subject.objects.get(
                        subject_name=subject_name, grade=grade_object)
                except Subject.DoesNotExist as e:
                    raise Exception(
                        "{} is not a valid subject in the database for {} grade {} board. Please check for typos / entry in the database".format(subject_name,grade,board))
                    logger.error("No such subject")
                    return
                chapter_to_question = subject_to_question_dict[subject_name]
                for chapter_tuple in chapter_to_question:
                    chapter_no = chapter_tuple[0]
                    chapter_name = chapter_tuple[1]
                    questions_dict = chapter_to_question[chapter_tuple]
                    try:
                        with transaction.atomic():
                            for question_type in questions_dict:
                                questions_list = questions_dict[question_type]
                                q_type, weightage = get_type_and_weightage(
                                    question_type)
                                for i in range(len(questions_list)):
                                    q = Questions(
                                        chapter=Chapter.objects.get(
                                            chapter_name=chapter_name),
                                        question_type=q_type,
                                        question_weightage=weightage,
                                        text=questions_list[i][0],
                                        uploaded_by=mentor,
                                        source=questions_list[i][1])
                                    q.save()
                    except Chapter.DoesNotExist as e:
                        raise Exception(
                            "{} is not a valid chapter in the database for {} subject {} grade {} board. Please check for typos / entry in the database".format(chapter_name,subject_name,grade,board))


def get_chapters(request):
    if request.method == 'GET':
        subject = request.GET['subject']
        board = request.GET['board']
        chapters = Chapter.objects.filter(
            subject__id=subject).values_list('id', 'chapter_name')
        subject_breakup = list(SubjectSplit.objects.filter(
            board__board=board).values_list(
                'name'
        ).distinct())
        json_data = {
            'chapters': [{'chapter_id': x[0], 'chapter_name': x[1]} for x in chapters],
            'subject_breakup': subject_breakup,
        }
        return JsonResponse(json_data)


def display_split_table(request):
    if request.method == 'GET':
        board = request.GET['board']
        split_names = request.GET.getlist('splits[]')
        subject_breakup = SubjectSplit.objects.filter(
            name__in=split_names,
            board__board=board).values_list(
                'id',
                'question_weightage',
                'question_type',
                'total_questions',
                'questions_to_attempt',
                'name'
        ).order_by('name')
        json_data = {
            'subject_breakup': [{'breakup_id': x[0], 'question_weightage_id': x[1],
                                 'question_weightage': Questions.QUESTION_WEIGHTAGE_CHOICES[x[1] - 1][1],
                                 'question_type_id': x[2],
                                 'question_type': Questions.QUESTION_TYPE_CHOICES[x[2] - 1][1], 'total_questions': x[3],
                                 'questions_to_attempt': x[4], 'name': x[5]} for x in subject_breakup]
        }
        return JsonResponse(json_data)


@login_required
def delete_subject_split(request):
    if request.method == 'GET':
        breakup_id = request.GET['id']
        SubjectSplit.objects.filter(id=breakup_id).delete()
        return JsonResponse({"message": "success"})


@login_required
def add_subject_split(request):
    if request.method == 'GET':
        split_name = request.GET['split_name']
        board = request.GET['board']
        question_type = request.GET['question_type']
        question_weightage = request.GET['question_weightage']
        total_questions = request.GET['total_questions']
        questions_to_attempt = request.GET['questions_to_attempt']
        try:
            # filter returns a query set which is converted to a list and then the first element is picked up.
            board_id = list(Board.objects.filter(
                board=board).values_list('id', flat=True))[0]
        except Board.DoesNotExist:
            raise Exception(
                "{} is not a valid board in the database. Please check for typos / entry in the database".format(
                    board_name))
        SubjectSplit.objects.create(name=split_name, board_id=board_id, question_weightage=question_weightage,
                                    question_type=question_type, total_questions=total_questions,
                                    questions_to_attempt=questions_to_attempt)
        return JsonResponse({"message": "success"})


@login_required
def add_chapter(request):
    if request.method == 'GET':
        subject = request.GET['subject']
        chapter_name = request.GET['chapter']
        try:
            # filter returns a query set which is converted to a list and then the first element is picked up.
            subject_name = list(Subject.objects.filter(
                id=subject).values_list('subject_name', flat=True))[0]
        except Subject.DoesNotExist:
            raise Exception(
                "{} is not a valid subject in the database. Please check for typos / entry in the database".format(
                    subject_name))
        Chapter.objects.create(chapter_name=chapter_name, subject_id=subject)
        return JsonResponse({"message": "success"})


@login_required
def delete_chapters(request):
    if request.method == 'GET':
        subject = request.GET['subject']
        chapters = request.GET.getlist('chapters[]')
        for chapter in chapters:
            Chapter.objects.filter(subject__id=subject, id=chapter).delete()
        return JsonResponse({"message": "success"})


def get_test_paper(request):
    if request.method == 'GET':
        subject = request.GET['subject']
        paper_breakup = request.GET['board'] # setting board as the deciding factor for subject breakup.
        chapters = request.GET.getlist('chapters[]')
        # filter returns a query set which is converted to a list and then the first element is picked up.
        subject_name = list(Subject.objects.filter(
            id=subject).values_list('subject_name', flat=True))[0]
        subject_breakup = SubjectSplit.objects.filter(
            name=paper_breakup.upper()).values_list(
                'question_weightage',
                'question_type',
                'total_questions',
                'questions_to_attempt')
        breakup = {}
        for qtype in subject_breakup:
            if qtype[0] == 1:
                if qtype[1] == 1:
                    breakup['1A'] = [qtype[2], qtype[3]]
                elif qtype[1] == 2:
                    breakup['1B'] = [qtype[2], qtype[3]]
            else:
                breakup[str(qtype[0])] = [qtype[2], qtype[3]]
        # token is basically used to identify paper
        token = hashlib.sha1(datetime.datetime.now(
        ).__str__().encode('utf-8')).hexdigest()
        generated_paper = GeneratedTestAndGenericPaper(
            token=token, submitted_date=datetime.datetime.now())
        generated_paper.save()
        generate_test_or_generic_paper(
            subject_name, chapters, breakup, token, 'random')
        return JsonResponse({"message": "success", "token": token})


def get_generic_paper(request):
    if request.method == "GET":
        breakup = {}
        subject = request.GET['subject']
        # filter returns a query set which is converted to a list and then the first element is picked up.
        subject_name = list(Subject.objects.filter(
            id=subject).values_list('subject_name', flat=True))[0]
        chapters = request.GET.getlist('chapters[]')
        sent_breakup = request.GET.getlist('breakup[]')
        random_settings = request.GET['random_setting']

        breakup = {
            '1A': [int(sent_breakup[0])] * 2,
            '1B': [int(sent_breakup[1])] * 2,
            '2': [int(sent_breakup[2])] * 2,
            '3': [int(sent_breakup[3])] * 2,
            '5': [int(sent_breakup[4])] * 2,
        }

        token = hashlib.sha1(datetime.datetime.now(
        ).__str__().encode('utf-8')).hexdigest()
        generated_paper = GeneratedTestAndGenericPaper(
            token=token, submitted_date=datetime.datetime.now())
        generated_paper.save()

        generate_test_or_generic_paper(
            subject_name, chapters, breakup, token, random_settings)

        return JsonResponse({"message": "success", "token": token})


def get_customize_paper(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "To access customised paper, you need to be logged in"}, status=401)
    if request.method == 'POST':
        subject = request.POST['subject']
        # filter returns a query set which is converted to a list and then the first element is picked up.
        subject_name = list(Subject.objects.filter(
            id=subject).values_list('subject_name', flat=True))[0]
        chapters = map(int, request.POST.getlist('chapters[]')[0].split(','))
        sent_breakup = request.POST.getlist('breakup[]')
        sent_breakup = sent_breakup[0].split(',')
        sent_breakup = [int(x) for x in sent_breakup]
        student_names = request.POST.getlist('student_names[]')
        student_names = student_names[0].split(',')
        if len(request.FILES) == 0:
            return JsonResponse({"message": "failed"})
        file_obj = request.FILES['file']
        if all(v == 0 for v in sent_breakup):
            breakup = {
                '1A': [1, 1],
                '1B': [1, 1],
                '2': [1, 1],
                '3': [1, 1],
                '5': [1, 1]
            }
        else:
            breakup = {
                '1A': [sent_breakup[0]] * 2,
                '1B': [sent_breakup[1]] * 2,
                '2': [sent_breakup[2]] * 2,
                '3': [sent_breakup[3]] * 2,
                '5': [sent_breakup[4]] * 2,
            }
        data = convert_marker_data(file_obj, breakup)
        stud_data = data[0]
        allowed_chapter_nos = data[1]
        allowed_chapter_nos = list(set(allowed_chapter_nos) - set(chapters))
        allowed_qtype = []
        for student_name in stud_data:
            for ques_type in stud_data[student_name]:
                allowed_qtype.append(ques_type)
        allowed_qtype = list(set(allowed_qtype))
        filtered_data = get_allowed_questions(
            stud_data, allowed_qtype, allowed_chapter_nos)
        customized_data = get_customized_paper(filtered_data)
        if len(allowed_chapter_nos) == 1:
            for item in customized_data:
                if len(customized_data[item]) == 0:
                    customized_data[item] = allowed_chapter_nos
        elif len(allowed_chapter_nos) == 2:
            for item in customized_data:
                dup_list = [x for x in allowed_chapter_nos if x not in customized_data[item]]
                if len(customized_data[item]) == 0:
                    customized_data[item] = customized_data[item] + (random.sample(dup_list, 2))
                elif len(customized_data[item]) == 1:
                    customized_data[item] = customized_data[item] + (random.sample(dup_list, 1))
        else:
            for item in customized_data:
                dup_list = [x for x in allowed_chapter_nos if x not in customized_data[item]]
                if len(customized_data[item]) == 0:
                    customized_data[item] = customized_data[item] + (random.sample(dup_list, 3))
                elif len(customized_data[item]) == 1:
                    customized_data[item] = customized_data[item] + (random.sample(dup_list, 2))
                elif len(customized_data[item]) == 2:
                    customized_data[item] = customized_data[item] + (random.sample(dup_list, 1))
        for item in student_names:
            if item in customized_data:
                del customized_data[item]
        token = hashlib.sha1(datetime.datetime.now().__str__().encode('utf-8')).hexdigest()
        generated_paper = GeneratedCustomizedPaper(token=token, mentor=request.user,
                                                   submitted_date=datetime.datetime.now())
        generated_paper.save()
        generate_customized_paper.delay(
            subject_name, allowed_chapter_nos, breakup, customized_data, request.user.username, token)
        return JsonResponse({"message": "success", "token": token})


def generate_optional_inputs(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        if len(request.FILES) == 0:
            return JsonResponse({"message": "failed"})
        file_obj = request.FILES['file']
        breakup = {
            '1A': [1, 1],
            '1B': [1, 1],
            '2': [1, 1],
            '3': [1, 1],
            '5': [1, 1]
        }
        data = convert_marker_data(file_obj, breakup)
        allowed_qtype = []
        allowed_chapter_nos = []
        student_name_list = []
        stud_data = data[0]
        allowed_chapter_nos = list(set(data[1]))
        for student_name in stud_data:
            student_name_list.append(student_name)
            for ques_type in stud_data[student_name]:
                allowed_qtype.append(ques_type)
        allowed_qtype = list(set(allowed_qtype))
        allowed_chapters = Chapter.objects.filter(id__in=allowed_chapter_nos).values_list('id', 'chapter_name')
        allowed_chapters = [{'chapter_id': x[0], 'chapter_name': x[1]} for x in allowed_chapters]
        return JsonResponse({"message": "success", "chapters": allowed_chapters, "stud_name": student_name_list,
                             "qtype": allowed_qtype})

@login_required
def get_dummy_tracker(request):
    if request.method == 'GET':
        split_name = request.GET['split_name']
        subject = request.GET['subject']
        # filter returns a query set which is converted to a list and then the first element is picked up.
        subject_name = list(Subject.objects.filter(
            id=subject).values_list('subject_name', flat=True))[0]
        subject_split_list = SubjectSplit.objects.filter(
            subject__id=subject, name__iexact=split_name)
        split_list = list(subject_split_list)
        import base64
        dummy_workbook = generate_dummy_question_paper_format()
        base64_response = base64.b64encode(
            save_virtual_workbook(dummy_workbook)).rstrip(b'\n=')
        return HttpResponse(base64_response, content_type='multipart/form-data')

@login_required
def get_dummy_question_paper_format(request):
    if request.method == 'GET':
        import base64
        dummy_workbook = generate_dummy_question_paper_format()
        base64_response = base64.b64encode(
            save_virtual_workbook(dummy_workbook)).rstrip(b'\n=')
        return HttpResponse(base64_response, content_type='multipart/form-data')
