import csv

def readcsv_Dict(file):
    with open(file,encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def gender(stu_list):
    M = 0  #男的
    F = 0  #女的
    for item in stu_list:
        if(item['性别']=='男'):
            M = M + 1
        if(item['性别']=='女'):
            F = F + 1
    print('男生%d人，女生%d人' % (M,F) )

def gender_and_major(stu_list):
    MandL = 0
    MandW = 0
    WandL = 0
    WandW = 0
    for item in stu_list:
        if(item['性别']=='男' and item['科类']=='理工'):
            MandL+=1
        if(item['性别']=='男' and item['科类']=='文史'):
            MandW+=1
        if(item['性别']=='女' and item['科类']=='理工'):
            WandL+=1
        if(item['性别']=='女' and item['科类']=='文史'):
            WandW+=1
    print('男生理工%d，男生文史%d，女生理工%d，女生文史%d' % (MandL,MandW,WandL,WandW))


if __name__=='__main__':
    
    info = readcsv_Dict('./stu_info.csv')
    info.pop() #最后多了一个
    for item in info:
        item['成绩'] = int(item['成绩'])

    gender(info)
    gender_and_major(info)
    for i in info:
        if(i['性别']=='女' and i['科类']!='理工' and i['科类']!='文史'):
            print(i)
