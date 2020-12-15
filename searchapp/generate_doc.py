from docx import Document
import json
import datetime
import os

qtype_to_section = {"1A": "A", "1B": "B", "2": "C", "3": "D", "5": "E"}


def get_no_of_questions(questions_mapping, question_type):
    count = 0
    for row in questions_mapping:
        if row.get('question_type') == question_type:
            for question in row['question']:
                count = count + 1
    return count


def add_headings(document, subject):
    heading = document.add_heading("EXAM")
    heading.alignment = 1
    subject_heading = document.add_heading(subject, level=2)
    subject_heading.alignment = 1
    para = document.add_paragraph()
    run = para.add_run()
    run.add_break()


def add_questions(document, questions_mapping, question_type, question_no, no_of_questions):
    section = document.add_paragraph()
    section.add_run("Section " + qtype_to_section[question_type]).bold = True
    section.alignment = 1
    subsection = document.add_paragraph()
    subsection.add_run(str(no_of_questions) + " questions of " + question_type[0] + " marks each")
    subsection.alignment = 1
    for row in questions_mapping:
        if row.get('question_type') == question_type:
            p = document.add_paragraph()
            p.add_run("Attempt only " + str(min(row['attempt'], no_of_questions)) + " questions").italic = True
            p.alignment = 1
            for index, question in enumerate(row['question']):
                question_no = question_no + 1
                p1 = document.add_paragraph(str(question_no) + ": ")
                p1.add_run(question)
                if row['table'][index]:
                    for table_data in row['table'][index]:
                        table_list = json.loads(table_data)
                        row_no = len(table_list)
                        column_no = len(max(table_list,key=len))
                        table = document.add_table(rows=row_no, cols=column_no)
                        for i in range(row_no):
                            table_row = table.rows[i]
                            for j in range(column_no):
                                if j >= len(table_list[i]):
                                    table_row.cells[j].text = ""
                                else:
                                    table_row.cells[j].text = table_list[i][j]
                    
                    

    para = document.add_paragraph()
    run = para.add_run()
    run.add_break()
    return question_no


def convert_customized_to_doc(questions_mapping, subject):
    document = Document()
    for name in questions_mapping:
        para = document.add_paragraph()
        student_name = para.add_run("Name: " + name)
        student_name.add_break()
        add_headings(document, subject)
        question_no = 0
        for qtype in qtype_to_section:
            no_of_questions = get_no_of_questions(questions_mapping[name], qtype)
            if no_of_questions != 0:
                question_no = add_questions(document, questions_mapping[name], qtype, question_no, no_of_questions)
        document.add_page_break()
    filename = "question_worksheet_" + datetime.datetime.now().__str__() + ".docx"
    filepath = os.path.join('searchapp/static/docs', filename)
    document.save(filepath)
    return filepath


def convert_to_doc(questions_mapping, subject):
    document = Document()
    add_headings(document, subject)
    question_no = 0
    for qtype in qtype_to_section:
        no_of_questions = get_no_of_questions(questions_mapping, qtype)
        if no_of_questions != 0:
            question_no = add_questions(document, questions_mapping, qtype, question_no, no_of_questions)
    filename = "question_worksheet_" + datetime.datetime.now().__str__() + ".docx"
    filepath = os.path.join('searchapp/static/docs', filename)
    document.save(filepath)
    return filepath
