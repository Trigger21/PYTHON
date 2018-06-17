"""
Python-15일차(2018.3.20)
"""

'''
[문제167] 부서이름별 총액 급여를 출력하세요.
'''
import pandas as pd
# emp
emp = pd.read_csv("c:/python/emp_new.csv",
                  names = ['empno','name','job','mgr','hdate','sal','comm','deptno'])
emp

# dept
dept = pd.read_csv("c:/python/dept.csv",
                   names = ['deptno','dname','mgr','loc'])
dept

# join
join = pd.merge(emp[['deptno','sal']], dept[['deptno','dname']])

# 답
join[['sal']].groupby(join['dname']).sum()


# 선생님 풀이 : 집계값 구함 -> join
from pandas import Series, DataFrame
e = emp['sal'].groupby(emp['deptno']).sum()
type(e)  # Series
e = DataFrame(e)  # Series ~ DataFrame join이 안됨, 그래서 변형
e
e = e.reindex([i for i in range(10,111,10)])  # index join을 위해
m = pd.merge(dept[['deptno','dname']], e, left_on = 'deptno', right_index = True)
m['sal'].groupby(m['dname']).sum()


## 15-1. groupby 추가기능(여러개 그룹, 여러개 함수)

emp['sal'].groupby([emp['deptno'],emp['job']]).sum()

empgroup = emp.groupby(['deptno','job'])  # 그룹화 기준
empsal = empgroup['sal']  # 집계값 대상

empsal.agg('sum')  # 적용함수 1개
empsal.agg(['sum','mean','count','max','min'])  # 적용함수 2개 이상


## 15-2. list 원소에 대한 조작

lst = [10,20,30,40,50]

'''화면결과(함술를 만들어서)
   20,40,60,80,100'''

lst * 2  # 실패

def f1(x): 
    return x * 2
f1(lst)  # 실패

[i*2 for i in lst]  # 성공

# sol.1
def f2(x):
    return [i*2 for i in x]
f2(lst)


# sol.2
def f2(x):
    res = []
    for i in x:
        res.append(i*2)
    return res
f2(lst)


(lambda x : x*2)(lst)  # 실패(해결방법은 아래)


# sol.3 : map() 인자값을 가지고 반복수행 하게 해주는 함수
map(lambda x : x*2, lst)  # map 객체 생성
list(map(lambda x : x*2, lst))  # 성공


# sol.4
def f1(x): 
    return x * 2
list(map(f1,lst))

'''map(함수, 반복해야할 자료형)는 함수와 반복가능한 자료형을 입력 받아서
   입력받은 자료형의 각 요소가 함수에 의해 수행된 결과를 묶어서 리턴하는 함수'''



'''
[문제168] x변수에는 1,2,3,4,5  y변수에는 6,7,8,9,10 들어 있다. 
          f(x,y) = x2 + y 를 구하세요.(lambda, map 함수를 이용하세요)
'''
x = [1,2,3,4,5]
y = [6,7,8,9,10]

list(map(lambda x,y : x*2 + y, x,y))


# 선생님 풀이
f = lambda x,y : x*2 + y
x = [1,2,3,4,5]
y = [6,7,8,9,10]
list(map(f,x,y))


## 15-3. pandas map

from pandas import Series, DataFrame
import pandas as pd

x = pd.Series([1,2,3], index = ['one','two','three'])
x
y = pd.Series(['하나','둘','셋'], index = [1,2,3])
y

'''Series를 merge처럼 합하고 싶을때'''
x.map(y)



'''
[문제169] emp.csv는 pandas로 읽고  dept.csv는 일반 csv로 읽어 들인 후 조인을 수행하세요.
'''
import pandas as pd
emp = pd.read_csv('c:/python/emp_new.csv',
                  names = ['empno','name','job','mgr','hdate','sal','comm','deptno'])
emp

import csv
file = open('c:/python/dept.csv','r')
dept_read = csv.reader(file)
dict = {}
for i in dept_read:
    # if i[0] != dict:
    dict[int(i[0])] = i[1]  
dict
dept_Series = Series(dict)
dept_Series
dept_DF = DataFrame(dept_Series)
dept_DF

pd.merge(emp, dept_DF, left_on = 'deptno', right_index = True)  # merge

emp['dname'] = emp['deptno'].map(dept_Series)  # map 활용
emp[['empno','deptno','dname']]


import csv
file = open('c:/python/dept.csv','r')
dept_read = csv.reader(file)
list(map(lambda x : Series(x), dept_read)) 
    

# 선생님 풀이
from pandas import Series, DataFrame
import pandas as pd
import csv

emp = pd.read_csv("c:\data\emp.csv", 
                  names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])

deptfile = open("c:\data\dept.csv",'r')
dept_csv = csv.reader(deptfile)
dept = {}

for i in dept_csv:
    if i[0] != dept:
        dept[int(i[0])] = i[1]

for k,v in dept.items():
    print(k,v)

emp['dname']=emp['deptno'].map(dept)
print(emp[['empid', 'deptno','dname']])


