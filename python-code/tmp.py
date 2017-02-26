#coding=utf-8
import re
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment
from openpyxl import Workbook

def make_excel(row,column):
	wb=Workbook()
	ws=wb.active

	thick = Side(border_style="thick", color="BA55D3")
	double = Side(border_style="double", color="BA55D3")
	border = Border(top=double, left=thick, right=thick, bottom=double)
	font = Font(b=True, color="FF0000")
	al = Alignment(horizontal="center", vertical="center")
	fill = PatternFill("solid", fgColor="FFFF00")
	ws.append([u'姓名',u'性别',u'学号',u'爱好',u'年龄'])
	for i in range(row):
		ws.append([u'张三',u'男',1,u'篮球',20])
	for i in range(1,row):
	    # for j in range(1,column+1):
		for j in range(column):
			my_cell=ws.rows[i][j]
			my_cell.fill=fill
			my_cell.border=border
			my_cell.font=font
			my_cell.alignment=al

	wb.save('f:\\test1.xlsx')
make_excel(7,5)
# print ws.rows
# print ws.rows[1][2].value
# print ws.columns[4][2].value
# print ws.max_column
# print ws.max_row

# for row in ws.iter_rows():
#     for cell in row:
#         print cell,cell.value,cell.coordinate
#     print 

# for row in range(10, 20):
#     for col in range(10, 20):
#         ws.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))  #get_column_letter函数可以把数字转换为列对应的字母
# print(ws['J10'].value)

import os
