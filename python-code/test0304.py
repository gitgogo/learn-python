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
#自动化测试
#coding=utf-8
import re
import urllib2
class DouBanSpider(object):
    def __init__(self):
        self.datas=[]
        self.cur_url='http://movie.douban.com/top250?start={page}&filter='
        self.index=1

    def get_page(self,page):
        try:
            my_page=urllib2.urlopen(self.cur_url.format(page=(page-1)*25)).read().decode('utf-8')
        except urllib2.URLError,e:
            print e
        return my_page

    def find_title(self,page_url):
        titles=re.findall(r'<span.*?class="title">(.*?)</span>',page_url,re.S)
        for title in titles:
            if '&nbs' in title:
                continue
            self.datas.append('Top'+str(self.index)+' '+title)
            self.index+=1

    def start_spide(self):
        for i in range(1,5):
            page=self.get_page(i)
            self.find_title(page)

def main():
    print '豆瓣电影top'
    douban=DouBanSpider()
    douban.start_spide()
    for movie in douban.datas:
        print movie
    print '结束...'

if __name__ == '__main__':
    main()