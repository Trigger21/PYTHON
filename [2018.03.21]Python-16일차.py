"""
Python-16일차(2018.3.21)
"""

## 파일 이름 가져오기
import os
file='/users/janghyeonan/pythonstudy/yob2016.txt'
name=os.path.basename(file)             #파일 이름 가져오기
name.split('.')[0]

'''
[문제172] emp1.csv, emp2.csv파일을 읽어서 부서별 총액급여를 구하세요. 
          (단, glob을 이용하지 마세요.)
'''
import os
import pandas as pd
from pandas import Series, DataFrame

emp = DataFrame()
for i in range(1,3):
    file = "c:/python/emp/emp{}.csv" .format(i)
    temp = pd.read_csv(file, names = ['eid','name','job','mgr','hd','sal','comm','did'])
    emp = emp.append(temp)
emp

emp[['sal']].groupby(emp['did']).sum()


'''
[문제173] 2016년도에 태어난 아이들의 정보가 들어 있는 year2016파일을 분석해야 합니다. 
          총 출생수를 생성해주세요.

countBirths()
[('yob2016', 3637321)]
'''
# sol.1
import os
import pandas as pd

file = 'c:\python\yob\yob2016.txt'
name = os.path.basename(file)
temp = pd.read_csv(file, header=None)
lst = [(name.split('.')[0], temp[2].sum())]
lst


# sol.2
with open('c:\python\yob\yob2016.txt', "r") as file:
    data = file.readlines()
    a = 0
    for i in data:
        a += int(i.split(',')[-1])
    lst = [(name.split('.')[0], a)]
lst


'''
[문제174] yob2016파일에 있는 데이터를 성별 기준으로 출생수, 총 출생수를 구하세요.
'''
import os
import pandas as pd

yob2016 = pd.read_csv('c:/python/yob/yob2016.txt', names = ['name','sex','birth'])
yob2016

# F : 1756647
yob2016.ix[yob2016['sex']=='F','birth'].sum()

# M : 1880674
yob2016.ix[yob2016['sex']=='M','birth'].sum()

yob2016.groupby('sex')['birth'].sum()

# total : 3637321
sum(yob2016['birth'])


1)pandas
def countBirths():
    import os
    import pandas as pd
    file='desktop/python/yob2016.txt'
    name=os.path.basename(file)
    temp=pd.read_csv('desktop/python/yob2016.txt', header=None)
    a=temp.loc[temp[1]=='M',2].sum()
    b=temp.loc[temp[1]=='F',2].sum()
    lst1=[name.split('.')[0], 'M', a]
    lst2=[name.split('.')[0], 'F', b]
    lst3=[name.split('.')[0], 'total', a+b]
    print(lst1)
    print(lst2)
    print(lst3)

countBirths()
    
2)일반
def countBirths():
    import os
    f='desktop/python/yob2016.txt'
    name=os.path.basename(f)
    with open(f, "r") as file:
        a=0
        b=0
        line=file.readlines()
        for l in line:
            x=l.split(',')
            if x[1]=='M':
                a+=int(x[-1])
            else:
                b+=int(x[-1])
    lst1=[name.split('.')[0], 'M', a]
    lst2=[name.split('.')[0], 'F', b]
    lst3=[name.split('.')[0], 'total', a+b]
    print(lst1)
    print(lst2)
    print(lst3)

countBirths()


'''
https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-national-level-data
'''


'''
[문제175] 2000 ~ 2016년도 년도별 출생수
2000 3777666
2001 3741011
2002 3735651
2003 3799547
2004 3817903
2005 3841440
2006 3952231
2007 3993206
2008 3925486
2009 3814539
2010 3689517
2011 3650434
2012 3648441
2013 3634744
2014 3692930
2015 3683749
2016 3637321 
'''
import os
import glob
import pandas as pd
from pandas import DataFrame

file = 'c:/python/yob/yob*.txt'
file_lst = glob.glob(file)
b = 2000
res = DataFrame()
for i in file_lst:
    if i.find(str(b)) != -1:
        tmp = pd.read_csv(i, header = None)
        total = tmp[2].sum()
        res = res.append(DataFrame([[b,total]], columns = ['년도','출생수'], index = [b-2000]))
        b += 1
res


1)
def countBirths(y1, y2):
    import os
    import pandas as pd
    for y in range(y1, y2+1):
        file='c:/python/yob/yob'+str(y)+'.txt'
        temp=pd.read_csv(file, header=None)
        print(y, temp[2].sum())

countBirths(2000, 2016)

2)
def countBirths(y1,y2):
    for y in range(y1, y2+1):
        f='desktop/python/names/yob'+str(y)+'.txt'
        with open(f, "r") as file:
            line=file.readlines()
            a=0
            for l in line:
                a+=int(l.split(',')[-1])
        print(y, a)
            
countBirths(2000,2016)


