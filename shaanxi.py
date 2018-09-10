#  date:       首次实现： 2018/8/3
#  author:     张锐祥
#  function:   爬取陕西招生考试信息网上单设本科批次A段录取名单

import urllib.request
import re

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

f = open('./学生信息.txt','w')
i = 0    #计数用的
j = 0    #排版用的
for item in items:
    if(i%9==1 and i!=1):
        f.write(item[1].ljust(20))
        #f.write('\t')
        j = j + 1
    elif(i%9==2 and i!=2):
        pass
    else:
        if(i%9==6 and i!=6):
            f.write(item[0][5:].ljust(20))
        else:
            f.write(item[0].ljust(20))
        #f.write('\t')
        j = j + 1
    i = i + 1
    if(j%8==0):
        f.write('\n')
f.close()
