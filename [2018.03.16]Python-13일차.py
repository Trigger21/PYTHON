"""
Python-13일차(2018.3.16)
"""

'''
[문제150]부서번호,급여를 기준으로 내림차순 정렬해서 아래 화면처럼 컬럼정보를 출력하세요.
     deptno  empid         name      sal
105   110.0    205      Higgins  12008.0
106   110.0    206        Gietz   8300.0
8     100.0    108    Greenberg  13208.8
9     100.0    109       Faviet   9900.0
10    100.0    110         Chen   8200.0
12    100.0    112        Urman   7800.0
11    100.0    111      Sciarra   7700.0
13    100.0    113         Popp   6900.0
'''

import pandas as pd
from pandas import Series,DataFrame

emp = pd.read_csv("c:/python/emp_new.csv",
                  names = ['empid','name','job','mgr','h_d','sal','comm','deptno'])
emp
emp[['deptno','empid','name','sal']].sort_values(by = ['deptno','sal'], ascending = False)


'''
[문제151] index 번호 0부터 50까지 부서번호, 급여를 기준으로 내림차순 정렬한 후 아래결과처럼 출력하세요.


    deptno  empid         name      sal
8    100.0    108    Greenberg  13208.8
9    100.0    109       Faviet   9900.0
10   100.0    110         Chen   8200.0
12   100.0    112        Urman   7800.0
11   100.0    111      Sciarra   7700.0
13   100.0    113         Popp   6900.0
'''
ex_151 = emp[['deptno','empid','name','sal']][:51]  # index 0~50
ex_151.sort_values(by = ['deptno','sal'], ascending = False)


'''
[문제152] 50번 부서 사원들의 정보를 급여를 기준으로 내림차순 정렬해서 해서 아래 화면처럼 컬럼정보를 출력하세요.

   empid         name  deptno     sal
21    121        Fripp    50.0  8200.0
20    120        Weiss    50.0  8000.0
22    122     Kaufling    50.0  7900.0
23    123      Vollman    50.0  6500.0
24    124      Mourgos    50.0  5800.0
84    184     Sarchand    50.0  4200.0
'''
ex_152 = emp[emp['deptno'] == 50][['empid','name','deptno','sal']]
ex_152.sort_values(by = 'sal', ascending = False)



## 13-1. type변환

s = Series(['1','2'])
s.sum()  # 12

s.astype(int).sum()  # 지금만 변환될 뿐 


df = DataFrame(['1','2'])
df.sum()
df.astype(int).sum()


s = Series(['1','2','10'])
s.sort_values()  # 문자기준 정렬
s.astype(int).sort_values()  # 숫자기준 정렬


'''
[문제153] 10,20,30,40,50번 부서 사원들의 급여의 총액을 출력하세요.

<화면출력>

10 4400.0
20 19000.0
30 24900.0
40 6500.0
50 156400.0
'''
# sol.1
for i in range(10,51,10):
    print(i,emp.loc[emp['deptno']==i,'sal'].sum())

# sol.2
e = emp['deptno'].unique()
e = e[pd.notnull(e)]
e.sort() # 정렬
e[:5]

