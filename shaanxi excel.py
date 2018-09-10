#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import re
import xlwt

url = 'http://www.sneac.com/htm/2018/2018dsA-lqmd.htm'
header = {
      'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
      'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
      'Connection': 'keep-alive'
      }

request = urllib.request.Request(url = url,headers = header)
reponse = urllib.request.urlopen(request)
content = reponse.read().decode('gbk')

pat = r'<.*?>(.*?)</td>|(男|女)'
pattern = re.compile(pat)

items = re.findall(pattern,content)

# 创建一个Workbook对象，这就相当于创建了一个Excel文件
book = xlwt.Workbook()
info = book.add_sheet('info')

row = 0
collumn = 0
i = 0   #计数用的

for item in items:
    if(i%9==1 and i!=1):
        info.write(row,collumn,item[1])
        
        if(collumn<7):
            collumn+=1
        else:
            collumn=0
            row+=1
        
    elif(i%9==2 and i!=2):
        pass
    
    else:
        if(i%9==6 and i!=6):
            info.write(row,collumn,item[0][5:])
        else:
            info.write(row,collumn,item[0])
        
        if(collumn<7):
            collumn+=1
        else:
            collumn=0
            row+=1
            
    i = i + 1

book.save('stu_info.xls')



