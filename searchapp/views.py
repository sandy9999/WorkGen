from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
import xlrd
from .models import Questions, Mentor
from .parser import parser_of_excel


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


@login_required(login_url='/upload/login')
def mentor_view(request):
    return render(request, 'mentor_view.html')

@login_required(login_url='/upload/login')
def add_questions_view(request):
    return render(request, 'question_upload_mentor.html')



@login_required(login_url='/upload/login')
def add_questions(request):
    error=""
    if request.method=='POST':
        subject=request.POST['dropdownSubject']
        print(subject)
        if(subject ==""):
            return render(request,'question_upload_mentor.html',{'error':"no subject selected",'flag':'1'})
        if len(request.FILES)!=0:
            file_obj = request.FILES['datafile']
            work_book = xlrd.open_workbook(file_contents=file_obj.read())
            handle_uploaded_file(work_book,subject)
            return HttpResponse("added successfully")
        else:
            return render(request,'question_upload_mentor.html',{'error':"no file selected",'flag':'1'})


def handle_uploaded_file(file,subject):
    user_data = User.objects.filter(is_superuser=True)
    _user = user_data.values_list('username', flat=True)
    _email = user_data.values_list('email', flat=True)
    _password = user_data.values_list('password', flat=True)

    check = Mentor.objects.filter(username=_user[0]).count()
    if check==0:
        u = Mentor(username=_user[0], email=_email[0], password=_password[0], mentor_type=1, full_name="john a george", phone="987654321")
        u.save()
    id = Mentor.objects.filter(username=_user[0]).values_list('id',flat=True)[0]
    dict, count = parser_of_excel(file)
    if(count>0):
        return HttpResponse(dict)
    type = ""
    question_weightage = ""
    for row in dict:
        if row['Question_type']=='1A'or row['Question_type']=='1B':
            question_weightage = 1;
        if(row['Question_type']=='2'):
            question_weightage = 2
        if(row['Question_type']=='3'):
            question_weightage = 3
        if(row['Question_type']=='4'):
            question_weightage = 4
        if(row['Question_type']=='5'):
            question_weightage = 5
        if(row['Question_type']=='1A'):
            type = 2
        else:
            type = 1
        q = Questions(subject=subject, chapter=row['Chapter'], question_type=type, uploaded_by=Mentor.objects.get(pk=id),
                       text=row['Text'], question_weightage=question_weightage)

        q.save()