for i in emp[']
emp['sal'].apply(lambda x : x['deptno'].isin ([i for i in range(10,51,10)]))

emp[emp[['sal','deptno']].apply(lambda x : x['deptno'] in [i for i in range(10,51,10)])][['sal']].sum()




def groupBySum(arg1,arg2):
    

emp.loc[emp['deptno'].isin ([i for i in range(10,51,10)]),'sal'].sum()


emp[['sal','deptno']].apply(lambda x : x['deptno'].values in [i for i in range(10,51,10)])


emp[['sal','deptno']]['deptno'].values[0]


# 선생님 풀이
deptno_dict = {}
for i in [10,20,30,40,50]:
    dept_sum = emp.loc[emp['deptno']==i,'sal'].sum()
    deptno_dict[i] = dept_sum
deptno_dict


------

s = Series([1,2,3,4,1,2,3,4,1,2,5,6])

# 유일값 찾기
s.unique()
type(s.unique())

# 빈도수 
s.value_counts()
s.value_counts(normalize = True)  # 상대비율값(빈도수/전체수)
s.value_counts(normalize = True) * 100

s.value_counts(sort = False)  # True : 기본값


import numpy as np
df = DataFrame({'a':['a1','a1','a1','a2','a2','a3'],
                'b':['b1','b1','b2','b2','b3',np.nan]})
    
df['a'].unique()
df['b'].unique()

df['a'].value_counts()
df['b'].value_counts(dropna = False)


'''
[문제154] 부서별로 급여 총액을 출력하세요.

<화면 출력>

10 4400.0
20 19000.0
30 24900.0
40 6500.0
50 156400.0
60 28800.0
70 10000.0
80 304500.0
90 58000.0
100 53708.8
110 20308.0
'''
e = emp['deptno'].unique()
e.sort()
e = e[:-1]
e
for i in e:
        print(int(i),emp.loc[emp['deptno']==i,'sal'].sum())


deptno_unique = Series(emp['deptno'].unique())
deptno_unique = deptno_unique.dropna()
deptno_unique = sorted(deptno_unique)
for i in deptno_unique:
        print(int(i),emp.loc[emp['deptno']==i,'sal'].sum())
        

# 선생님 풀이
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from operator import itemgetter
import math

deptno_unique = Series(emp['deptno'].unique())
deptno_unique = deptno_unique.dropna()

deptno_dict = {}

for i in deptno_unique:
    dept_sum = emp.loc[emp['deptno'] == i,'sal'].sum()
    deptno_dict[i] = dept_sum

for k,v in sorted(deptno_dict.items(), key=itemgetter(0)):
    print(math.trunc(k),v)


emp.shape  # (row, col)
emp.columns
emp.dtype


emp2 = emp[['empid','name','job','deptno']]
emp2
emp2.head()  # 앞에서 5줄
emp2.tail()  # 뒤에서 5줄

emp2['deptno'].unique()


## 13-2. groupby

'''방법1'''
emp['sal'].groupby(emp['deptno']).sum()
'''select sum(sal) from emp group by deptno'''

deptno_group = emp['sal'].groupby(emp['deptno'])
deptno_group.sum()
deptno_group.mean()
deptno_group.var()
deptno_group.std()
deptno_group.count()
deptno_group.max()
deptno_group.min()

emp['deptno'].value_counts()  # 10, 40, 70은 1명 뿐이라서 var, std : NaN으로 나옴

dept_group = emp['sal'].groupby([emp['deptno'], emp['job']])
dept_group.sum()
dept_group.mean()
dept_group.var()
dept_group.std()

dept_mean = dept_group.mean()
dept_mean

dept_mean.unstack()  # Cross_Table 처럼 만듬 

'''방법2'''
emp.groupby(['deptno','job'])['sal'].sum()
emp.groupby(['deptno','job'])['sal'].sum().unstack()
emp.groupby(['deptno','job']).count()


emp.groupby('deptno')  # deptno로 그룹핑된 객체

for name, group in emp.groupby('deptno'):  # 그룹별 출력
    print(name)
    print(group)


for (name1, name2), group in emp.groupby(['deptno','job']):  # 그룹별 출력
    print(name1, name2)
    print(group)


'''
[문제155] 년도별로 입사한 인원수 결과를 출력해주세요.
'''
# sol.1
import csv
file = open("c:/python/emp_new.csv","r")
emp_read = csv.reader(file)
x = []
for i in emp_read:
    x.append(i[4][:4])
x_unique = list(set(x))

dict = {}
for i in x:
    cnt = 0
    if i in x_unique:
        cnt += 1
        if i not in dict.keys():
            dict[i] = cnt
        else:
            dict[i] = int(dict[i]) + cnt
dict
len(x) # 107
sum(dict.values())  # 107

dict_sort = sorted(dict.items(), key = itemgetter(0))  # 년도별 정렬

for k,v in dict_sort:
    print(k,v)


# sol.2
year = []
for i in emp['h_d'].values:
    year.append(i[:4])
emp['year'] = Series(year)
emp

emp.groupby('year')['empid'].count()


# sol.3
import csv
file = open("c:/python/emp_new.csv","r")
emp_read = csv.reader(file)
x = []
for i in emp_read:
    x.append(i[4][:4])
x_unique = list(set(x))
for i in sorted(x_unique):
    print(i, x.count(i))



# other.1
emp.groupby(emp['h_d'].apply(lambda x:x[:4]))['empid'].count()

from time import strptime
emp.groupby(emp['h_d'].apply(lambda x: strptime(x,'%Y-%m-%d').tm_year))['empid'].count()


# other.2
file = open("c:/python/emp_new.csv","r")
emp_read = csv.reader(file)
result={}
for i in list(emp_read):
    if i[4][:4] in result:
        result[i[4][:4]]=result[i[4][:4]]+1
    else:
        result[i[4][:4]]=1


for k,v in sorted(result.items(), key=lambda x:x[0]):
    print('년도','인원')
    print(k, v)

# other.3
file = open("c:/python/emp_new.csv","r")
emp_read = csv.reader(file)

date=[]
import time
import datetime as dt

for x in list(emp_read):
    y = time.strptime(x[4], '%Y-%m-%d')
    date.append(time.strftime('%Y', y))

cnt={}
n=0
for i in set(date):
    n= date.count(i)
    cnt[i]=n
cnt


# 선생님 풀이 : str.slice()
emp.groupby(emp['h_d'].str.slice(0,4))['empid'].count()


'''
[문제156] dept.csv 를 dept 리스트 변수안에 아래 모양과 같은 딕셔너리 데이터 유형에 
          데이트를 입력한 후 출력하세요.


{'deptno': '10', 'dname': 'Administration', 'mgr': '200', 'loc': '1700'}
    ↑            ↑
    키           값 


10 Administration 200 1700
20 Marketing 201 1800
30 Purchasing 114 1700
40 Human Resources 203 2400
50 Shipping 121 1500
60 IT 103 1400
70 Public Relations 204 2700
'''

import csv
file = open('c:/python/dept.csv','r')
dept_read = csv.reader(file)

dept = {}
key = ['deptno','dname','mgr','loc']
for i in range(len(key)):
    x = []
    for j in dept_read:
        x.append(j[i])
    dept[key[i]] = x
dept
emp_dict = {}
for j in range(len(emp[0])):
    x =[]
    for i in emp[1:]:
        x.append(i[j])
    emp_dict[emp[0][j]] = x



# 선생님 풀이
import csv
file = open('c:/python/dept.csv','r')
dept_read = csv.reader(file)
dept =[]
for i in  dept_read:
    dept.append({'deptno':i[0],'dname':i[1],'mgr':i[2],'loc':i[3]})
dept
for d in dept:
    print(d['deptno'],d['dname'],d['mgr'],d['loc'])


'''
[문제157] emp.csv 를 emp리스트 변수안에 아래 모양과 같은 딕셔너리 데이터 유형에 
          데이트를 입력한 후 출력하세요.


{'empno': 100, 'ename': King, 'job': AD_PRES, 'mgr': '', 'hiredate': 2003-06-17, 'sal': 24000, 'comm': '', 'deptno': 90}

100 King AD_PRES  2003-06-17 24000  90
101 Kochhar AD_VP 100 2005-09-21 17000  90
102 De Haan AD_VP 100 2001-01-13 17000  90
103 Hunold IT_PROG 102 2006-01-03 9000  60
104 Ernst IT_PROG 103 2007-05-21 6000  60
'''
import csv
file = open('c:/python/emp_new.csv','r')
emp_csv = csv.reader(file)
emp = []
for i in emp_csv:
    emp.append({'empno': i[0], 'ename': i[1], 'job': i[2], 'mgr': i[3], 'hiredate': i[4], 'sal': i[5], 'comm': i[6], 'deptno': i[7]})
for e in emp:
    print(e['empno'],e['ename'],e['job'],e['mgr'],e['hiredate'],e['sal'],e['comm'],e['deptno'])


'''
[문제158] emp.csv, dept.csv 파일을 읽어서 사원의 이름, 부서 이름을 출력하세요.
'''
emp[0]['deptno']
# cnt = 0
for i in range(len(dept)):
    for j in range(len(emp)):
        if dept[i]['deptno']==emp[j]['deptno']:
            print(emp[j]['ename']+'  '+dept[i]['dname'])
            # print(cnt)
            # cnt += 1

# merge
emp_df = pd.read_csv('c:/python/emp_new.csv',
                     names = ['empno','ename','job','mgr','hiredate','sal','comm','deptno'])
dept_df = pd.read_csv('c:/python/dept.csv',
                      names = ['deptno','dname','mgr','loc'])

emp_df.merge(dept_df, left_on='deptno', right_on='deptno')[['ename','dname']]

'''
select ename,
       (select dname
        from dept
        where deptno = e.deptno)
from emp e
'''


'''
[문제159] 사원들의 이름, 부서 이름을 출력하면서 소속부서가 없는 사원도 출력해주세요. 
          마지막에는 총건수도 출력하세요. 
'''
cnt = 0
dept_null = []
for i in range(len(dept)):
    for j in range(len(emp)):
        if dept[i]['deptno']==emp[j]['deptno']:
            print(emp[j]['ename']+'  '+dept[i]['dname'])
            cnt += 1           
        elif i == len(dept)-1 and emp[j]['deptno'] == '':
            print(emp[j]['ename']+'  '+'부서없음')
            cnt += 1 
print(cnt)


# 선생님 풀이
import  csv
empfile = open("c:\data\emp.csv",'r')
deptfile = open("c:\data\dept.csv",'r')
emp_csv = csv.reader(empfile)
dept_csv = csv.reader(deptfile)

emp = []  
dept =[]

for i in  dept_csv:
    dept.append({'deptno':i[0],'dname':i[1],'mgr':i[2],'loc':i[3]})

for j in emp_csv:
    emp.append({'empno':j[0],'ename':j[1],'job':j[2],'mgr':j[3], 'hiredate':j[4],'sal':j[5],'comm':j[6],'deptno':j[7]})

cn = 0
for e in emp:
    if e['deptno'] == '':
        print(e['ename'])
        cn += 1
    else:
        for d in dept:
            if e['deptno'] == d['deptno']:
               print ( e['ename'], d['dname'])
               cn += 1

print(cn)












