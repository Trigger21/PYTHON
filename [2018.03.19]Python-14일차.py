"""
Python-14일차(2018.3.19)
"""

'''
[문제160] emp.csv 파일  데이터에 커미션 정보를 분석하려 합니다.
              커미션에 null값들의 수, null이 아닌값들의 수를 구하세요.
'''
# 기존방법
import csv
file = open("c:\python\emp_new.csv","r")
emp_read = csv.reader(file)
cnt_null = 0
cnt_total = 0
for i in emp_read:
    if i[6] == '':
        cnt_null += 1
    cnt_total += 1
print(cnt_null)  # null 수 : 72
print(cnt_total-cnt_null)  # 35


# pandas
import pandas as pd
emp = pd.read_csv("c:\python\emp_new.csv", 
                  names = ['empid','name','job','mgr','hdate','sal','comm','deptno'])
emp
sum(emp['comm'].isnull())  # 72
sum(emp['comm'].notnull()) # 35

emp.comm.count()


'''
[문제161] emp.csv, dept.csv 파일 데이터를 이용해서  조인된 결과를 보려고 합니다.
          조인 함수를 생성하세요.

 
join(emp,'deptno', dept,'deptno')

join(emp,'mgr', emp,'empno')
'''
import csv
file = open("c:\python\emp_new.csv","r")
emp_read = csv.reader(file)
emp_lst = []
for i in emp_read:
    emp_lst.append({'empid':i[0],'name':i[1],'job':i[2],'mgr':i[3],
                    'hdate':i[4],'sal':i[5],'comm':i[6],'deptno':i[7]})

file = open("c:\python\dept.csv","r")
dept_read = csv.reader(file)
dept_lst = []
for i in dept_read:
    dept_lst.append({'deptno':i[0],'dname':i[1],'mgr':i[2],'loc':i[3]})
dept_lst


def join(csv1,col1,csv2,col2):
    for i in csv1:
        for j in csv2:
            if i[col1] == j[col2]:
                print(i,j)

join(emp_lst,'deptno', dept_lst,'deptno')
join(emp_lst,'mgr', emp_lst,'empid')


# merge
pd.merge(emp, dept, on = 'deptno')
pd.merge(emp, emp, left_on = 'mgr', right_on = 'empid')



'''
[문제162] 사원번호를 입력하면 부서이름을 리턴해주는 함수를 생성하세요.

print(dept_name_find(100))

Executive
'''
# sol.1
def dept_name_find(empid):
    for i in emp_lst:
        # print(i['empid'])
        if i['empid'] == str(empid):
            tmp = i['deptno']
            break
    for j in dept_lst:
        if tmp == j['deptno']:
            return j['dname']
dept_name_find(100)  # 'Executive'


# sol.2 : pandas
def dept_name_find(empid):
    return dept[dept['deptno'] == emp[emp['empid']==empid]['deptno'].values[0]]['dname'].values[0]
dept_name_find(100) 


'''
[문제163] emp.csv, dept.csv 파일 데이터에서 50번 부서 사원의 중에 급여가 
          5000 이상인 사원의 이름, 부서 이름을 출력하세요.
'''
emp[(emp['deptno'] == 50) & (emp['sal'] >= 5000)]['empid'].values

for i in emp[(emp['deptno'] == 50) & (emp['sal'] >= 5000)]['empid'].values:
    print(dept_name_find(i))
# Shipping


name_50 = emp[(emp['deptno'] == 50) & (emp['sal'] >= 5000)][['name']]
name_50['dname'] = 'Shipping'
name_50


# 선생님 풀이
for d in dept_lst:
    if d['deptno'] == '50':
        for e in emp_lst:
            if (e['deptno'] == d['deptno']) & (float(e['sal']) >= 5000):
                print(e['name'],d['dname'])
                
for e in emp_lst:
    if (e['deptno'] == '50') & (float(e['sal']) >= 5000):
        for d in dept_lst:
            if d['deptno'] == e['deptno']:
                print(e['name'],d['dname'])


# merge
emp[emp['sal'] >= 5000]
emp_dept = pd.merge(emp, dept, on = 'deptno')
emp_dept.loc[(emp_dept['sal'] >= 5000) & (emp_dept['deptno']==50), ['name','dname']]




## 14-1. merge

import pandas as pd

emp.columns
dept.columns

