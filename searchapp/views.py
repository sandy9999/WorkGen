from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.http import HttpResponse

from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db import transaction

import logging

from .utils.utils import convert_question_bank,get_type_and_weightage,default_to_regular
from .test_paper import generate_test_paper
from .models import Mentor, Questions, MCQOptions, Subject

logger = logging.getLogger(__name__)


def student_view(request):
    print("hello")
    template_data=[]
    subject_list = Subject.objects.all().values_list('subject_name', flat=True)
    for i in range(len(subject_list)):
        subject=subject_list[i]
        chap_list=Questions.objects.filter(subject=i)
        row={
          'subject':subject,
          'chap_list':chap_list
        }
        template_data.append(row)
    print(template_data)
    return render(request,'student_view.html',{'data':template_data})


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
            print("So such subject")
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