# 선생님 풀이

def countBirths():
    ret=[]
    for y in range(2000,2017):
        count=0
        filename='/users/janghyeonan/pythonstudy/yob%d.txt'%y
        with open(filename,'r') as f:
            data=f.readlines()
            for d in data:
                birth = d.split(',')[2]
                count += int(birth)
            ret.append((y,count))
    return ret



result = countBirths()
for year, cn in result:
    print(year,cn)


import os
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

year_cn=[]
all_data = pd.DataFrame()
for y in range(2000,2017):
    filename='/users/janghyeonan/pythonstudy/yob%d.txt'%y
    name = os.path.basename(filename)
    name = name.split('.')[0]
    df = pd.read_csv(filename, names=['name','gender','birth'])
    all_data = all_data.append(df)
    year_cn.append((name[3:],all_data['birth'].sum()))
    print(name[3:],all_data['birth'].sum())
    
    
    
'''
[문제176]  2000 ~ 2016년도 년도별 출생수 결과를 year.txt 파일에 저장하세요.
'''
with open('c:/python/yob/year.txt','w') as file:
    

def countBirths(y1,y2):
    a1=[]
    a2=[]
    for y in range(y1, y2+1):
        a1.append(y)
        f='desktop/python/names/yob'+str(y)+'.txt'
        with open(f, "r") as file:
            line=file.readlines()
            a=0
            for l in line:
                a+=int(l.split(',')[-1])
        a2.append(a)
    import pandas as pd
    x=pd.Series(a2, index=a1)
    return(x)
            
x=countBirths(2000,2016)

with open("desktop/python/year.txt", "w") as file:
    for i in list(x.items()):
        file.write(str(i[0])+'년'+str(i[1])+'명'+'\n')


# 선생님 답안 

def countBirths(): 
    ret=[] 
    for y in range(2000,2017): 
        count=0 
        filename='/users/janghyeonan/pythonstudy/yob%d.txt'%y 
        with open(filename,'r') as f: 
            data=f.readlines() 
            for d in data: 
                birth = d.split(',')[2] 
                count += int(birth) 
            ret.append((y,count)) 
    return ret 

result = countBirths() 
for year, cn in result: 
    print(year,cn) 


with open('/users/janghyeonan/pythonstudy/year.txt','w') as f: 
    for year, birth in result: 
        data = '%s,%s\n'%(year,birth) 
        print(data) 
        f.write(data) 



import os 
import glob 
from pandas import Series, DataFrame 
import pandas as pd 
import numpy as np 

year_cn=[] 
all_data = pd.DataFrame() 
for f in glob.glob("/users/janghyeonan/pythonstudy/yob*.txt"): 
    name = os.path.basename(f) 
    name = name.split('.')[0] 
    df = pd.read_csv(f, names=['name','gender','birth']) 
    all_data = all_data.append(df) 
     
    year_cn.append((name[3:],all_data['birth'].sum())) 
    print(name[3:],all_data['birth'].sum()) 


with open('/users/janghyeonan/pythonstudy/year_1.txt','w') as f: 
    for year, birth in year_cn: 
        data = '%s,%s\n'%(year,birth) 
        print(data) 
        f.write(data) 


import os 
from pandas import Series, DataFrame 
import pandas as pd 
import numpy as np 
import csv 

with open('/users/janghyeonan/pythonstudy/total_year.csv','w') as f: 
    writer = csv.writer(f, delimiter=',') 
    for y in range(2000,2017): 
        filename='/users/janghyeonan/pythonstudy/yob%d.txt'%y 
        name = os.path.basename(filename) 
        name = name.split('.')[0] 
        df = pd.read_csv(filename, names=['name','gender','birth']) 
        writer.writerow([name[3:],df['birth'].sum()]) # csv 모듈안에 들어있는 writerow 를 이용 
        
        
'''
[문제177] 2016년도에 태어난 아이 이름 상위 10까지 보여주세요. 성별 상위 5까지 보여주세요.
'''
1)
def BirthsName(y1):
    from pandas import Series
    a1={}
    f='desktop/python/names/yob'+str(y1)+'.txt'
    with open(f, "r") as file:
        line=file.readlines()
        for l in line:
            if l.split(',')[0] in a1:
                a1[l.split(',')[0]]+=int(l.split(',')[-1])
            else:
                a1[l.split(',')[0]]=int(l.split(',')[-1])
    return(Series(a1).sort_values(ascending=False)[:10])
print(BirthsName(2016))

2)
def BirthsName(y1, g):
    from pandas import Series
    a1={}
    f='desktop/python/names/yob'+str(y1)+'.txt'
    with open(f, "r") as file:
        line=file.readlines()
        for l in line:
            if l.split(',')[1]==g: 
                if l.split(',')[0] in a1:
                    a1[l.split(',')[0]]+=int(l.split(',')[-1])
                else:
                    a1[l.split(',')[0]]=int(l.split(',')[-1])
    return(Series(a1).sort_values(ascending=False)[:5])
