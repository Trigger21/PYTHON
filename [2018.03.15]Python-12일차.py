"""
Python-12일차(2018.3.15)
"""

'''
[문제142] 이름이 g로 끝나는 사원들의 이름, 급여 출력하세요
'''
# sol.1 : 3줄
import csv
file = open("c:/python/emp_new.csv","r")
emp_read = csv.reader(file)
for i in emp_read:
    if i[1][len(i[1])-1] == 'g':
        print(i[1],i[5])


# sol.2 : 2줄
import pandas as pd
emp = pd.read_csv("c:/python/emp_new.csv",
                  names = ['e_id','name','job','mgr','hd','sal','pct','d_id'])
emp
emp.columns


a = [i for i in emp['name'] if i[len(i)-1]=='g']  # 해당조건 이름
emp[['name','sal']][emp['name'].isin (a)]



# sol.3 : 1줄
emp[emp['name'].apply(lambda x : x[-1] == 'g')][['name','sal']]


'''
[문제143] 110번 사원의 급여보다 많이 받는 사원의 이름, 급여 출력하세요.
'''
# sol.1
a = emp.loc[emp['e_id']==110,'sal']
emp[emp['sal'].apply(lambda x : x > float(a.values))][['name','sal']]


# sol.2
import csv
file = open("c:/python/emp_new.csv","r")
emp_read = csv.reader(file)
for i in emp_read:
    if i[0] == '110':
        lst = i[:]
file = open("c:/python/emp_new.csv","r")
emp_read = csv.reader(file)
for i in emp_read:
    if float(i[5]) > float(lst[5]):
        print(i[1],i[5])


'''
[문제144] 관리자 사원의 이름, 입사일, 급여 출력하세요.
'''
# sol.1
a = [i for i in emp['e_id'] if i in emp['mgr'].values]
emp[emp['e_id'].isin (a)][['name','hd','sal']]

# sol.2
emp[emp['e_id'].apply(lambda x : x in emp['mgr'].values)][['name','hd','sal']]

# sol.3
emp[emp['e_id'].isin (emp['mgr'])][['name','hd','sal']]


'''
[문제145] 101번 사원의 관리자 이름, 입사일, 급여정보를 출력하세요.
'''
a = emp[emp['e_id']==101]
emp[emp['e_id'].apply(lambda x : x == a['mgr'].values[0])][['name','hd','sal']]


mgr_name = emp[emp['e_id'].apply(lambda x : x in emp['mgr'].values)]['name'].values
mgr_name

emp['mgr'].isin (emp[emp['name'].isin (mgr_name)]['e_id'])


emp[emp['e_id']==101][['mgr','hd','sal']]


for i in emp['mgr'].values:
    if i in emp[emp['e_id'].apply(lambda x : x in emp['mgr'].values)]['e_id'].values:
                
    
# 선생님 풀이
mgr = emp[['mgr']][emp['e_id']==101].values
mgr
emp[['name','hd','sal']][emp['e_id'] == float(mgr[0])]
    

# 선생님 왈 : 자료형 중요하다
    
    
집계함수

'''
오라클 성능 고도화 원리와 해법1-2
엔코아 : 모델링 회사
엑셈 : 조종환 대표 / 조동욱 책
'''


## 12-1. 집계함수

from pandas import Series, DataFrame
import numpy as np
s = Series([2,4,8,np.nan,6])
s

s.sum()  # NaN 제외하고 더한다
s.sum(skipna = True)

s.sum(skipna = False)  # nan 있으면 계산불가

s.mean()  # NaN 제외하고 평균

s.var()  # NaN 제외하고 분산

s.std()  # NaN 제외하고 표준편차

s.max()
s.min()
s.cumsum()  # 누적합
s.idxmin()  # s.min() index
s.idxmax()  # s.max() index
s[s.idxmin()]  # s.min()
s[s.idxmax()]  # s.max()

s.describe()  # R : summary()
'''
count    4.000000
mean     5.000000
std      2.581989
min      2.000000
25%      3.500000
50%      5.000000
75%      6.500000
max      8.000000
'''

s.count()  # 4(NaN 제외건수)
len(s)  # 전체건수


df = DataFrame([[60,80,70],[50,75,83],[90,83,81]],
               index = ['홍길동','박찬호','손흥민'],
               columns = ['영어','수학','국어'])
df
df.sum()
df.sum(axis = 0)  # colSum()
df.sum(axis = 1)  # rowSum()
np.sum(df)

df.mean(axis = 1)
df.mean()

제임스 영어(100), 수학(np.nan), 국어(90) 추가

