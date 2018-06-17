"""
Python-11일차(2018.3.14)
"""

'''
[문제132] emp.csv file에 있는 데이터 중에 100번 사원정보를 출력하세요.
'''
import csv

# sol.1
file = open("c:/python/emp_new.csv","r")  # pointer 정보 file에 저장
emp_read = csv.reader(file)  # 객체정보
for i in emp_read:
    if i[0]=='100':
        print(i)
# ['100', 'King', 'AD_PRES', '', '2003-06-17', '24000', '', '90']


# sol.2
file = open("c:\python\emp_new.csv","r")
emp_read = csv.reader(file)
emp_dict = {}
for i in emp_read:
    emp_dict[i[0]] = i[1:]
emp_dict    
emp_dict.keys()  # emp_id를 key로 설정

emp_dict['100']  # 100번 사원정보


# sol.3
import pandas as pd
from pandas import Series, DataFrame
emp = pd.read_csv("c:\\python\\emp_new.csv", 
                  names = ['emp_id','name','job','mgr_id','hire_date','sal','comm_pct','dept_id'])
emp.columns
emp.index
emp.ix[0]  # 100번 사원정보
emp[emp['emp_id']==100]  # 100번 사원정보
emp.xs(0, axis = 0)


'''
[문제133] emp.csv file에 있는 데이터 중에 직업이 ST_CLERK 인 사원들의 이름과 급여, 직업을 출력하세요
'''
emp.columns
# sol.1
import csv
file = open('c:/python/emp_new.csv','r')
emp_read = csv.reader(file)
for i in emp_read:
    if i[2] == 'ST_CLERK':
        print(i[1],i[5],i[2])


# sol.2 : pandas로 받은 emp 활용(위의 문제 참조)
emp.ix[emp['job']=='ST_CLERK',['name','sal','job']]
emp.loc[emp['job']=='ST_CLERK',['name','sal','job']]
emp[['name','sal','job']][emp['job']=='ST_CLERK']
emp[emp['job']=='ST_CLERK'][['name','sal','job']]


'''
[문제134] 급여 10000 이상인 사원들의 이름과 급여, 입사일를 출력하세요
'''
emp[['name','sal','hire_date']][emp['sal'] >= 10000]
emp.loc[emp['sal'] >= 10000,['name','sal','hire_date']]


'''
[문제135] 급여 10000 이상인 사원들의 이름과 급여, 입사일를 출력하세요. 
          급여를 기준으로 내림차순하세요.
'''
import csv
file = open('c:/python/emp_new.csv','r')
emp_read = csv.reader(file)
x = []
for i in emp_read:
    if float(i[5]) >= 10000:
        x.append([i[1],float(i[5]),i[4]])
x
# 내림차순.1
sorted(x, reverse = True, key = lambda data : data[1])

# 내림차순.2
from operator import itemgetter
sorted(x, reverse = True, key = itemgetter(1))


# pandas
ex_135 = emp[emp['sal'] >= 10000][['name','sal','hire_date']] 
  # sal = sorted(ex_135['sal'].values, reverse = True)

x = []
for i in ex_135.index:
    x.append([i,ex_135.ix[i]['sal']])
x
y = sorted(x, reverse = True, key = itemgetter(1))

idx = []
for i in y:
    idx.append(i[0])
idx

ex_135.ix[idx]  # 최종결과
ex_135.sort_values('sal', ascending = False)  # sort_values


# 선생님 풀이

import  pandas  as  pd
'''
emp = pd.read_csv("c:\data\emp.csv", 
                  names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
'''
print(emp[['name','sal','hire_date']][emp['sal'] >= 10000].sort_values('sal',ascending=False))
            
print(emp.ix[emp['sal'] >= 10000, ['name','sal','hire_date']].sort_values('sal',ascending=False))

print(emp.loc[emp['sal'] >= 10000, ['name','sal','hire_date']].sort_values('sal',ascending=False))

import  csv

def salCheck(data):
    return data[5]

file = open("c:\data\emp.csv",'r')
emp_csv = csv.reader(file)
emp_list = []
for i in emp_csv:
     if (float(i[5]) >= 10000):
         emp_list.append(i)
         
emp_list_sorted = sorted(emp_list, reverse=True, key=salCheck)
    
for i in emp_list_sorted:
    print (i[1],i[5],i[4])


import  csv

file = open("c:\data\emp.csv",'r')
emp_csv = csv.reader(file)
emp_list = []
for i in emp_csv:
     if (float(i[5]) >= 10000):
         emp_list.append(i)

emp_list_sorted = sorted(emp_list, reverse=True, key=lambda x: x[5])

for i in emp_list_sorted:
    print (i[1],i[5],i[4])


'''
[문제136] 급여를 많이 받는 순으로 10위 까지를 구하세요. (연이은 정수)
'''
# sol.1
emp.sort_values('sal', ascending = False).head(13)

