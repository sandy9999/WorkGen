import openpyxl as op
from collections import defaultdict

def default_to_regular(d):
    """
        This function converts a nested defaultdict to a dict

        :param d: defaultdict
        :type d: defaultdict
        :returns: equivalent dict
        :rtype: dict
    """
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

def get_allowed_questions(data, allowed_qtypes, allowed_chapters):
    """
        This function gets the parsed marker data as input and filters out chapters and question types according
        to the selection made

        :param data: Dictionary of student_name => (Dictionary of question_type => [(marks_secured, question_number, chapter_number)])
        :param allowed_qtypes: list of allowed question types
        :param allowed_chapters: list of allowed chapters
        :type data: dict
        :type allowed_qtypes: list
        :type allowed_chapters: list
        :returns: Updated data which has allowed_qtypes and allowed_chapters only
        :rtype: Dictionary of student_name => (Dictionary of question_type => [(marks_secured, question_number, chapter_number)])
    """
    updated_data = defaultdict(lambda: defaultdict(lambda: list))
    for student in data:
        qtypes = data[student]
        for qtype in qtypes:
            if qtype in allowed_qtypes:
                updated_data[student][qtype] = [x for x in qtypes[qtype] if x[2] in allowed_chapters]
    updated_data = default_to_regular(updated_data)
    return updated_data

def get_customized_paper(marker_data):
    """
        This function returns a student wise split up of the customized paper given a particular marker data.
        Given the marks of a student, this function finds the ratio of marks_secured_for_a_question/total_marks_for_that_question
        We then take the three least scored chapters and generate questions based on those three chapters.

        :param marker_data: Dictionary of student_name => (Dictionary of question_type => [(marks_secured, question_number, chapter_number)])
        :type marker_data: dict
        :returns: dict
        :rtype: dict
    """
    student_to_chapter = {}
    for student in marker_data:
        student_data = marker_data[student]
        lowest_scored_chapters = []
        for question_type in student_data:
            results_per_questiontype = student_data[question_type]
            ratio_array = [(x[0]/float(question_type[0]), x[2]) for x in results_per_questiontype]
            for result in ratio_array:
                # if he/she scored less that 70% for that question, add that to the list of chapters to prepare
                if result[0] < 0.70:
                    lowest_scored_chapters.append(result)
        lowest_scored_chapters.sort(key=lambda x: x[0])
        student_to_chapter[student] = [x[1] for x in lowest_scored_chapters]
    return student_to_chapter

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

if __name__ == "__main__":
    science_breakup = {
        '1A': [5, 5],
        '1B': [5, 5],
        '2': [7, 5],
        '3': [7, 5],
        '5': [2, 2]
    }
    data = convert_marker_data("data.xlsx", science_breakup)
    customized_data = get_customized_paper(data)
    filtered_data = get_allowed_questions(data, ['1A', '1B'], [3])
    print(filtered_data)