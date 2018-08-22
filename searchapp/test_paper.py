from .models import Questions
from .utils.utils import get_type_and_weightage
from .generate_doc import convert_to_doc
import random


def generate_test_paper(subject, chapters, subject_breakup):

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
    test_paper_dict=[]
    for question_type in subject_breakup:
        final_list = []
        total_question_no = subject_breakup[question_type][0]
        q_type,weightage = get_type_and_weightage(question_type)
        total_list = Questions.objects.filter(question_type=q_type,
            subject__subject_name=subject,
            question_weightage=weightage,
            chapter__in=chapters).values_list('text',flat=True)
        total_list = list(total_list)
        final_list = random.sample(total_list,total_question_no)
        row={
            'question_type':question_type,
            'question':final_list,
            'attempt':subject_breakup.get(question_type,None)[1]
         }
        test_paper_dict.append(row)
    document = convert_to_doc(test_paper_dict, subject)
    return document
