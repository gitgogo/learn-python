#coding=utf-8
from xlrd import open_workbook
from xlwt import Workbook

test_file=open_workbook('f:\\test.xlsx')
test_sheet=test_file.sheets()[0]
result=Workbook()
result_sheet=result.add_sheet('result',cell_overwrite_ok=True)
count=0
for row in range(1,test_sheet.nrows):
	for col in range(1,test_sheet.ncols):
		if test_sheet.cell(row,1).value<=test_sheet.cell(row,2).value:
			result_sheet.write(row,1,test_sheet.cell(row,1).value)
			count+=1
result_sheet.write(0,0,count/2)
result.save('f:\\result.xls')