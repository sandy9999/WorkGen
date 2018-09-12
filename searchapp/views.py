from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from collections import defaultdict
from django.conf import settings

import logging
import datetime
import hashlib
import random
from docx import Document

from .utils.utils import convert_question_bank,get_type_and_weightage,default_to_regular,convert_marker_data,get_allowed_questions,get_customized_paper
from .test_paper import generate_test_or_generic_paper, generate_customized_paper
from .models import Mentor, Questions, MCQOptions, Subject, GeneratedQuestionPaper,SubjectSplit

logger = logging.getLogger(__name__)

@login_required(login_url='/login')
def student_view(request):
    subject_list = Subject.objects.all().values_list('subject_name', flat=True)
    subject_list = list(subject_list)
    return render(request,'student_view.html',{'data':subject_list, 'is_logged_in': request.user.is_authenticated})


def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if(form.is_valid()):
            user=form.get_user()
            login(request,user)
            return redirect('searchapp:mentor_view')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})


def logout_view(request):
  logout(request)
  return redirect('/')


@login_required(login_url='/login')
def mentor_view(request):
    return render(request, 'mentor_view.html', {'is_logged_in': request.user.is_authenticated})


@login_required(login_url='/login')
def add_questions_view(request):
    return render(request, 'question_upload_mentor.html')


@login_required(login_url='/login')
def download_docx(request):
    token = request.GET['token']
    doc_obj = GeneratedQuestionPaper.objects.get(mentor=request.user, token=token, is_ready=True)
    document = Document(settings.BASE_DIR + "/" + doc_obj.file_path)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=workgen_document.docx'
    document.save(response)
    return response


