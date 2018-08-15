import csv
import pandas as pd
import xlrd


def csv_from_excel(workbook):

    question_sheet=workbook.sheet_by_name('Question Bank')
    question_csv_file= open('question_csv_file.csv', 'w')
    csv_writer = csv.writer(question_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(question_sheet.nrows):
        csv_writer.writerow(question_sheet.row_values(rownum))

    question_csv_file.close()


def parser_of_excel(file):

    csv_from_excel(file)
    error_count=0
    error=""
    question_df=pd.read_csv('question_csv_file.csv')

    if(question_df.iloc[0,0]!='Q Type:')
      error_count=1
      error="Error in cell 2A"
      return error,error_count

    for i in question_df.index:
        if(question_df.iat[i, 1]=='1A' or question_df.iat[i, 1]=='1B' or question_df.iat[i, 1]=='2.0' or question_df.iat[i, 1]=='3.0'or question_df.iat[i, 1]=='4.0' or question_df.isnull().iat[i, 1]):
        else:
           error="wrong question type"
           error_count=1
           return error,error_count

    dict=[]
    text=""
    question_type=""
    chapters_list=list(question_df.columns.values)
    for chapter_no in range(2,21):
        for i in question_df.index:
            if question_df.isnull().iat[i,chapter_no]==False:
                text=question_df.iat[i,chapter_no]
                for j in range(i,-1,-1):
                    if question_df.isnull().iat[j,1]== False:
                        question_type=question_df.iat[j,1]
                        input_list={
                           'Chapter':chapters_list[chapter_no],
                           'Text':text,
                           'Question_type':question_type

                       }
                        dict.append(input_list)
                        break
    return dict,error_count