df.at['제임스','영어'] = 100
df.at['제임스','수학'] = np.nan
df.at['제임스','국어'] = 90
df

pd.isnull(df)
df.isnull()

df.sum()
df.sum(axis = 1)
df.mean()
df.mean(skipna = False)
df.mean(axis = 1)
df.mean(axis = 1, skipna = False)

np.mean(df, axis = 1)

df.idxmax()  # 열기준 최고값 인덱스 : 과목별 고득점자
df.idxmin()  # 열기준 최소값 인덱스 : 과목별 저득점자

df.cumsum()  # row단위 누적합
df.cumsum(axis = 1)  # col단위 누적합

df['영어'].sum()
df['영어'].mean()
df['영어'].var()
df['영어'].std()
df['영어'].max()
df['영어'].min()

df.loc['홍길동'].sum()
df.loc['박찬호'].mean()
df.describe()


'''
[문제146] 최고 급여, 최저 급여 출력하세요.
'''
emp  # DataFrame
emp['sal'].max()  # 24000
np.max(emp['sal'])

emp['sal'].min()  # 2100
np.min(emp['sal'])

max(emp['sal'])
min(emp['sal'])


'''
[문제147] 20번 부서 사원들의 급여 합을 구하세요.
'''
emp.loc[emp['d_id']==20,'sal'].sum()  # 19000
np.sum(emp.loc[emp['d_id']==20,'sal'])

sum(emp.loc[emp['d_id']==20,'sal'])

'''
select sum(salary)
from employees
where department_id = 20
'''

'''
[문제148] 부서번호를 입력하면 그 부서의 급여 총액을 구하는 함수를 생성하세요.

dept_sum_sal()

부서번호를 입력하세요 :  20

19000.0


dept_sum_sal()

부서번호를 입력하세요 :  30

24900.0
'''
def dept_sum_sal():
    n = int(input("부서번호를 입력하세요 : "))
    return emp.loc[emp['d_id']==n,'sal'].sum()

dept_sum_sal()


## 12-2. 주의사항 

emp['sal'].sum()  # emp['sal'] : Series -> numpy array
   '''vs''' 
emp[['sal']].sum()  # emp[['sal']] : DataFrame -> Series

type(emp['sal'].sum())
type(emp[['sal']].sum().values[0])  # numpy array


'''
[문제149] 직업을 물어보게하고 직업을 입력하면 해당 직업의 최고 급여를 출력되게하는데 
          아무것도 입력하지 않으면 계속 물어보게하는 프로그램을 작성하세요.

job_max_sal()

직업을 입력하세요 ?  ST_CLERK
3600.0

job_max_sal()

직업을 입력하세요 ? sa_rep
11500.0

job_max_sal()

직업을 입력하세요 ? 

직업을 입력하세요 ? 

직업을 입력하세요 ? 

job_max_sal()

직업을 입력하세요 ? sales
해당 직업의 사원은 없습니다.
'''
# 대문자로 비교 : .upper()
# 미입력시  : while
# 없는 직업(NaN) : exception

def job_max_sal():
    while True:
        job = input("직업을 입력하세요 ? ")
        if job.replace(' ','') == '':
            continue
        else:
            break
    import pandas as pd
    emp = pd.read_csv("c:/python/emp_new.csv",names = ['e_id','name','job','mgr','hd','sal','pct','d_id'])
    try:
        res = emp.loc[emp['job']==job.upper(),'sal'].max()
        if pd.notnull(res):
            return res
        else:
            raise Exception()
    except Exception as error:
        print("해당 직업의 사원은 없습니다.")
    
job_max_sal()



def job_max_sal():
    while True:
        job = input("직업을 입력하세요 ? ")
        if job == '':
            continue
        else:
            break
    import pandas as pd
    emp = pd.read_csv("c:/python/emp_new.csv",names = ['e_id','name','job','mgr','hd','sal','pct','d_id'])
    res = emp.loc[emp['job']==job.upper(),'sal'].max()
    if pd.notnull(res):
        return res
    else:
        print("해당 직업의 사원은 없습니다.")
        return


# 선생님 풀이
import pandas as pd

def job_max_sal():
    try:
        emp = pd.read_csv("c:\python\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
        name = ''
        while name =='':
            name = input('직업을 입력하세요 ? ')
        maxsal = emp['sal'][emp['job'] == name.upper()].max()
        if pd.isnull(maxsal):
            raise
        return maxsal
    except Exception as err:
        print ('해당 직업의 사원은 없습니다.')

job_max_sal()        







