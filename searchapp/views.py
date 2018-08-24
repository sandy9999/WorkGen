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

from .utils.utils import convert_question_bank,get_type_and_weightage,default_to_regular
from .test_paper import generate_test_paper
from .models import Mentor, Questions, MCQOptions, Subject, GeneratedQuestionPaper
from docx import Document

logger = logging.getLogger(__name__)


def student_view(request):
    subject_list = Subject.objects.all().values_list('subject_name', flat=True)
    subject_list = list(subject_list)
    return render(request,'student_view.html',{'data':subject_list})


def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if(form.is_valid()):
            user=form.get_user()
            login(request,user)
            return redirect('searchapp:mentor_view')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})


def logout_view(request):
  logout(request)
  return render_to_response('logout.html')


@login_required(login_url='/login')
def mentor_view(request):
    return render(request, 'mentor_view.html')


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
            return HttpResponse("added successfully")
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
        breakup = {
            '1A': [1, 1],
            '1B': [1, 1],
            '2': [1, 1],
            '3': [1, 1],
            '5': [1, 1]
        }
        # token is basically used to identify paper
        token = hashlib.sha1(datetime.datetime.now().__str__().encode('utf-8')).hexdigest()
        generated_paper = GeneratedQuestionPaper(token=token, mentor=request.user, submitted_date=datetime.datetime.now())
        generated_paper.save()
        generate_test_paper.delay(subject, chapters, breakup, request.user.username, token)
        return JsonResponse({"message":"success", "token": token})
