from docx import Document
import datetime
import os

def convert_customized_to_doc(questions_mapping, subject):
    document = Document()
    for name in questions_mapping:
        pp = document.add_paragraph()
        stud_name = pp.add_run("Name: " + name)
        stud_name.add_break()
        heading = document.add_heading("EXAM")
        heading.alignment = 1
        heading2 = document.add_heading(subject,level = 2)
        heading2.alignment = 1
        para = document.add_paragraph()
        run = para.add_run()
        run.add_break()
        i = 0
        ct = 0
        for row in questions_mapping[name]:
            if row.get('question_type')=='1A':
                for question in row['question']:
                    ct = ct+1
        section=document.add_paragraph()
        section.add_run("Section A").bold=True
        section.alignment = 1
        subsection = document.add_paragraph()
        subsection.add_run(str(ct) + " questions of 1 marks each")
        subsection.alignment = 1
        for row in questions_mapping[name]:
            if row.get('question_type')=='1A':
                p = document.add_paragraph()
                p.add_run("Attempt only "+str(row['attempt'])+" questions").italic=True
                p.alignment = 1
                for question in row['question']:
                    i = i+1
                    p1 = document.add_paragraph(str(i)+": ")
                    p1.add_run(question)

        para = document.add_paragraph()
        run = para.add_run()
        run.add_break()
        ct = 0
        for row in questions_mapping[name]:
            if row.get('question_type')=='1B':
                for question in row['question']:
                    ct = ct+1
        section=document.add_paragraph()
        section.add_run("Section B").bold=True
        section.alignment = 1
        subsection = document.add_paragraph()
        subsection.add_run(str(ct) + " questions of 1 marks each")
        subsection.alignment = 1
        for row in questions_mapping[name]:
            if row['question_type'] == '1B':
                p = document.add_paragraph()
                p.add_run("Attempt only "+str(row['attempt'])+" questions").italic=True
                p.alignment = 1
                for question in row['question']:
                    i=i+1
                    p1=document.add_paragraph(str(i)+": ")
                    p1.add_run(question)
        
        para = document.add_paragraph()
        run = para.add_run()
        run.add_break()
        ct = 0
        for row in questions_mapping[name]:
            if row.get('question_type')=='2':
                for question in row['question']:
                    ct = ct+1
        section=document.add_paragraph()
        section.add_run("Section C").bold=True
        section.alignment = 1
        subsection = document.add_paragraph()
        subsection.add_run(str(ct) + " questions of 2 marks each")
        subsection.alignment = 1
        for row in questions_mapping[name]:
            if row['question_type'] == '2':
                p=document.add_paragraph()
                p.add_run("Attempt only "+str(row['attempt'])+" questions").italic=True
                p.alignment = 1
                for question in row['question']:
                    i=i+1
                    p1=document.add_paragraph(str(i)+": ")
                    p1.add_run(question)
        
        para = document.add_paragraph()
        run = para.add_run()
        run.add_break()
        ct = 0
        for row in questions_mapping[name]:
            if row.get('question_type')=='3':
                for question in row['question']:
                    ct = ct+1
        section=document.add_paragraph()
        section.add_run("Section D").bold=True
        section.alignment = 1
        subsection = document.add_paragraph()
        subsection.add_run(str(ct) + " questions of 3 marks each")
        subsection.alignment = 1
        for row in questions_mapping[name]:
            if row['question_type'] == '3':
                p=document.add_paragraph()
                p.add_run("Attempt only "+str(row['attempt'])+" questions").italic=True
                p.alignment = 1
                for question in row['question']:
                    i = i+1
                    p1 = document.add_paragraph(str(i)+" : ")
                    p1.add_run(question)

        para = document.add_paragraph()
        run = para.add_run()
        run.add_break()
        ct = 0
        for row in questions_mapping[name]:
            if row.get('question_type')=='5':
                for question in row['question']:
                    ct = ct+1
        section=document.add_paragraph()
        section.add_run("Section E").bold=True
        section.alignment = 1
        subsection = document.add_paragraph()
        subsection.add_run(str(ct) + " questions of 5 marks each")
        subsection.alignment = 1
        for row in questions_mapping[name]:
            if row['question_type'] == '5':
                p = document.add_paragraph()
                p.add_run("Attempt only "+str(row['attempt'])+" questions").italic=True
                p.alignment = 1
                for question in row['question']:
                    i = i+1
                    p1 = document.add_paragraph(str(i)+" : ")
                    p1.add_run(question)
        document.add_page_break()

    filename = "question_worksheet_" + datetime.datetime.now().__str__() + ".docx"
    filepath = os.path.join('searchapp/static/docs', filename)
    document.save(filepath)
    return filepath


