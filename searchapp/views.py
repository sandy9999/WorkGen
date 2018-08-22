from django.shortcuts import render
from .models import Mentor,Questions,MCQOptions
from .utils.utils import *
from django.http import JsonResponse
# from generate_doc import *
# from test.py import *
# from generic.py import *
# from .addstuff import *

# Create your views here.

def student_view(request):
    subject = Questions.objects.order_by('subject').values('subject').distinct()
    chap = Questions.objects.filter(subject='Science')
    template_data = {'subject':subject,'chap':chap}
    return render(request,'student_view.html',template_data)

def upload(request):
    if request.method == 'POST':
        science_breakup = {
        '1A': [5, 5],
        '1B': [5, 5],
        '2': [7, 5],
        '3': [7, 5],
        '5': [2, 2]
        }
        response_data = {}
        response_data['student_name_list'] = []
        response_data['chapter_list']  = []
        worksheetType = request.POST['worksheetType']
        if worksheetType == "customizedWorksheet":
            if len(request.FILES)!=0:
                file_obj = request.FILES['datafile']
                print(file_obj)
                marker_data = convert_marker_data(file_obj,science_breakup)
                for student_name in marker_data:
                    response_data['student_name_list'].append(student_name)
                # append to chapters list same way
                return JsonResponse(response_data)
                

def download_test(request):
    if request.method == 'POST':
        science_breakup = {
        '1A': [5, 5],
        '1B': [5, 5],
        '2': [7, 5],
        '3': [7, 5],
        '5': [2, 2]
        }
        subjectTest = request.POST['subjectTest']
        chapterTest = request.POST['chapterTest']
        generate_test_paper(subjectTest,chapterTest,science_breakup)
    return render(request,'download.html')

def download_generic_random(request):
    if request.method == 'POST':
        science_breakup = {
        '1A': [5, 5],
        '1B': [5, 5],
        '2': [7, 5],
        '3': [7, 5],
        '5': [2, 2]
        }
        subjectGeneric = request.POST['subjectGeneric']
        chapterGeneric = request.POST['chapterGeneric']
        chapterList = chapterGeneric.split(',')
        qtypeGeneric = request.POST['qtypeGeneric']
        qtypeList = qtypeGeneric.split(',')
        noOfQ1Generic = request.POST['noOfQ1Generic']
        noOfQ2Generic = request.POST['noOfQ2Generic']
        noOfQ3Generic = request.POST['noOfQ3Generic']
        noOfQ4Generic = request.POST['noOfQ4Generic']
        noOfQ5Generic = request.POST['noOfQ5Generic']
        random_setting = request.POST['random_setting']
        subjectBreakup = {}
        subjectBreakup['1A'] = noOfQ1Generic
        subjectBreakup['1B'] = noOfQ2Generic
        subjectBreakup['2'] = noOfQ3Generic
        subjectBreakup['3'] = noOfQ4Generic
        subjectBreakup['5'] = noOfQ5Generic
        generateRandomGeneric(subjectGeneric,chapterList,subjectBreakup)
    return render(request,'download.html')

def download_generic_segregated(request):
    if request.method == 'POST':
        science_breakup = {
        '1A': [5, 5],
        '1B': [5, 5],
        '2': [7, 5],
        '3': [7, 5],
        '5': [2, 2]
        }
        subjectGeneric = request.POST['subjectGeneric']
        chapterGeneric = request.POST['chapterGeneric']
        chapterList = chapterGeneric.split(',')
        qtypeGeneric = request.POST['qtypeGeneric']
        qtypeList = qtypeGeneric.split(',')
        noOfQ1Generic = request.POST['noOfQ1Generic']
        noOfQ2Generic = request.POST['noOfQ2Generic']
        noOfQ3Generic = request.POST['noOfQ3Generic']
        noOfQ4Generic = request.POST['noOfQ4Generic']
        noOfQ5Generic = request.POST['noOfQ5Generic']
        random_setting = request.POST['random_setting']
        subjectBreakup = {}
        subjectBreakup['1A'] = noOfQ1Generic
        subjectBreakup['1B'] = noOfQ2Generic
        subjectBreakup['2'] = noOfQ3Generic
        subjectBreakup['3'] = noOfQ4Generic
        subjectBreakup['5'] = noOfQ5Generic
        generateSegregatedGeneric(subjectGeneric,chapterList,subjectBreakup)
    return render(request,'download.html')

