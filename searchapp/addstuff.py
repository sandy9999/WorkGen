import sys
sys.path.append('/home/sandy/WorkGen/searchapp/utils')
from utils import *
from .models import Mentor,Questions,MCQOptions
from django.contrib.auth.models import User
# from .utils.utils import *

def add_to_database(chapter_to_question,subject):
    science_breakup = {
        '1A': [5, 5],
        '1B': [5, 5],
        '2': [7, 5],
        '3': [7, 5],
        '5': [2, 2]
    }
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
    print("check1")
    print(chapter_to_question)
    for chapter in chapter_to_question:
        chapter_no=chapter_no+1
        questions_dict=chapter_to_question[chapter]
        print("check2")
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