pd.merge(emp, dept, on = 'deptno')  # join
pd.merge(emp, dept, on = 'deptno')[['name','dname']] 
pd.merge(emp, dept, left_on = 'deptno', right_on = 'deptno')
pd.merge(emp, dept, on = 'deptno', how = 'left')  # left outer join
pd.merge(emp, dept, on = 'deptno', how = 'right')  # right outer join
pd.merge(emp, dept, on = 'deptno', how = 'outer')  # 둘다 outer join(key값 일치 안되는 것까지)
pd.merge(emp, dept, on = 'deptno', how = 'inner')  # 둘다 inner join(key값 일치되는 것만)

# self join
pd.merge(emp, emp, left_on = 'mgr', right_on = 'empid')[['name_x','name_y']]


# emp, dept join를 index를 기준으로 join 하기위해 

dept_new = dept.ix[:10, ['deptno','dname']]
dept_new

dept_new = dept_new.set_index('deptno')  # index를 deptno로 변경
dept_new

del dept_new.index.name  # index name delete
dept_new


pd.merge(emp, dept_new, left_on = 'deptno',right_index = True)


'''
[문제164] emp.csv, dept.csv 파일 데이터에서 50번 부서 사원의 중에 급여가 
          5000 이상인 사원의 이름, 부서 이름을 출력하세요.(pandas이용하세요)
'''
# sol.1
emp_dept = pd.merge(emp, dept, on = 'deptno')
emp_dept.loc[(emp_dept['sal'] >= 5000) & (emp_dept['deptno']==50), ['name','dname']]

# sol.2
dept_50 = dept.loc[dept['deptno']==50, ['deptno','dname']]
dept_50 = dept_50.set_index('deptno')
del dept_50.index.name
dept_50

a = pd.merge(emp, dept_50, left_on = 'deptno', right_index = True, how = 'inner')
a[a['sal'] >= 5000][['name','dname']]


emp[행을 제한한 건의 열][행을 제한]

# 선생님 풀이

empRes = emp[['name','sal','deptno']][(emp['sal'] >= 5000) & (emp['deptno']==50)]
empRes

pd.merge(empRes, dept[['deptno','dname']], on = 'deptno')


'''
[문제165] 2002년도에 근무한 사원들의 이름, 급여, 입사일, 부서코드,부서이름을 출력하세요.
'''
a = [int(i[:4]) for i in emp['hdate']]
emp_2002 = emp[['name','sal','hdate','deptno']][[i==2002 for i in a]]
pd.merge(emp_2002, dept[['deptno','dname']])


# 선생님 풀이
emp_2002 = emp[['name','sal','hdate','deptno']][emp['hdate'].str.slice(0,4) == '2002']
pd.merge(emp_2002, dept[['deptno','dname']])


'''
[문제166] 직업이 AD_VP, AD_PRES 인 사원들의 이름, 급여, 직업, 부서코드, 부서이름 을 출력하세요.
'''
e1 = emp[['name','sal','job','deptno']][emp['job'].isin (['AD_VP','AD_PRES'])]
pd.merge(e1,dept[['deptno','dname']])


# 선생님 풀이

''' 
csv 파일에 header가 있어서 그대로 쓰겠다면
pd.read_csv("  ", header = 0)

내가 지정해서 쓰겠다면
pd.read_csv("  ", names = [' ',' ',' '], header = 0)

header = 0 미기입시 지정한 값은 행이름으로
'''


## multi index(main index, sub index)

from pandas import Series, DataFrame
data = Series(range(10), 
              index = [['a','a','a','b','b','b','c','c','c','d'],
                       [1,2,3,1,2,3,1,2,3,3]])
data
'''
a  1    0
   2    1
   3    2
b  1    3
   2    4
   3    5
c  1    6
   2    7
   3    8
d  3    9
'''

data.index
data['c']
'''
1    6
2    7
3    8
'''

data['b':'c']
'''
b  1    3
   2    4
   3    5
c  1    6
   2    7
   3    8
'''

data[:3]
'''
a  1    0
   2    1
   3    2
'''

data['a']
'''
1    0
2    1
3    2
'''

data.xs('a')
'''
1    0
2    1
3    2
'''

data.xs(('a',3))  # 2
data.xs('a',level=0)  # data.xs('a')
data.xs(3,level=1)  # sub index 해당 값 다 출력

# 많이 쓰임
data.unstack()  # main index : row, sub indes : col
data.unstack().stack()  # 다시 원상태로


df = DataFrame(data)
df
df.index
df.columns

df[0]
df.xs('a')
df.xs(('a',3))  # main index 'a' - sun index 3 : 2
df.xs('a',level = 0)
df.xs(3,level = 1)  # sub index(3) 해당 값 다 출력


