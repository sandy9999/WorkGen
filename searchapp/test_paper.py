from .models import Questions
from .utils.utils import get_type_and_weightage
from .generate_doc import convert_to_doc
import random
from searchapp.models import GeneratedQuestionPaper
from celery import shared_task


@shared_task
def generate_test_paper(subject, chapters, subject_breakup, mentor, token, random_settings):

    ''' here chapters should be in form of list=['Sun','Gravitation']

    here subject_breakup will be of form{
        '1A': [5, 5],
        '1B': [5, 5],
        '2': [7, 5],
        '3': [7, 5],
        '5': [2, 2]
    }


    it returns a list of dicts of form==>[{'question_type':'','question':'','attempt':''},{},{}]
    '''
    test_paper_dict = []
    for question_type in subject_breakup:
        final_list = []
        total_list = []
        total_question_no = subject_breakup[question_type][0]
        q_type,weightage = get_type_and_weightage(question_type)
        total_list = Questions.objects.filter(question_type=q_type,
            subject__subject_name=subject,
            question_weightage=weightage,
            chapter__in=chapters).values_list('text','chapter_number','chapter')
        total_list = list(total_list)
        final_list = random.sample(total_list,total_question_no)
        final_questions=[]
        if random_settings=='segregated':
            final_list = sorted(final_list,key=lambda s : s[1])

        for tuples in final_list:
            final_questions.append(tuples[0])
        row = {
            'question_type':question_type,
            'question':final_questions,
            'attempt':subject_breakup.get(question_type,None)[1]
         }
        test_paper_dict.append(row)
    print(test_paper_dict)
    filepath = convert_to_doc(test_paper_dict, subject)
    GeneratedQuestionPaper.objects.filter(mentor__username=mentor, token=token).update(file_path=filepath, is_ready=True)