'''
[문제170] happiness 변수에 문장이 있습니다. 행복이란 단어가 몇개 나오는지 분석하시고, 
          위치정보도 출력해주세요.

happiness = '우리나라 「헌법」 제10조는 “모든 국민은 인간으로서의 존엄과 가치를 가지며, 
             행복을 추구할 권리를 가진다”라고 규정하고 있다.행복추구권은 근대 입헌민주주의의 
             핵심인 개인주의·자유주의를 그 사상적 기반으로 하고 있다. 행복추구권에 있어서 
             행복은 다의적인 개념으로, 각자의 생활조건이나 가치관에 따라 다르게 이해될 수 있으나,
             최소한 인간적인 고통이 없는 상태 내지 만족감을 느낄 수 있는 행복한 상태를 의미한다.'
'''
happiness = '우리나라 「헌법」 제10조는 “모든 국민은 인간으로서의 존엄과 가치를 가지며, 행복을 추구할 권리를 가진다”라고 규정하고 있다.행복추구권은 근대 입헌민주주의의 핵심인 개인주의·자유주의를 그 사상적 기반으로 하고 있다. 행복추구권에 있어서 행복은 다의적인 개념으로, 각자의 생활조건이나 가치관에 따라 다르게 이해될 수 있으나, 최소한 인간적인 고통이 없는 상태 내지 만족감을 느낄 수 있는 행복한 상태를 의미한다.'

happiness.count('행복')  # 5
a = happiness.find('행복')
print('단어의 위치:', a)

a += 1
while happiness.find('행복', a) != -1:
    a = happiness.find('행복', a)
    print('단어의 위치:', a)
    a += 1



happy = happiness.split('행복')
total = 0
for i in happy:
    n = len(i)
    total += n
    print(total)

happiness[120]


## 15-4. 파일 입출력

'''      파일 생성
         파일 객체 = open(파일이름, 파일열기모드)
         파일 모드
         - r : 읽기(파일읽기)
         - w : 쓰기(기존의 파일이 있을 경우는 파일 안에 내용이 전부 지워지고
                    열린다, 파일이 없는 경우는 새로운 파일이 생성된다)
         - a : 추가
'''
file = open('c:/python/test.txt','w')  # 객체생성       
file.write('행복하자')  # 파일 입력
file.close()  # 파일 닫기(session 유지되면 계속 열려있음, 습관적으로 해주자)


file = open('c:/python/test.txt','w') 
for i in range(1,11):
    content = "%d 번째줄 .... \n" %i
    file.write(content)
file.close()

file = open('c:/python/test.txt','a') 
for i in range(11,21):
    content = "%d 번째줄 .... \n" %i
    file.write(content)
file.close()


import os
os.path.exists('c:/python/test.txt')  # 파일의 존재여부 확인
os.path.exists('c:/python/test1.txt')


file = open('c:/python/test.txt','w') 
for i in range(1,11):
    content = "{} 번째줄 .... \n" .format(i)
    file.write(content)
file.close()


# 파일읽기
file = open('c:/python/test.txt','r')
data = file.readline()  # 1째 줄만 읽고 끝남
print(data)
file.close()


# 다 읽으려면
file = open('c:/python/test.txt','r')
for i in range(10):
    print(file.readline())


file = open('c:/python/test.txt','r')
while True:
    data = file.readline()
    if not data:
        break
    print(data,end='')  # end = '' : 공백 미발생


file = open('c:/python/test.txt','r')
print(file.read())  # readlines와 같으면서 공백도 발생이 안하는 것


file = open('c:/python/test.txt','r')
data = file.readlines()  # 모든 라인을 읽어서 리스트에 저장
print(data)
file.close()


file = open('c:/python/test.txt','r')
data = file.readlines()  # 모든 라인을 읽어서 리스트에 저장
for i in data:
    print(i, end = '')
file.close()


# with문(sql, inline view 재호출)

with open('c:/python/test.txt', 'w') as file:  # file.close() 자동으로 됨
    file.write("복습하자")


with open('c:/python/test.txt', 'r') as file:
    line = file.readline()
    print(line)

        
with open('c:/python/test.txt', 'r') as file:
    line = file.readline()
    for i in line:
        print(i, end = '')


lines = ['안녕하세요','제임스딘 입니다.']
with open('c:/python/hello.txt','w') as file:
    for i in lines:
        file.write(i+'\n')

with open('c:/python/hello.txt','r') as file:
    print(file.read())


'''
[문제171] happiness 변수에 단어의 수를 구하세요.(공백문자를 기준)
'''
happiness = '우리나라 「헌법」 제10조는 “모든 국민은 인간으로서의 존엄과 가치를 가지며, 행복을 추구할 권리를 가진다”라고 규정하고 있다.행복추구권은 근대 입헌민주주의의 핵심인 개인주의·자유주의를 그 사상적 기반으로 하고 있다. 행복추구권에 있어서 행복은 다의적인 개념으로, 각자의 생활조건이나 가치관에 따라 다르게 이해될 수 있으나, 최소한 인간적인 고통이 없는 상태 내지 만족감을 느낄 수 있는 행복한 상태를 의미한다.'
len(happiness.split(' '))



# 여러개의 파일을 읽어야 할 때 : glob
c:/python/emp1.csv
c:/python/emp2.csv

import os
import glob  # 파일관리
import pandas as pd
from pandas import Series, DataFrame

file = 'c:/python/emp/emp*.csv'  # 여러개 파일이라면 *으로 한번에 담는다
file_list = glob.glob(file)  # file에 대해서 물리적으로 찾는것
file_list


emp = pd.DataFrame()  # 초기화
for i in file_list:
    temp = pd.read_csv(i,names = ['empid','name','job','mgr','hdate','sal','comm','deptno'])
    emp = emp.append(temp)  # rbind
emp
    
emp['sal'].groupby(emp['deptno']).sum()

