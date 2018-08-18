<<<<<<< HEAD
from django.shortcuts import render
import logging
from .models import Mentor,Questions,MCQOptions
# Create your views here.

logger = logging.getLogger(__name__)

def student_view(request):
    subject = Questions.objects.order_by('subject').values('subject').distinct()
    chap = Questions.objects.filter(subject='Science')
    template_data = {'subject':subject,'chap':chap}
    return render(request,'student_view.html',template_data)
=======
from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
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

            return HttpResponse("added successfully")
        else:
            return render(request,'question_upload_mentor.html',{'error':"no file selected",'flag':'1'})
>>>>>>> ui modified 2
