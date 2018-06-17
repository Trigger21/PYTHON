"""
Python-7일차(2018.3.8)
"""

## 7-1. 시간(time module)

import time

# 1970년 1월 1일 자정 이후 누적된 초
time.time() 

# 초만큼 정지시킨다.
time.sleep(10)

# 현재시간
time.localtime()

t = time.time()
time.localtime(t)
'''
tm_wday=3, 요일 : 월 0 ~ 일 6
tm_yday=67 (1.1 기준 누적된 날짜 : 1 ~ 366), 
tm_isdst=0 : 일광적약 시간(서머타임) 0, 1, -1
'''

time.localtime().tm_yday

t1 = time.localtime()  # 짧게 사용하려면
t1.tm_mon

# UTC 기준의 표준시
time.gmtime()
time.gmtime(1234567890)  # 발렌타인 & 13일의 금요일


time.asctime()
time.ctime()

time.mktime(time.localtime())


# date -> str
time.strftime('%y %Y %m %d %B %b %h %H %p%I %M %S',time.localtime())
'''
%y : 2자리 년도
%Y : 4자리 년도
%H : 24시간 기준
%I : 12시간 기준
%p : am pm
'''

time.strftime('%A %a %w %j %c',time.localtime())
'''
%A : 긴요일
%a : 짧요일
%w : 일 0, 월 1, 화 2, 수 3, 목 4, 금 5, 토 6
%j : 1.1 ~ 누적된 날짜(1~366)
%c : 날짜, 시간
%x : 월/일/년도
%X : 시:분:초
%W : 누적된 주(월요일 시작)
%U : 누적된 주(일요일 시작) 
%z : 시간대(대한민국표준시)   
'''

time.strftime('%x %X %W %U %z',time.localtime())


# str -> date
time.strptime('2018 7 8','%Y %m %d')


## 7-2. 달력(calendar module)

import calendar

print(calendar.calendar(2018))

# 년도의 달력
calendar.prcal(2019)

# 달의 달력
calendar.prmonth(2018,5)

# 해당 날짜의 요일
calendar.weekday(2018,5,8)

# 그 달의 첫째 날짜의 요일, 마지막 일
calendar.monthrange(2018,3)



## 7-3. csv

import csv

file = open("c:\python\emp_1.csv", "r")  # r : read / 포인터 정보만 가져옴
emp_csv = csv.reader(file)
emp_csv  # csv 객체

# csv 내용 출력
for emp_list in emp_csv:
    print(emp_list)


'''
[문제74] last_name, salary 출력하세요.
'''
file = open("c:\python\emp_1.csv", "r")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[2], emp_list[7])


'''
[문제75] last_name, last_name의 길이를 출력하세요.
'''
file = open("c:\python\emp_1.csv", "r")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[2], len(emp_list[2]))


'''
[문제76] employee_id, last_name, salary를 12달 곱한값 출력하세요.
'''
file = open("c:\python\emp_1.csv", "r")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[0],emp_list[2], int(emp_list[7])*12)


file = open("c:\python\emp_1.csv", "r")
emp_csv = csv.reader(file)
emp_lst = []
for emp_list in emp_csv:
    emp_lst.append(emp_list)
emp_lst

for i in emp_lst:
    print(i[2],i[7])



file = open("c:\python\emp_1.csv", "r")
emp_csv1 = file.read()
emp_csv1 = emp_csv1.split(',')
emp_csv1
for emp_list in emp_csv1:
    print(emp_list)


'''
[문제77] 이름과 커미션을 출력하는데 커미션 ''이면 0으로 출력하시오
'''
def ifnull(var1,var2):
    if var1 == '':
        return var2
    return var1

file = open("c:\python\emp.csv", "r")
empCsv = csv.reader(file)
emp = []
for i in empCsv:
    emp.append(i)

for i in emp:
    print(i[2],ifnull(i[8],0))
    
    
# dict에 넣기
emp_dict = {}
for j in range(len(emp[0])):
    x =[]
    for i in emp[1:]:
        x.append(i[j])
    emp_dict[emp[0][j]] = x

emp_dict.keys()
emp_dict['COMMISSION_PCT']

for i in emp_dict['COMMISSION_PCT']:
    print(ifnull(i,0))

'''
[문제78] 이름은 대문자로 직업은 소문자로 출력하세요.
'''

# dict에 넣기
emp_dict = {}
for j in range(len(emp[0])):
    x =[]
    for i in emp[1:]:
        x.append(i[j])
    emp_dict[emp[0][j]] = x
type(emp_dict)  # dict

# last_name 대문자
type(emp_dict['LAST_NAME'])  # list
for i in emp_dict['LAST_NAME']:
    print(i.upper())