# sol.2
empSal_sort = emp.sort_values('sal', ascending = False)  # sal 기준 내림차순
a = empSal_sort.rank(ascending = False,method='dense')['sal']<= 10  # 10위 이내
empSal_sort[a]  # 해당 목록

emp['salRank'] = empSal_sort.rank(ascending = False,method='dense')['sal']
emp[emp['salRank']<=10].sort_values('salRank')


# 선생님 풀이
emp['salRank'] = emp['sal'].rank(ascending = False,method='dense')
emp[emp['salRank']<=10].sort_values('salRank')


'''
[문제137] 직업이 AD_VP, AD_PRES 인 사원들의 이름, 급여, 직업을 출력하세요.
'''
emp[(emp['job'] == 'AD_VP') | (emp['job'] == 'AD_PRES')][['name','sal','job']]

# 선생님 풀이
emp.ix[emp['job'].isin (['AD_VP','AD_PRES']), ['name','sal','job']]


'''
[문제138] 직업이 AD_VP ,AD_PRES 아닌 사원들의 이름, 급여, 직업을 출력하세요.
'''
emp[(emp['job'] != 'AD_VP') & (emp['job'] != 'AD_PRES')][['name','sal','job']]

# 선생님 풀이
emp.ix[~emp['job'].isin (['AD_VP','AD_PRES']), ['name','sal','job']]  # ~ : not
emp.ix[-emp['job'].isin (['AD_VP','AD_PRES']), ['name','sal','job']]


-------------

obj = Series([1,2,3,None,5])  # None : python에서 null 함수
obj

obj.isnull()
pd.isnull(obj)

obj.notnull()
pd.notnull(obj)

obj[obj.notnull()]  # NaN 제외하고 보기
obj.dropna()

obj[obj.isnull()]  # NaN 값 보기


import numpy as np
obj = Series([1,2,3,np.nan,5])  # np.nan : numpy에서 null 함수
obj

from numpy import nan as NA  # 이 세션에서 null을 NA로 쓸게요(편리성)
obj = Series([1,2,3,NA,5])
obj

obj = obj.fillna(0)  # .fillna(0) : NaN -> 0 치환(바로적용은 안됨)
obj

obj.dropna()  # NaN 없애기

lst = [None]
pd.isnull(lst)




df = DataFrame([[1,2,3,],[1,NA,NA],[NA,NA,NA],[NA,2,3]])
df

df.isnull()
pd.isnull(df)

df.dropna()  # NaN 하나라도 있으면 row단위 제외
df.dropna(how = 'all')  # NaN만 전부인 row 제외

df[4] = NA  # 새로운 열 추가하면서 NaN 가득히
df

df.dropna(how = 'all', axis = 1)  # NaN만 전부인 열 제거


df.fillna(0)  # NaN -> 0 치환
df[0].fillna(0) # 0 col만 

df.fillna({0:0,1:1,2:2,4:4})  # col:input, NaN 열별 적용값 다르게 주기

df.fillna(0, inplace = True)  # inplace = True 바로 적용
df


df = DataFrame([[1,2,5],[NA,NA,4],[3,2,NA],[2,NA,3]])
df

df.fillna(method = "ffill")  # NaN 앞의 값으로 채원
df.ffill()

df.fillna(method = "bfill")  # NaN 뒤의 값으로 채원
df.bfill()


'''
[문제139] 커미션이 null 인 사원들의 이름과 커미션을 출력하세요 
'''
emp.ix[emp['comm_pct'].isnull(),['name','comm_pct']]
emp[emp['comm_pct'].isnull()][['name','comm_pct']]
emp[pd.isnull(emp['comm_pct'])][['name','comm_pct']]


'''
[문제140] 커미션이 null이 아닌 사원들의 이름과 커미션을 출력하세요.
'''
emp.ix[~emp['comm_pct'].isnull(),['name','comm_pct']]
emp[~emp['comm_pct'].isnull()][['name','comm_pct']]
emp[~pd.isnull(emp['comm_pct'])][['name','comm_pct']]



s1 = Series([1,2,3])
s1

s1**2  # R처럼 연산가능

def square(x):
    return x**2

square(s1)

# apply함수는 인수값으로 행,열값을 인수값으로 받아서 반복하여 그 함수를 적용
s1.apply(square)
s1.apply(lambda x : x**2)

df = DataFrame([[1,2,3],[4,5,6]])
df

df.apply(square)
df.apply(lambda x : x**2)
df[0].apply(square)
df[0].apply(lambda x : x**3)


df.apply(square, axis = 0)  # 0 : 각 컬럼이 함수에 적용
df.apply(square, axis = 1)  # 1 : 각 행 함수에 적용

df.ix[0,:]

df.apply(np.sum, axis = 0)  # rowSum
df.apply(np.sum, axis = 1)  # colSum


'''
[문제141] 이름 첫글자가 S 로 시작하는 사원들의 이름을 출력하세요.
'''
emp[emp['name'].apply(lambda x : x[0] == 'S')]['name']


abcd12348!












