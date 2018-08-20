from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .test_paper import generate_test_paper
from .utils.utils import convert_question_bank,get_type_and_weightage
from .test_paper import generate_test_paper
from .models import Questions, Mentor



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
            chapter_to_question=convert_question_bank(file_obj)
            print("after calling function")
            print(chapter_to_question)
            add_to_database(chapter_to_question,subject)
            return HttpResponse("added successfully")
        else:
            return render(request,'question_upload_mentor.html',{'error':"no file selected",'flag':'1'})



def add_to_database(chapter_to_question,subject):
    user_data = User.objects.filter(is_superuser=True)
    _user = user_data.values_list('username', flat=True)
    _email = user_data.values_list('email', flat=True)
    _password = user_data.values_list('password', flat=True)

    check = Mentor.objects.filter(username=_user[0]).count()
    if check==0:
        u = Mentor(username=_user[0], email=_email[0], password=_password[0][:40], mentor_type=1, full_name="john a george", phone="987654321")
        u.save()
    id = Mentor.objects.filter(username=_user[0]).values_list('id',flat=True)[0]

    chapter_no=0
    for chapter in chapter_to_question:
        chapter_no=chapter_no+1
        questions_dict=chapter_to_question[chapter]

        for question_type in questions_dict:
                    questions_list=questions_dict[question_type]
                    type,weightage=get_type_and_weightage(question_type)
                    for i in range(len(questions_list)):
                        chapter_name=chapter.strip()
                        print(chapter_name)
                        print(weightage)
                        q=Questions(chapter_number=chapter_no,subject=subject,chapter=chapter_name,question_type=type,question_weightage=weightage,text=questions_list[i],uploaded_by=Mentor.objects.get(pk=id))
                        q.save()
                        print("data saved")