@login_required(login_url='/login')
def generated_documents_view(request):
    generated_data = GeneratedQuestionPaper.objects.filter(
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


@login_required(login_url='/login')
def add_questions(request):
    error = ""
    if request.method == 'POST':
        if request.FILES:
            file_obj = request.FILES['datafile']
            default_dict = convert_question_bank(file_obj)
            subject_to_chapter_to_question=default_to_regular(default_dict)
            add_to_database(subject_to_chapter_to_question, request.user)
            return render(request,'mentor_view.html',{'pop':" the questions have been added successfully",'flag':'0'})
        else:
            return render(request,'question_upload_mentor.html',{'error':"no file selected",'flag':'1'})


def add_to_database(subject_to_chapter_to_question, user):
    mentor = Mentor.objects.get(username=user.username)
    for subject_name in subject_to_chapter_to_question:
        try:
            subject = Subject.objects.get(subject_name=subject_name)
        except Exception as e:
            print("No such subject")
            return
        chapter_to_question = subject_to_chapter_to_question[subject_name]
        for chapter_tuple in chapter_to_question:
            chapter_no = chapter_tuple[0]
            chapter_name = chapter_tuple[1]
            questions_dict = chapter_to_question[chapter_tuple]
            for question_type in questions_dict:
                        questions_list = questions_dict[question_type]
                        q_type, weightage = get_type_and_weightage(question_type)
                        for i in range(len(questions_list)):
                            q = Questions(chapter_number=chapter_no,
                                    subject=subject,
                                    chapter=chapter_name,
                                    question_type=q_type,
                                    question_weightage=weightage,
                                    text=questions_list[i][0],
                                    uploaded_by=mentor,
                                    source=questions_list[i][1])
                            q.save()
                        transaction.commit()


def get_chapters(request):
    if request.method == 'GET':
        subject_name = request.GET['subject']
        chapters = Questions.objects.filter(subject__subject_name__iexact=subject_name).values_list('chapter', flat=True).distinct()
        json_data = {
            'chapters': list(chapters)
        }
        return JsonResponse(json_data)


def get_test_paper(request):
    if request.method == 'GET':
        subject = request.GET['subject']
        chapters = request.GET.getlist('chapters[]')
        papertype = request.GET['papertype']
        subject_breakup = SubjectSplit.objects.filter(
            name=papertype,
            subject__subject_name__iexact=subject).values_list(
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
        token = hashlib.sha1(datetime.datetime.now().__str__().encode('utf-8')).hexdigest()
        generated_paper = GeneratedQuestionPaper(token=token, mentor=request.user, submitted_date=datetime.datetime.now())
        generated_paper.save()
        generate_test_or_generic_paper.delay(subject, chapters, breakup, request.user.username, token, 'random')
        return JsonResponse({"message":"success", "token": token})


def get_generic_paper(request):
    if request.method == "GET":
        breakup = {}
        subject = request.GET['subject']
        chapters = request.GET.getlist('chapters[]')
        sent_breakup = request.GET.getlist('breakup[]')
        random_settings = request.GET['random_setting']

        breakup = {
            '1A': [int(sent_breakup[0])]*2,
            '1B': [int(sent_breakup[1])]*2,
            '2': [int(sent_breakup[2])]*2,
            '3': [int(sent_breakup[3])]*2,
            '5': [int(sent_breakup[4])]*2,
        }

        token = hashlib.sha1(datetime.datetime.now().__str__().encode('utf-8')).hexdigest()
        generated_paper = GeneratedQuestionPaper(token=token, mentor=request.user, submitted_date=datetime.datetime.now())
        generated_paper.save()

        generate_test_or_generic_paper.delay(subject, chapters, breakup, request.user.username, token, random_settings)

        return JsonResponse({"message":"success", "token": token})

def get_test_format(request):
    if request.method == 'GET':
        subject = request.GET['subject']
        papers = SubjectSplit.objects.filter(subject__subject_name__iexact=subject).values_list('name', flat=True).distinct()
        return JsonResponse({"papers": list(papers)})

def get_customize_paper(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        chapters = request.POST.getlist('chapters[]')
        chapters = chapters[0].split(',')
        sent_breakup = request.POST.getlist('breakup[]')
        sent_breakup = sent_breakup[0].split(',')
        sent_breakup = [ int(x) for x in sent_breakup ]
        student_names = request.POST.getlist('student_names[]')
        student_names = student_names[0].split(',')
        if len(request.FILES)==0:
                return JsonResponse({"message":"failed"})
        file_obj = request.FILES['file']
        if all(v==0 for v in sent_breakup):
            breakup = {
                '1A': [1, 1],
                '1B': [1, 1],
                '2': [1, 1],
                '3': [1, 1],
                '5': [1, 1]
            }
        else:
            breakup = {
                '1A': [sent_breakup[0]]*2,
                '1B': [sent_breakup[1]]*2,
                '2': [sent_breakup[2]]*2,
                '3': [sent_breakup[3]]*2,
                '5': [sent_breakup[4]]*2,
            }
        data = convert_marker_data(file_obj, breakup)
        allowed_qtype = []
        allowed_chapters = []
        stud_data  = data[0]
        allowed_chapter_nos = list(set(data[1]))
        allowed_chapters = Questions.objects.filter(subject__subject_name__iexact=subject,chapter_number__in=allowed_chapter_nos).values_list('chapter', flat=True).distinct()
        allowed_chapters = list(allowed_chapters)
        for item in chapters:
            if item in allowed_chapters:
                allowed_chapters.remove(item)
        for student_name in stud_data :
            for ques_type in stud_data[student_name]:
                allowed_qtype.append(ques_type)
        allowed_qtype = list(set(allowed_qtype))
        allowed_chapter_nos = Questions.objects.filter(subject__subject_name__iexact=subject,chapter__in=allowed_chapters).values_list('chapter_number', flat=True).distinct()
        allowed_chapter_nos = list(allowed_chapter_nos)
        filtered_data = get_allowed_questions(stud_data,allowed_qtype,allowed_chapter_nos)
        customized_data = get_customized_paper(filtered_data)
        if len(allowed_chapter_nos)==1:
            for item in customized_data:
                if len(customized_data[item])==0:
                    customized_data[item] = allowed_chapter_nos
        elif len(allowed_chapter_nos)==2:
            for item in customized_data:
                dup_list = [ x for x in allowed_chapter_nos if x not in customized_data[item] ]
                if len(customized_data[item])==0:
                    customized_data[item] = customized_data[item] + (random.sample(dup_list,2))
                elif len(customized_data[item])==1:
                    customized_data[item] = customized_data[item] + (random.sample(dup_list,1))
        else:
            for item in customized_data:
                dup_list = [ x for x in allowed_chapter_nos if x not in customized_data[item] ]
                if len(customized_data[item])==0:
                    customized_data[item] = customized_data[item] + (random.sample(dup_list,3))
                elif len(customized_data[item])==1:
                    customized_data[item] = customized_data[item] + (random.sample(dup_list,2))
                elif len(customized_data[item])==2:
                    customized_data[item] = customized_data[item] + (random.sample(dup_list,1))
        for item in student_names:
            if item in customized_data:
                del customized_data[item]
        token = hashlib.sha1(datetime.datetime.now().__str__().encode('utf-8')).hexdigest()
        generated_paper = GeneratedQuestionPaper(token=token, mentor=request.user, submitted_date=datetime.datetime.now())
        generated_paper.save()
        generate_customized_paper.delay(subject, allowed_chapter_nos, breakup, customized_data, request.user.username, token)
        return JsonResponse({"message":"success", "token": token})

def generate_optional_inputs(request):
    if request.method=='POST':
        subject = request.POST['subject']
        if len(request.FILES)==0:
            return JsonResponse({"message":"failed"})
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
        stud_data  = data[0]
        allowed_chapter_nos = list(set(data[1]))
        for student_name in stud_data :
            student_name_list.append(student_name)
            for ques_type in stud_data[student_name]:
                allowed_qtype.append(ques_type)
        allowed_qtype = list(set(allowed_qtype))
        allowed_chapters = Questions.objects.filter(subject__subject_name__iexact=subject,chapter_number__in=allowed_chapter_nos).values_list('chapter', flat=True).distinct()
        allowed_chapters = list(allowed_chapters)
        return JsonResponse({"message":"success","chapters":allowed_chapters,"stud_name":student_name_list,"qtype":allowed_qtype})