def convert_to_doc(questions_mapping, subject):
    document = Document()
    heading = document.add_heading("EXAM")
    heading.alignment = 1
    heading2 = document.add_heading(subject,level = 2)
    heading2.alignment = 1
    para = document.add_paragraph()
    run = para.add_run()
    run.add_break()
    i = 0

    ct = 0
    for row in questions_mapping:
        if row.get('question_type')=='1A':
            for question in row['question']:
                ct = ct+1
    section=document.add_paragraph()
    section.add_run("Section A").bold=True
    section.alignment = 1
    subsection = document.add_paragraph()
    subsection.add_run(str(ct) + " questions of 1 marks each")
    subsection.alignment = 1
    for row in questions_mapping:
        if row.get('question_type')=='1A':
            p = document.add_paragraph()
            p.add_run("Attempt only "+str(row['attempt'])+" questions").italic=True
            p.alignment = 1
            for question in row['question']:
                i = i+1
                p1 = document.add_paragraph(str(i)+": ")
                p1.add_run(question)

    para = document.add_paragraph()
    run = para.add_run()
    run.add_break()
    ct = 0
    for row in questions_mapping:
        if row.get('question_type')=='1B':
            for question in row['question']:
                ct = ct+1
    section=document.add_paragraph()
    section.add_run("Section B").bold=True
    section.alignment = 1
    subsection = document.add_paragraph()
    subsection.add_run(str(ct) + " questions of 1 marks each")
    subsection.alignment = 1
    for row in questions_mapping:
        if row['question_type'] == '1B':
            p = document.add_paragraph()
            p.add_run("Attempt only "+str(row['attempt'])+" questions").italic=True
            p.alignment = 1
            for question in row['question']:
                i=i+1
                p1=document.add_paragraph(str(i)+": ")
                p1.add_run(question)
    
    para = document.add_paragraph()
    run = para.add_run()
    run.add_break()
    ct = 0
    for row in questions_mapping:
        if row.get('question_type')=='2':
            for question in row['question']:
                ct = ct+1
    section=document.add_paragraph()
    section.add_run("Section C").bold=True
    section.alignment = 1
    subsection = document.add_paragraph()
    subsection.add_run(str(ct) + " questions of 2 marks each")
    subsection.alignment = 1
    for row in questions_mapping:
        if row['question_type'] == '2':
            p=document.add_paragraph()
            p.add_run("Attempt only "+str(row['attempt'])+" questions").italic=True
            p.alignment = 1
            for question in row['question']:
                i=i+1
                p1=document.add_paragraph(str(i)+": ")
                p1.add_run(question)
    
    para = document.add_paragraph()
    run = para.add_run()
    run.add_break()
    ct = 0
    for row in questions_mapping:
        if row.get('question_type')=='3':
            for question in row['question']:
                ct = ct+1
    section=document.add_paragraph()
    section.add_run("Section D").bold=True
    section.alignment = 1
    subsection = document.add_paragraph()
    subsection.add_run(str(ct) + " questions of 3 marks each")
    subsection.alignment = 1
    for row in questions_mapping:
        if row['question_type'] == '3':
            p=document.add_paragraph()
            p.add_run("Attempt only "+str(row['attempt'])+" questions").italic=True
            p.alignment = 1
            for question in row['question']:
                i = i+1
                p1 = document.add_paragraph(str(i)+" : ")
                p1.add_run(question)

    para = document.add_paragraph()
    run = para.add_run()
    run.add_break()
    ct = 0
    for row in questions_mapping:
        if row.get('question_type')=='5':
            for question in row['question']:
                ct = ct+1
    section=document.add_paragraph()
    section.add_run("Section E").bold=True
    section.alignment = 1
    subsection = document.add_paragraph()
    subsection.add_run(str(ct) + " questions of 5 marks each")
    subsection.alignment = 1
    for row in questions_mapping:
        if row['question_type'] == '5':
            p = document.add_paragraph()
            p.add_run("Attempt only "+str(row['attempt'])+" questions").italic=True
            p.alignment = 1
            for question in row['question']:
                i = i+1
                p1 = document.add_paragraph(str(i)+" : ")
                p1.add_run(question)

    filename = "question_worksheet_" + datetime.datetime.now().__str__() + ".docx"
    filepath = os.path.join('searchapp/static/docs', filename)
    document.save(filepath)
    return filepath
