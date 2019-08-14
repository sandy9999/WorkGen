from .models import Questions, Chapter
from .utils.utils import get_type_and_weightage
from .generate_doc import convert_customized_to_doc, convert_to_doc
import random
from searchapp.models import GeneratedCustomizedPaper, GeneratedTestAndGenericPaper
from celery import shared_task

def form_test_paper_dictionary(subject, chapters, subject_breakup):
    test_paper_dict=[]
    for question_type in subject_breakup:
        final_list = []
        total_question_no = subject_breakup[question_type][0]
        q_type,weightage = get_type_and_weightage(question_type)
        total_list = Questions.objects.filter(question_type=q_type,
            question_weightage=weightage,
            chapter__in=Chapter.objects.filter(id__in=chapters)).values_list('text',flat=True)
        total_list = list(total_list)        
        total_question_no = min(total_question_no,len(total_list))
        final_list = random.sample(total_list,total_question_no)
        row={
            'question_type':question_type,
            'question':final_list,
            'attempt':subject_breakup.get(question_type,None)[1]
        }
        test_paper_dict.append(row)
    return test_paper_dict

@shared_task
def generate_test_or_generic_paper(subject, chapters, subject_breakup, token, sorted_type):

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
    test_paper_dict = form_test_paper_dictionary(subject, chapters, subject_breakup)
    filepath = convert_to_doc(test_paper_dict, subject)
    GeneratedTestAndGenericPaper.objects.filter(token=token).update(file_path=filepath, is_ready=True)

@shared_task
def generate_customized_paper(subject, chapters, subject_breakup, data, mentor, token):
    '''
    data will be a dictionary of student names to chapter numbers they need more practice in
    here subject_breakup will be of form{
        '1A': [5, 5],
        '1B': [5, 5],
        '2': [7, 5],
        '3': [7, 5],
        '5': [2, 2]
    }
    it returns a list of dicts of form==>{stud_name_1: [{'question_type':'','question':'','attempt':''},{},{}],stud_name_2: [{'question_type':'','question':'','attempt':''},{},{}]}
    '''
    final_dict = {}
    for student_name in data:
        test_paper_dict = form_test_paper_dictionary(subject, data[student_name], subject_breakup)
        final_dict.update({student_name: test_paper_dict})
    filepath = convert_customized_to_doc(final_dict, subject)
    GeneratedCustomizedPaper.objects.filter(mentor__username=mentor, token=token).update(file_path=filepath, is_ready=True)
