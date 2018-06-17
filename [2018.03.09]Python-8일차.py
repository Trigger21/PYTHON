"""
Python-8일차(2018.3.9)
"""

'''
[문제90] 오늘부터 이번달 말일까지 몇일 남았는지 출력하세요.
'''
from datetime import date
import calendar
calendar.monthrange(2018,3)  # 말일은 3.31
date(2018,3,31) - date.today()  # 22

# 선생님 풀이
from datetime import date
from calendar import monthrange 
monthrange(2018,3)[1] - date.today().day  # 말일 - 현재일


'''
[문제91] 사원번호가 100번 사원의 사원이름과 급여를 출력하세요.
'''
import csv
file = open('c:/python/emp.csv','r')
emp_csv = csv.reader(file)  # 객체 덩어리
emp = []  # emp_csv를 중첩리스트로 emp에 저장
for emp_list in emp_csv:
    emp.append(emp_list) 

for i in emp:
    if i[0] == '100':
        print(i[0], i[2], i[7])


'''
[문제92] 급여가 10000이상인 사원들의 이름과 급여를 출력하세요.
'''
for i in emp[1:]:  # header 제외한 범위
    if int(i[7]) >= 10000:  # str -> int 변환후 논리비교
        print(i[0], i[2], i[7])  # 결과 출력


'''
[문제93] 2001-01-13일에 입사한 사원의 이름과 입사일을 출력하세요.
'''
emp[0]  # header
for i in emp[1:]:
    if i[5] == '2001-01-13':
        print(i[0], i[2], i[5])


'''
[문제94] 2002년도에 입사한 사원들의 이름과 입사일을 출력하세요.
'''
from datetime import datetime
for i in emp[1:]:
    dt = datetime.strptime(i[5], '%Y-%m-%d')
    if datetime.strftime(dt,'%Y') == '2002':
        print(i[0], i[2], i[5])

for i in emp[1:]:
    dt = datetime.strptime(i[5], '%Y-%m-%d')
    if dt.year == 2002:
        print(i[0], i[2], i[5])


'''
[문제95] job이 ST_CLERK이고 월급 3000이상인 사원들의 이름과 job, 급여 출력하세요
'''
emp[0]
for i in emp[1:]:
    if i[6] == 'ST_CLERK' and int(i[7]) >= 3000:
        print(i[0], i[2], i[6], i[7])


'''
[문제96] 급여가 2500에서 3000 사이인 사원들의 이름과 급여를 출력하세요
'''
for i in emp[1:]:
    if 2500 <= int(i[7]) <= 3000:
        print(i[0], i[2], i[7])


'''
[문제97] job AD_VP, AD_PRES인 사원들의 이름과 월급과 직업을 출력하세요
'''
for i in emp[1:]:
    if i[6] in ['AD_VP','AD_PRES']:
        print(i[0], i[2], i[6], i[7])        


'''
[문제98] job AD_VP, AD_PRES이 아닌 사원들의 이름과 월급과 직업을 출력하세요
'''
for i in emp[1:]:
    if not i[6] in ['AD_VP','AD_PRES']:
        print(i[0], i[2], i[6], i[7])    


'''
[문제99] 커미션이 null인 사원들의 이름, 급여, 커미션을 출력하세요
'''
emp[0]
for i in emp[1:]:
    if i[8] == '':
        print(i[0], i[2], i[7], i[8]) 
        
'''
[문제100] 커미션이 null이 아닌 사원들의 이름, 급여, 커미션을 출력하세요.
'''
for i in emp[1:]:
    if i[8] != '':
        print(i[0], i[2], i[7], i[8]) 
        
        
'''
[문제101] last_name의 첫번째 철자가 S로 시작하는 사원들의 이름과 급여를 출력하세요
'''
for i in emp[1:]:
    if i[2][0].upper() == 'S':
        print(i[0], i[2], i[7]) 
        
        
'''
[문제102] last_name의 두번째 철자가 i인 사원들의 이름과 월급을 출력하세요
'''
for i in emp[1:]:
    if i[2][1].lower() == 'i':
        print(i[0], i[2], i[7]) 


# dict에 넣기
emp_dict = {}
for j in range(len(emp[0])):
    x =[]
    for i in emp[1:]:
        x.append(i[j])
    emp_dict[emp[0][j]] = x
    

'''
[문제103] 이름, 급여 출력하는데 이름이 오름차순으로 출력하세요
'''
x=[]
for i in emp[1:]:
    x.append(i[2]+' '+i[7])
x.sort()
print(x)


# 선생님 풀이
def sortCheck(data):
    return(data[1]) # data 인덱스 1번 기준 반환

import csv
file = open('c:/python/emp.csv','r')
emp_csv = csv.reader(file)
emp_list = []
for i in emp_csv:
    emp_list.append(i)

emp_list_sorted = sorted(emp_list, reverse = False, key = sortCheck)
# key : 별도의 함수를 넣는곳(직접 넣으면 X) / 안쓰면 기본 0 인덱스 기준 정렬
# 작동방식 : emp_list가 sortCheck 함수에 들어감
# sorted는 display용, 계속 사용하려면 저장해야 함

for i in emp_list_sorted:
    print(i[1],i[7])



## 8-1. 람다(lambda) 함수

 - 이름이 없는 한줄 짜리 함수
 - 가독성을 위해서
 - 함수를 인수로 넘겨 줄때
 