def download_customized(request):
    if request.method == 'POST':
        """subjectCustomized = request.POST['subjectCustomized']
        print(subjectCustomized)
        stud_name = request.POST['stud_name']
        print(stud_name)
        chapterCustomized = request.POST['chapterCustomized']
        qtypeCustomized = request.POST['qtypeCustomized']
        print(qtypeCustomized)
        noOfQ1Customized = request.POST['noOfQ1Customized']
        print(noOfQ1Customized)
        noOfQ2Customized = request.POST['noOfQ2Customized']
        noOfQ3Customized = request.POST['noOfQ3Customized']
        noOfQ4Customized = request.POST['noOfQ4Customized']
        noOfQ5Customized = request.POST['noOfQ5Customized']"""
        science_breakup = {
        '1A': [5, 5],
        '1B': [5, 5],
        '2': [7, 5],
        '3': [7, 5],
        '5': [2, 2]
        }
        if len(request.FILES)!=0:
            file_obj = request.FILES['datafile']
            print(file_obj)
            totalchapterlist  = Questions.objects.all().values_list('chapter_number',flat=True).distinct()
            data = convert_marker_data(file_obj,science_breakup)
                # chapterCustomized = chapterCustomized.split(',')
                # print(chapterCustomized)
            filtered_data = get_allowed_questions(data, ['1A', '1B', '2','3','5'], totalchapterlist)
            customized_data = get_customized_paper(filtered_data)
            for key in customized_data:
                generate_test_paper(subject,customized_data[key],science_breakup)
    return render(request,'download.html')


def download(request):
    if request.method == 'POST':
        science_breakup = {
        '1A': [5, 5],
        '1B': [5, 5],
        '2': [7, 5],
        '3': [7, 5],
        '5': [2, 2]
        }
        worksheetType = request.POST['worksheetType']
        if worksheetType == "testWorksheet":
            subjectTest = request.POST['subjectTest']
            chapterTest = request.POST['chapterTest']
        elif worksheetType == "genericWorksheet":
            subjectGeneric = request.POST['subjectGeneric']
            chapterGeneric = request.POST['chapterGeneric']
            chapterList = chapterGeneric.split(',')
            qtypeGeneric = request.POST['qtypeGeneric']
            qtypeList = qtypeGeneric.split(',')
            noOfQ1Generic = request.POST['noOfQ1Generic']
            noOfQ2Generic = request.POST['noOfQ2Generic']
            noOfQ3Generic = request.POST['noOfQ3Generic']
            noOfQ4Generic = request.POST['noOfQ4Generic']
            noOfQ5Generic = request.POST['noOfQ5Generic']
            random_setting = request.POST['random_setting']
            subjectBreakup = {}
            subjectBreakup['1A'] = noOfQ1Generic
            subjectBreakup['1B'] = noOfQ2Generic
            subjectBreakup['2'] = noOfQ3Generic
            subjectBreakup['3'] = noOfQ4Generic
            subjectBreakup['5'] = noOfQ5Generic
            if random_setting == "random":
                generateRandomGeneric(subjectGeneric,chapterList,subjectBreakup)
            elif random_setting == "segregated":
                generateSegregatedGeneric(subjectGeneric,chapterList,subjectBreakup)
            print(Questions.objects.all().values_list('text',flat=True))
            total_chapters_list = Questions.objects.filter(question_type=1,subject="Science",question_weightage=1,chapter__in=['Motion','Gravitation']).values_list('text',flat=True)
        elif worksheetType == "customizedWorksheet":
            subjectCustomized = request.POST['subjectCustomized']
            print(subjectCustomized)
            stud_name = request.POST['stud_name']
            print(stud_name)
            chapterCustomized = request.POST['chapterCustomized']
            qtypeCustomized = request.POST['qtypeCustomized']
            print(qtypeCustomized)
            noOfQ1Customized = request.POST['noOfQ1Customized']
            print(noOfQ1Customized)
            noOfQ2Customized = request.POST['noOfQ2Customized']
            noOfQ3Customized = request.POST['noOfQ3Customized']
            noOfQ4Customized = request.POST['noOfQ4Customized']
            noOfQ5Customized = request.POST['noOfQ5Customized']
            """
            if len(request.FILES)!=0:
                file_obj = request.FILES['datafile']
                print(file_obj)
                totalchapterlist  = Questions.objects.all().values_list('chapter_number',flat=True).distinct()
                data = convert_marker_data(file_obj,science_breakup)
                # chapterCustomized = chapterCustomized.split(',')
                # print(chapterCustomized)
                filtered_data = get_allowed_questions(data, ['1A', '1B', '2','3','5'], totalchapterlist)
                customized_data = get_customized_paper(filtered_data)
                for key in customized_data:
                    generate_test_paper(subject,customized_data[key],science_breakup)
                # add_to_database(convert_question_bank(file_obj),'Science')
            """
                
    # print(request.POST)
    # print(request.FILES)
    return render(request,'download.html')