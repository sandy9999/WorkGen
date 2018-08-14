import openpyxl as op
from collections import defaultdict

def default_to_regular(d):
    if isinstance(d, defaultdict):
        d = {k: default_to_regular(v) for k, v in d.items()}
    return d

def convert_marker_data(marker_path, subject_breakup):
    """
        This function takes the path of the worksheet as an input along with the subject_breakup and returns
        a dictionary of names to score in each question type.

        Note: Please do not leave any mark field empty. If he/she got a zero, enter zero.

        :param marker_path: path of the excel file of the tracker
        :param subject_breakup: dictionay of QuestionType => [total_questions, no_to_attempt] for the given subject
        :type marker_path: str
        :type subject_breakup: str
        :returns: Dictionary of student_name => (Dictionary of question_type => [(marks_secured, question_number, chapter_number)])
        :rtype: dict

        :example subject_breakup:
            {
                '1A': [5, 5],
                '1B': [5, 5],
                '2': [7, 5],
                '3': [7, 5],
                '5': [2, 2]
            }
        :example of return:
            {
                'Akshay': {
                    '1A': [(1,1,1), (1,2,1), (1,3,1), (1,4,1), (1,5,1)],
                    '1B': ...
                    '2': ...
                    '3': ...
                    '5':  ...
                }
            }
    """
    marker = op.load_workbook(marker_path).worksheets[0]
    row_no = -1
    student_to_answer = {}
    for row in marker.rows:
        row_no += 1

        # the first row is the header which has question types
        if row_no == 0:
            header_row = row
        # the second row has the chaper numbers
        elif row_no == 1:
            chapter_row = row
        # this is for every other row that contains data
        else:
            student = row[0].value
            student_to_answer[student] = {}
            question_type_start_row = 1
            question_type = header_row[question_type_start_row].value
            while (question_type != None):
                #  Incase you get a string like '1A' as your question type, thats fine, else if you get a float like 2.0, convert to '2'
                question_type = question_type if type(question_type) == str else str(int(question_type))
                total_questions, questions_to_attempt = subject_breakup[question_type]
                questions_of_given_type = []
                for i in range(question_type_start_row, question_type_start_row + total_questions):
                    question_number = i - question_type_start_row + 1
                    chapter_number = int(chapter_row[i].value)
                    marks_secured = row[i].value
                    questions_of_given_type.append((marks_secured, question_number, chapter_number))
                questions_of_given_type.sort(key=lambda x: x[0], reverse=True)
                questions_of_given_type = questions_of_given_type[:questions_to_attempt]
                student_to_answer[student][question_type] = questions_of_given_type
                question_type_start_row += total_questions
                question_type = header_row[question_type_start_row].value
    return student_to_answer

def convert_question_bank(question_bank_path):
    """
        This function converts the excel file of the question bank to a mapping between chapter name to questions.

        :param question_bank_path: path of the question bank excel file
        :type question_bank_path: str
        :returns: dictionary of chapter_name => (dictionary of question_type => list of questions)
        :rtype: dict

        :example return:
            {
                'Gravitation': {
                    '1A': ['Gravitation is caused by ______', 'There are ___ laws of Kepler', 'Earth has a radius of ___'],
                    '1B': ['Planetary motion blah True?', 'Give reason why the sun...', 'What is a ...?'],
                    '2': ['State the laws', 'What is Kepler', 'WHy is escape velo?'],
                    '3': ['Derive conditions for escape veloty and find it', 'State the Keplers Law and derive', 'What is potential energy'],
                    '4': ['Numerical on free fall', 'Derive the gravitational constant from Newtons Law', 'Find launching speed of satellite']
                    },
                'Sun': {
                    '1A': [],
                    '1B': [],
                    '2': [],
                    '3': [],
                    '4': []
                    }
            }

    """
    question_bank = op.load_workbook(question_bank_path).worksheets[0]
    col_count = -1
    chapter_to_question = defaultdict(lambda: defaultdict(lambda: list))
    for col in question_bank.columns:
        col_count += 1
        if col_count == 0:
            # header_col = col
            continue
        elif col_count == 1:
            question_type_col = col
        else:
            break
    question_type_start_row = 1
    question_type = question_type_col[question_type_start_row].value
    max_questions = 1
    while (question_type != None):
        question_type = question_type if type(question_type) == str else str(int(question_type))
        col_no = -1
        for col in question_bank.columns:
            col_no += 1
            if col_no <= 1:
                continue
            else:
                chapter_name = col[0].value
                if not chapter_name:
                    break
                col = [i.value for i in col]
                temp_col = col[question_type_start_row:]
                questions = temp_col[:temp_col.index2(None)]
                max_questions = max(max_questions, len(questions))
                chapter_to_question[chapter_name][question_type] = questions
        question_type_start_row += max_questions + 1
        question_type = question_type_col[question_type_start_row].value
    chapter_to_question = default_to_regular(chapter_to_question)
    return chapter_to_question