def f1(x,y):
    return x*y
f1(2,3)  # 6

(lambda x, y : x*y)(2,3)  # 6

f1 = lambda x,y : x*y
f1(2,3)  # 6


# [문제103]-1 : lambda 
import csv
file = open('c:/python/emp.csv','r')
emp_csv = csv.reader(file)
emp_list = []
for i in emp_csv:
    emp_list.append(i)

emp_list_sorted = sorted(emp_list, reverse = False, key = lambda data:data[1])

for i in emp_list_sorted:
    print(i[1],i[5])


# [문제103]-2 : 다른 방법
from operator import itemgetter
file = open('c:/python/emp.csv','r')
emp_csv = csv.reader(file)
emp_list = []
for i in emp_csv:
    emp_list.append(i)
emp_list_sorted = sorted(emp_list, reverse = False, key = itemgetter(2))
# itemgetter(2) : index 2를 기준
emp_list_sorted
for i in emp_list_sorted:
    print(i[2],i[5],i[7])


'''
[문제104] Job ST_CLERK인 사원들의 이름과 입사일과 Job을 출력하는데 가장 최근에
          입사한 사원부터 출력하세요.
'''

emp[0]

# sol.1
emp_sorted = sorted(emp, reverse = False, key = lambda data:data[5])
for i in emp_sorted:
    if i[6] == 'ST_CLERK':
        print(i[2], i[6], i[5])

# sol.2 
from operator import itemgetter
emp_sorted = sorted(emp, reverse = False, key = itemgetter(5))
for i in emp_sorted:
    if i[6] == 'ST_CLERK':
        print(i[2], i[6], i[5])


'''
[문제105] 부서별 급여의 총액을 구하세요.
'''
emp_sorted = sorted(emp[1:], reverse = False, key = lambda data:data[10])

y = set()
z = set()
for i in emp_sorted:
    x = 0
    for j in emp_sorted:
        if i[10] == j[10]:
            x += int(j[7])
            continue
        y.add(x)
    z.add(i[10])
print(z)
print(y)

y = set()
for i in emp_sorted:
    y.add(i[10])
y

# sol.1
import csv
file = open('c:/python/emp.csv','r')
emp_csv = csv.reader(file)
emp = []  # emp_csv를 중첩리스트로 emp에 저장
for emp_list in emp_csv:
    emp.append(emp_list) 
    
emp_sorted = emp[1:]
for i in emp_sorted:
    if i[10] == '':
        i[10] = 0  # 없는 부서는 0
    else:
        i[10] = int(i[10])
emp_sorted = sorted(emp_sorted, reverse = False, key = lambda data:data[10])
emp_sorted


emp_dict = {}
for i in emp_sorted:
    if i[10] in emp_dict:
        emp_dict[i[10]] = int(emp_dict[i[10]]) + int(i[7])
    else:
        emp_dict[i[10]] = int(i[7])
emp_dict



# 선생님 풀이
import csv
file = open('c:/python/emp_1.csv','r')  # header 없는 emp
emp_csv = csv.reader(file)
dept_sum = {}
for emp_list in emp_csv:
    if emp_list[10] in dept_sum:
        dept_sum[emp_list[10]] = float(dept_sum[emp_list[10]]) + float(emp_list[7])
    else:
        dept_sum[emp_list[10]] = float(emp_list[7])

for k,v in dept_sum.items():
    print(k,v)


# 숙제 : 부서코드 오름차순으로 출력되게
'''
[문제106] 부서별 급여의 총액을 구하세요. 아래 결과 처럼 출력하세요.

10 4400.0
20 19000.0
30 24900.0
40 6500.0
50 156400.0
60 31584.6
70 10000.0
80 304500.0
90 82655.1
100 51608.0
110 20308.0
non 7000.0
'''
import csv
file = open('c:/python/emp.csv','r')
emp_csv = csv.reader(file)
emp = []  # emp_csv를 중첩리스트로 emp에 저장
for emp_list in emp_csv:
    emp.append(emp_list) 
    
emp_sorted = emp[1:]
for i in emp_sorted:
    if i[10] == '':
        i[10] = 'non'  # 없는 부서는 0
    else:
        i[10] = int(i[10])
emp_sorted = sorted(emp_sorted, reverse = False, key = lambda data:data[10])
emp_sorted

emp_dict = {}
for i in emp_sorted:
    if i[10] in emp_dict:
        emp_dict[i[10]] = int(emp_dict[i[10]]) + int(i[7])
    else:
        emp_dict[i[10]] = int(i[7])
emp_dict

# 선생님 풀이
import csv
import operator

file = open("c:\data\emp.csv",'r')
emp_csv = csv.reader(file)
dept_sum = {}
for emp_list in emp_csv:
    if emp_list[10] in dept_sum:
        dept_sum[emp_list[10]] =  float(dept_sum[emp_list[10]])+float(emp_list[7])
    else:
        dept_sum[emp_list[10]] =  float(emp_list[7])

#for k,v in sorted(dept_sum.items(), key=operator.itemgetter(0)):
#    if k == '':
#        print('non',v)
#    else:
#        print(k,v)

def get_key(key):
    if key == '':
        return int(1000)
    else:
        return int(key)
   
for k,v in sorted(dept_sum.items(), key = lambda k:get_key(k[0])):
    if k == '':
        print('non',v)
    else:
        print(k,v)


dept_sum.items()[0]
