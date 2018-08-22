from .models import Questions
from .utils.utils import get_type_and_weightage
from .generate_doc import convert_to_doc
import random

def generateRandomGeneric(subject,chapters,subjectBreakup):
    """
        Basically Paper contains a list [{'1A',[1A question list]},{'1B',[1B question list]},{'2',[2 question list]},{'3',[3 question list]},{'5',5 question list]}]
    """
    Paper = []
    for questionType in subjectBreakup:
        finalQList = [] #Contains the final list of questions
        qtype,weightage = get_type_and_weightage(questionType)
        totalQList = Questions.objects.filter(questionType=qtype,subject=subject,question_weightage = weightage, chapter__in=chapters).values_list('text',flat=True)
        listOfIndices = []
        for i in range(len(totalQList)):
            listOfIndices.append(i)
        randomNo = random.sample(listOfIndices,subjectBreakup[questionType])
        for i in randomNo:
            question = totalQList[i]
            finalQList.append(question)
        row={
            'question_type':questionType,
            'question':finalQList
        }
        Paper.append(row)
    convert_to_doc(Paper)
    return Paper

def generateSegregatedGeneric(subject,chapters,subjectBreakup):
    Paper = []
    for questionType in subjectBreakup:
        finalQList = []
        qtype,weightage = get_type_and_weightage(questionType)
        totalQList = Questions.objects.filter(questionType=qtype,subject=subject,question_weightage = weightage, chapter__in=chapters).order_by('-chapter_no').values_list('text',flat=True)
        listOfIndices = []
        for i in range(len(totalQList)):
            listOfIndices.append(i)
        randomNo = random.sample(listOfIndices,subjectBreakup[questionType])
        for i in randomNo:
            question = totalQList[i]
            finalQList.append(question)
        row={
            'question_type':questionType,
            'question':finalQList
        }
        Paper.append(row)
    convert_to_doc(Paper)
    return Paper
