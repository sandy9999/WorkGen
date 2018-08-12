import csv
import pandas as pd
import xlrd





def csv_from_excel(workbook):
   # work_book = xlrd.open_workbook(workbook)
   # question_sheet= work_book.sheet_by_name('Question Bank')
    question_sheet=workbook.sheet_by_name('Question Bank')
    question_csv_file= open('question_csv_file.csv', 'w')
    csv_writer = csv.writer(question_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(question_sheet.nrows):
        csv_writer.writerow(question_sheet.row_values(rownum))

    question_csv_file.close()

# runs the csv_from_excel function:
#csv_from_excel("excel.xlsx")

#results = []
#with open('your_csv_file.csv') as File:
    #reader = csv.DictReader(File)
    #for row in reader:
    #    results.append(row)

#print(results)
#print(results[0][0])
#print(results['question text'])
#print(results['subject'])
#print(results['chapter'])
#print(results['question type'])


def parser_of_excel(file):
    csv_from_excel(file)

    error=""
    question_df=pd.read_csv('question_csv_file.csv')
    print(question_df.iloc[:, 1])
    for i in question_df.index:
        if(question_df.iat[i, 1]=='1A' or question_df.iat[i, 1]=='1B' or question_df.iat[i, 1]=='2.0' or question_df.iat[i, 1]=='3.0'or question_df.iat[i, 1]=='4.0' or question_df.isnull().iat[i, 1]):
           print("ok")
        else:
           error="wrong question type"


    print(error)
    print(question_df.isnull().iat[0,2])

    print(question_df)
    print("question_type=")
    print(question_df.iat[0,1])

    dict=[]
    text=""
    question_type=""
    chapters_list=list(question_df.columns.values)
    for chapter_no in range(2,21):
        chapter=chapters_list[chapter_no]
        print(chapter_no)
        print(chapter)
        for i in question_df.index:
            print("i="+str(i))

            #print(question_df.iat[i,chapter_no])
            if question_df.isnull().iat[i,chapter_no]==False:
                print("hi")
                text=question_df.iat[i,chapter_no]
                print(text)
                print(question_df.iat[0,1])
                for j in range(i,-1,-1):
                    print("inside j")
                    if question_df.isnull().iat[j,1]== False:
                        question_type=question_df.iat[j,1]
                        input_list={
                           'Chapter':chapters_list[chapter_no],
                           'Text':text,
                           'Question_type':question_type

                        }
                        dict.append(input_list)
                        print(question_type)
                        break


    print(dict)
    return dict
