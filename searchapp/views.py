from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Questions,Mentor
from os.path import join, dirname, abspath
from .parser import parser_of_excel
from django.core.files.storage import default_storage
from django.http import HttpResponse
import tempfile
import os
import xlrd
# Create your views here.


def upload_view(request):
  return render(request,'question_upload_mentor.html')


def add_questions(request):
    if request.method=='POST':

        file_obj=request.FILES['datafile']
        print(file_obj)
        filename =file_obj.name
        if request.FILES['datafile']:
            book=xlrd.open_workbook(file_contents=file_obj.read())
            handle_uploaded_file(book)
            return HttpResponse('added successfully')




def handle_uploaded_file(file):
   # bytes=file.read()   # fname = join(dirname(dirname(abspath(__file__))), 'test_data',file.name)
   # file.save(fname)
    data=User.objects.filter(is_superuser=True)
    print(data)
    _user=data.values_list('username',flat=True)
    _email=data.values_list('email',flat=True)
    _password=data.values_list('password',flat=True)
    print(_password[0])
    check=Mentor.objects.filter(username=_user[0]).count()
    if check==0:
        u=Mentor(username=_user[0],email=_email[0],password=_password[0],mentor_type=1,full_name="john a george",phone="987654321")
        u.save()
    id=Mentor.objects.filter(username=_user[0]).values_list('id',flat=True)[0]

    dict=parser_of_excel(file)
    type=""
    question_weightage=""
    for row in dict:
        if row['Question_type']=='1A'or row['Question_type']=='1B':
            question_weightage=1;
        if(row['Question_type']=='2'):
            question_weightage=2
        if(row['Question_type']=='3'):
            question_weightage=3
        if(row['Question_type']=='4'):
            question_weightage=4
        if(row['Question_type']=='5'):
            question_weightage=5
        if(row['Question_type']=='1A'):
            type=2
        else:
            type=1
        print(Mentor.objects.get(pk=id))
        q=Questions(subject="science",chapter=row['Chapter'],question_type=type,uploaded_by=Mentor.objects.get(pk=id),
                       text=row['Text'],question_weightage=question_weightage)

        q.save()