print(BirthsName(2016, 'M'))
print(BirthsName(2016, 'F'))



# 선생님 답안 
import pandas as pd  
yob2016 = pd.read_csv('/users/janghyeonan/pythonstudy/yob2016.txt', names=['name','gender','birth']) 

def top(df, n=5, column='birth'): 
    return df.sort_values(by=column, ascending=False)[:n] 

print(top(yob2016 , n=10)) 

print(yob2016.groupby('gender').apply(top))


## 16-1. 파일 이름 가져오기

import os
file='desktop/python/yob2016.txt'
name=os.path.basename(file)             # 파일 이름 가져오기
name.split('.')[0]

**[문제174] yob2016파일에 있는 데이터를 성별 기준으로 출생수, 총 출생수를 구하세요.
import os
def countBirths():
    ret=[]
    fcount = 0
    mcount = 0
    file = 'c:\yob\yob2016.txt'
    name = os.path.basename('c:\yob\yob2016.txt')
    name = name.split('.')[0]
    with open(file,'r') as f:
        data=f.readlines()
        for d in data:
            birth = d.split(',')
            if birth[1] == 'F':
                fcount += int(birth[2])
            else:
                mcount += int(birth[2])
        ret.append((name,'F',fcount))
        ret.append((name,'M',mcount))
        ret.append((name,'Total',fcount+mcount))
    return ret
a = countBirths()
for i in a:
    print(i[:])
    
import pandas as pd 
import os
file = 'c:/yob/yob2016.txt'
name = os.path.basename(file)
name = name.split('.')[0]
yob = pd.read_csv('c:\yob\yob2016.txt', names=['name','gender','birth'])
print(yob.groupby('gender').birth.sum())
print(name,yob['birth'].sum())


## 이력서 작성법
이력서 vs 입사지원서
입사지원서: 이력서만으로 불충분한 세부적 신상 파악, 객관적 자료 확보
이력서는 개인 특성에 따라 이력을 한눈에 파악하기 쉽게 작성
인사담당자 입장에서 직무에 필요한 장점을 써야 함.
http://unijob.co.kr/main/index.html
회원가입하고 연수생 승인 되고 나면 이력서 게시판 업로드
(비공개로, 특정 기업명 들어가지 않도록. 입사지원서 요청 기업은 별도 제출. 유의사항 필독.)
1차 상담은 마음 편하게 오시면 됨. 


'''
[문제176]  2000 ~ 2016년도 년도별 출생수 결과를 year.txt 파일에 저장하세요.
'''
1)
def countBirths():
    ret=[]
    for y in range(2000,2017):
        count=0
        filename='c:\yob\yob%d.txt'%y
        with open(filename,'r') as f:
            data=f.readlines()
            for d in data:
                birth = d.split(',')[2]
                count += int(birth)
            ret.append((y,count))
    return ret

result = countBirths()
for year, cn in result:
    print(year,cn)

with open('c:\yob\year.txt','w') as f:
    for year, birth in result:
        data = '%s,%s\n'%(year,birth)
        print(data)
        f.write(data)

import os
import glob
from pandas import Series, DataFrame
import pandas as pd
import numpy as np


2)
year_cn=[]
all_data = pd.DataFrame()
for f in glob.glob("c:\yob\yob*.txt"):
    name = os.path.basename(f)
    name = name.split('.')[0]
    df = pd.read_csv(f, names=['name','gender','birth'])
    all_data = all_data.append(df)
    year_cn.append((name[3:],all_data['birth'].sum()))
    print(name[3:],all_data['birth'].sum())

with open('c:\yob\year_1.txt','w') as f:
    for year, birth in year_cn:
        data = '%s,%s\n'%(year,birth)
        print(data)
        f.write(data)


3)
import os
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import csv

## 16-2. 정보 가져오면서 바로 write 하는 방법
with open('c:/yob/total_year.csv','w') as f:
    writer = csv.writer(f, delimiter=',')
    for y in range(2000,2017):
        filename='c:\yob\yob%d.txt'%y
        name = os.path.basename(filename)
        name = name.split('.')[0]
        df = pd.read_csv(filename, names=['name','gender','birth'])
        writer.writerow([name[3:],df['birth'].sum()])


'''
[문제177] 2016년도에 태어난 아이 이름 상위 10까지 보여주세요. 성별 상위 5까지 보여주세요.
'''
import pandas as pd 
yob2016 = pd.read_csv('c:\yob\yob2016.txt', names=['name','gender','birth']
def top(df, n=5, column='birth'):
    return df.sort_values(by=column, ascending=False)[:n]
print(top(yob2016 , n=10))
print(yob2016.groupby('gender').apply(top))

