import xlrd
import csv
import pandas as pd





def csv_from_excel(workbook):
    wb = xlrd.open_workbook(workbook)
    sh = wb.sheet_by_name('Question Bank')
    your_csv_file = open('your_csv_file.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

# runs the csv_from_excel function:
csv_from_excel("excel.xlsx")

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
error=""
df1=pd.read_csv('your_csv_file.csv')
print(df1.iloc[:,1])
for i in df1.index:
    if(df1.iat[i,1]=='1A'or df1.iat[i,1]=='1B'or df1.iat[i,1]=='2.0'or df1.iat[i,1]=='3.0'or df1.iat[i,1]=='4.0'or df1.isnull().iat[i,1]):
       print("ok")
    else:
       error="wrong question type"


print( error)


print(df1)