# job_id 소문자
emp_dict['JOB_ID']    
for i in emp_dict['JOB_ID']:
    print(i.lower())


'''
[문제79] 이름 첫글자만 추출해서 소문자로 출력하세요.
'''
for i in emp_dict['LAST_NAME']:
    print(i[0].lower())


'''
[문제80] 이름의 두번째 부터 마지막까지 추출해서 소문자로 출력하세요.
'''
for i in emp_dict['LAST_NAME']:
    print(i[1:].lower())


'''
[문제81] initcap 함수 생성 후 이름 출력해라(첫글자만 대문자)
'''
def initcap(var):
    return var[0].upper() + var[1:].lower()

initcap('chung')  # 'Chung'

for i in emp_dict['LAST_NAME']:
    print(initcap(i))
    
    
'''
[문제82] tailcap 함수 생성 후 이름 출력해라(마지막글자만 대문자)
'''
def tailcap(var):
    return var[:-1].lower() + var[-1].upper()

tailcap('chung')  # 'chunG'

for i in emp_dict['LAST_NAME']:
    print(tailcap(i))
    

'''
[문제83] 이름의 첫번째 철자부터 세번째 철자까지 출력하세요
'''
for i in emp_dict['LAST_NAME']:
    print(i[0:3])

[i[:3] for i in emp_dict['LAST_NAME']]


'''
[문제84] 이름 뒤에서 두글자만 출력하세요.
'''
[i[-2:] for i in emp_dict['LAST_NAME']]


'''
[문제85] 이름과 급여를 출력하는데 월급을 출력할때에 0 대신에 *를 출력하시오!
'''
for i in range(len(emp_dict['EMPLOYEE_ID'])):
    print(emp_dict['SALARY'][i].replace('0','*'),emp_dict['LAST_NAME'][i])


'''
[문제86] 문제85번 결과를 새로운 sal변수에 넣어 주세요
'''
emp_dict['sal'] = []
for i in range(len(emp_dict['EMPLOYEE_ID'])):
    emp_dict['sal'].append(emp_dict['SALARY'][i].replace('0','*'))

emp_dict['sal']


# round()

round(45.926,0)
round(45.926,1)
round(45.926,2)
round(45.926,-1)


import math
math.trunc(45.926)  # 45(소숫점 다 버림)
int(45.926)


'''
[문제87] 이름, 급여, 보너스를 출력하는데, 보너스는 급여의 15% 출력해주세요.
         (단, 보너스는 소숫점은 버리세요.)
'''
import math
for i in range(len(emp_dict['EMPLOYEE_ID'])):
    print(emp_dict['LAST_NAME'][i], 
          emp_dict['SALARY'][i], 
          math.trunc(int(emp_dict['SALARY'][i])*.15))


'''
[문제88] 이름, 입사한 요일(한글)을 출력하세요.
'''
# sol.1 : datetime
days = ['일요일','월요일','화요일','수요일','목요일','금요일','토요일']
from datetime import datetime
for i in range(len(emp_dict['EMPLOYEE_ID'])):
    d = datetime.strptime(emp_dict['HIRE_DATE'][i], '%Y-%m-%d')
    n = int(datetime.strftime(d,'%w'))
    print(emp_dict['LAST_NAME'][i], days[n])


# sol.2 : time
days = ['일요일','월요일','화요일','수요일','목요일','금요일','토요일']
import time
for i in range(len(emp_dict['EMPLOYEE_ID'])):
    d = time.strptime(emp_dict['HIRE_DATE'][i], '%Y-%m-%d')
    n = int(time.strftime('%w',d))
    print(emp_dict['LAST_NAME'][i], days[n])


# sol.3 : tm_wday
days = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
import time
for i in range(len(emp_dict['EMPLOYEE_ID'])):
    d = time.strptime(emp_dict['HIRE_DATE'][i], '%Y-%m-%d')
    n = d.tm_wday
    print(emp_dict['LAST_NAME'][i], days[n])


'''
[문제89] 이름, 입사한 날짜부터 오늘까지 총 몇일 근무했는지 출력하세요.
'''
import time
tl = time.localtime()
for i in range(len(emp_dict['EMPLOYEE_ID'])):
    d1 = time.strptime(emp_dict['HIRE_DATE'][i], '%Y-%m-%d')
    d2 = math.trunc((time.mktime(tl) - time.mktime(d1))/(60*60*24))
    print(emp_dict['LAST_NAME'][i],d2)


# float 과 int의 연산

1 + 1.1
2 - 1.1
2*1.1
2/1.1
1.0/2.0





















