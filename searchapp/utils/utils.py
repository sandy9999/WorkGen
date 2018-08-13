import openpyxl as op

def convert_marker_data(marker, subject_breakup):
    """
        This function takes the path of the worksheet as an input along with the subject_breakup and returns
        a dictionary of names to score in each question type

        :param marker: path of the excel file of the tracker
        :param subject_breakup: dictionay of QuestionType => [total_questions, no_to_attempt] for the given subject
        :type marker: str
        :type subject_breakup: str
        :returns: Dictionary of student_name => (Dictionary of question_type => [(marks_secured, question_number, chapter_number)])

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