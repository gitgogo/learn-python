#coding=utf-8
from openpyxl import Workbook
import os
import time,random

def make_excel(filename,row):
    addr=raw_input('input the address you want to save: ')
    filepath=os.path.join(addr,filename)
    todo=['learn','play','sleep','eat','bike']
    wb=Workbook(guess_types=True)
    ws=wb.create_sheet(u'result',0)
    ws.append(['Todo list','Time'])
    for i in range(row):
        ws.append([random.choice(todo),time.strftime('%H:%M:%S')])
        time.sleep(2)
    wb.save(filepath)
make_excel('test.xlsx',6)