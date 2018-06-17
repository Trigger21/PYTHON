"""
Python-10일차(2018.3.13)
"""

import pandas as pd
from pandas import Series, DataFrame

student = DataFrame([[60,80,70],[50,75,85],[90,80,85]],
                    index = ['홍길동','박찬호','손흥민'],
                    columns = ['영어','수학','국어'])
student

'''(곧 사라질 set_value)
student = student.set_value('제임스','영어',100)  # 추가(굳이 대입 안해도 됨)
student = student.set_value('제임스','수학',50)   # 추가
student = student.set_value('제임스','국어',80)   # 추가
student
'''

## 10-1. DataFrame에 추가/수정하는 방법

# at : index, column에 직접추가
student.at['제임스','영어'] = 100
student.at['제임스','수학'] = 50
student.at['제임스','국어'] = 80
student

student.ix['제임스','영어'] = 98  # 수정
student.loc['제임스','영어']
student

'''
student = student.set_value('제임스','영어',90)  # 수정
student
'''

# append : DataFrame에 DataFrame을 rbind 시키기 1
student_new = DataFrame([[60,80,70],[50,75,85],[90,80,85]],
                    index = ['윤건','김건모','이문세'],
                    columns = ['영어','수학','국어'])
student_new

student = student.append(student_new)  # student에 student_new 붙이기(R : rbind())
student


# pd.concat : DataFrame에 DataFrame을 rbind 시키기 2
student1 = DataFrame([[60,80,70],[50,75,85],[90,80,85]],
                     index = ['싸이','나얼','윤상'],
                     columns = ['영어','수학','국어'])
student1

student = pd.concat([student,student1])  # student에 student1 붙이기(R : rbind())
student


## row,column 추가/삭제

student['과학'] = [100,80,86,90,95,90,80,70,90,70]  # column 추가
student['한국사'] = '조선'
student

del student['한국사']  # column delete(열은 바로 삭제됨)
student

student = student.drop('제임스')  # row delete display(행은 바로 삭제 안됨)


student['영어']  # column 보기
student[['영어','국어']]
student[0]  # KeyError

student.ix['나얼']
student.ix[7]
student.loc['나얼']
student.iloc[7]

student.ix[0:5] 
student.ix['나얼',['영어','국어']]  # 나얼의 영어,국어 점수 보기
student.ix[['나얼','윤건'],['영어','국어']]  # 나얼,윤건의 영어,국어 점수 보기
student.ix[['나얼','윤건'],[0,2]]  # 나얼,윤건의 영어,국어 점수 보기
student.ix[[3,7],[0,2]]  # index로 출력가능
student.ix[:'윤건']  # 슬라이싱
student.loc[:'윤건'] 

student.index  # indext 목록 
student.columns  # column 목록

student[student.index.isin(['나얼','윤건'])]  # isin : in 기능


student['수학'] > 90  # boolean
student[(student['수학'] > 70) & (student['과학'] > 80)]  # & : and
student[(student['수학'] > 70) | (student['과학'] > 80)]  # | : or

student.loc[student['수학'] > 90]
student.loc[student['국어'] == 85]
student.loc[student['수학'].isin([80,95])]  # isin : in 기능

student.ix[student['과학'] <= 80]
student.ix[student['과학'] <= 80, ['수학','과학']]  # 앞에 조건, 뒤에 컬럼지정
student.ix[student['과학'] <= 80, :'국어']  # 컬럼지정 슬라이싱

student.ix['윤건']
student.xs('윤건')
student.xs('영어',axis = 1)
student['영어']


student.rename(index = {'윤상':'김상'})  # 윤상 -> 김상 으로 index 변경(바로 적용안됨)
student = student.rename(index = {'윤상':'김상'})
student

student = student.rename(columns = {'과학':'물리'})
student


## 연산

obj1 = Series([10,5,3,7], index = ['a','b','c','d'])
obj2 = Series([2,4,6,8,10], index = ['a','b','c','e','f'])

obj1 + obj2  # index 기준으로 덧셈
obj1.add(obj2,fill_value = 0)  # obj1 + obj2, 가상의 값을 부여

obj1 - obj2
obj1.sub(obj2, fill_value = 0)

obj1 * obj2
obj1.mul(obj2, fill_value = 1)

obj1/obj2
obj1.div(obj2, fill_value = 1)

obj1*10


import numpy as np

df1 = DataFrame(np.arange(6).reshape(2,3), 
                index = ['2015','2016'], 
                columns = ['python','sql','plsql'])
df1

df2 = DataFrame(np.arange(12).reshape(3,4),
                index = ['2014','2015','2016'],
                columns = ['python','r','sql','plsql'])
df2

df1 + df2  # index, column 기준으로 덧셈
df1.add(df2, fill_value = 0)
df1.sub(df2, fill_value = 0)
df1.mul(df2, fill_value = 1)
df1.div(df2, fill_value = 1)  # inf : infinite(python : 1/0 되버려서)


obj = np.arange(15).reshape(5,3)  # matrix
obj

obj[0]  # 0번 행
obj1 = obj[0]
obj1

# broadcasting : pandas, numpy에서 작동됨

obj+obj1
obj-obj1

   obj            obj1
0   1   2      0   1   2    
3   4   5      0   1   2
6   7   8      0   1   2
9   10  11     0   1   2
12  13  14     0   1   2


obj1.repeat(5)  # 각 자리 반복(딥러닝에서 무진장 많이 한다고 함)
obj1.repeat(5).reshape(3,5)
obj1.repeat(5).reshape(3,5).T

obj - obj1.repeat(5).reshape(3,5).T

obj2 = obj[:2]
obj2

obj-obj2

## DataFrame ~ Series 연산

# list 내장객체 잘 쓰자
df1 = DataFrame(np.arange(15).reshape(5,3), 
                index = [str(i) for i in range(2012,2017)],
                columns = ['서울','부산','광주'])
df1

s = df1.ix[0]
s
type(s)


df1 + s  # broadcasting

s2 = Series([1,2,3,4], index = ['서울','부산','광주','제주'])
s2

df1 + s2  # DataFrame column ~ Series index 기준으로 연산


df1 = DataFrame(np.arange(15).reshape(5,3), 
                index = [str(i) for i in range(2012,2017)],
                columns = ['서울','부산','광주'])
df1

s3 = Series([0,3,6,9,12], index = [str(i) for i in range(2012,2017)])
s3

df1 + s3
df1.add(s3, axis = 1)

df1.add(s3, axis = 0)  # index(row) 기준  (1 : column 기준)

df1.T + s3


'''
[문제112] 아래와 같은 모양의 표를 생성하세요. 

      PYTHON   R  SQL
2014      60  90   50
2015      80  65   75
2016      70  75   85
'''
ex_112 = DataFrame([[60,90,50],[80,65,75],[70,75,85]],
                   index = ['2014','2015','2016'],
                   columns = ['PYTHON','R','SQL'])
ex_112

# 선생님 풀이
DataFrame({'PYTHON':[60,80,70],'R':[90,65,75],'SQL':[50,75,85]}, index = ['2014','2015','2016'])


'''
[문제113] 'PYTHON' 열을 선택하세요
'''
ex_112.PYTHON
ex_112['PYTHON']


'''
[문제114] '2014' 행 정보를 출력하세요.
'''
ex_112.ix[0]
ex_112.ix['2014']
ex_112.iloc[0]
ex_112.loc['2014']


'''
[문제115] 인덱스번호를 기준으로 1부터 2번까지 출력하세요.
'''
ex_112.ix[1:]
ex_112.iloc[1:]
ex_112.ix['2015':]
ex_112.loc['2015':]


'''
[문제116] PYTHON의 값을 기준으로 60보다 큰값을 가지고 있는 행 정보를 출력하세요.
'''
ex_112[ex_112.PYTHON > 60]
ex_112.ix[ex_112.PYTHON > 60]


'''
[문제117] PYTHON의 값을 기준으로 60 보다 큰값을 가지고 있는 PYTHON 정보만 출력하세요.
'''
ex_112.ix[ex_112.PYTHON > 60, 'PYTHON']
ex_112.loc[ex_112.PYTHON > 60, 'PYTHON']

# 선생님 풀이
ex_112['PYTHON'][ex_112['PYTHON'] > 60]


'''
[문제118] '2015' 행값 중에 PYTHON 정보만 출력하세요
'''
ex_112.ix['2015','PYTHON']  # 80
ex_112.loc['2015','PYTHON']


'''
[문제119] '2015'  행값 중에 PYTHON, R 정보 출력하세요 
'''
ex_112.ix['2015',['PYTHON','R']]
ex_112.loc['2015',['PYTHON','R']]


'''
[문제120] 'R' 열 정보를 출력하세요.
'''
ex_112['R']
ex_112.R
ex_112.xs('R', axis = 1)

# 선생님 풀이
ex_112.ix[:,'R']
ex_112.loc[:,'R']


'''
[문제121] 2013 행을 추가하세요. PYTHON : 70,  SQL : 90, R : 85
'''
# sol.1
ex_112.set_value('2013','PYTHON',70)
ex_112.set_value('2013','SQL',90)
ex_112.set_value('2013','R',85)

# sol.2
ex_121 = DataFrame([[70, 90, 85]], index = ['2013'], columns = ['PYTHON','SQL','R'])
ex_121
ex_112.append(ex_121)

# sol.3
pd.concat([ex_112,ex_121])


# 선생님 풀이 : set_value 만기
ex_112.at['2013','PYTHON'] = 70
ex_112.at['2013','SQL'] = 90
ex_112.at['2013','R'] = 85


'''
[문제122] PLSQL 열을 추가한 후 값은 0로 설정하세요
'''
ex_112['PLSQL'] = 0
ex_112


'''
[문제123] PLSQL 열의 값은 2013 : 50, 2014 : 60, 2015 : 80, 2016 : 90 으로 수정하세요.
'''
ex_112['PLSQL'] = [60,80,90,50]
ex_112

# 선생님 풀이 : set_value 만기
ex_112.at['2013','PLSQL'] = 50
ex_112.at['2014','PLSQL'] = 60
ex_112.at['2015','PLSQL'] = 80
ex_112.at['2016','PLSQL'] = 90
 
'''
[문제124] 2016년도에 있는 정보 출력하세요
'''
ex_112.ix['2016']
ex_112.loc['2016']
ex_112.xs('2016')


'''
[문제125] 2015, 2016년도에  정보 출력하세요.
'''
ex_112.ix[['2015','2016']]
ex_112.loc[['2015','2016']]


'''
[문제126] 2016년도에 PYTHON 정보만 출력하세요.
'''
ex_112.ix['2016','PYTHON']  # 70.0
ex_112.loc['2016','PYTHON']


'''
[문제127] 2016년도에 PYTHON, SQL 정보 출력하세요
'''
ex_112.ix['2016',['PYTHON','SQL']]
ex_112.loc['2016',['PYTHON','SQL']]


'''
[문제128] SQL 점수가 80점보다 이상인 정보를 출력하세요.
'''
ex_112[ex_112.SQL >= 80]
ex_112[ex_112['SQL'] >= 80]


'''
[문제129]PYTHON 점수가 80 이상 또는 SQL 점수가 90 이상인 데이터 출력하세요.
'''
ex_112[(ex_112.PYTHON >= 80) | (ex_112.SQL >= 90)]
ex_112[(ex_112['PYTHON'] >= 80) | (ex_112['SQL'] >= 90)]


'''
[문제130] PYTHON 점수가 80 이상 이고 SQL 점수 90 이상인 데이터 출력하세요.
'''
ex_112[(ex_112.PYTHON >= 80) & (ex_112.SQL >= 90)]  # empty
ex_112[(ex_112['PYTHON'] >= 80) & (ex_112['SQL'] >= 90)]  # empty


'''
[문제131] SQL 점수가 80점 미만인 SQL정보 출력하세요
'''
ex_112.ix[ex_112.SQL < 80, 'SQL']



sorted(ex_112.values, key = lambda data : ex_112.index)
sorted(ex_112.index)


## 정렬

obj = Series([2,3,5,6], index = ['d','c','b','a'])
obj

obj.sort_index()  # index 기준 오름차순
obj.sort_index(ascending = False)  # index 기준 내림차순

obj.sort_values()  # value 기준 오름차순
obj.sort_values(ascending = False)  # value 기준 내림차순


df = DataFrame(np.arange(8).reshape(2,4), 
               index = ['two','one'], 
               columns = ['b','d','a','c'])
df 

df.sort_index()
df.sort_index(ascending = False)
df.sort_index(axis = 1)  # axis = 0 : row, axis = 1 : col
df.sort_index(ascending = False, axis = 1)

df.sort_values(by = 'b', axis = 0, ascending = False)
# b 열의 값을 기준으로 행이 내림차순 정렬

df.sort_values(by = 'one', axis = 1, ascending = False)
# 행의 값을 기준으로 열이 내림차순 정렬

obj1 = Series([4,7,89,87,82,11,15,68,90,90])
obj1.sort_values()

obj1.rank()  # 오름차순 순위(index : 몇 등)

obj1.rank(ascending = False, method = 'average')  # 내림차순 순위(index : 몇 등)
# 기본값 : method = 'average'(같은 값 있을 경우)

obj1.rank(ascending = False, method = 'min') # 같은 순위는 남은 순위 중 최소값
obj1.rank(ascending = False, method = 'max') # 같은 순위는 남은 순위 중 최대값
obj1.rank(ascending = False, method = 'first') # 같은 순위는 index 순으로 순위 나눔
obj1.rank(method = 'first')
obj1.rank(method = 'dense')  # 연이은 정수 순위
obj1.rank(ascending = False, method = 'dense')


df = DataFrame({'영어':[60,80,70],'수학':[50,72,86]},
                index = ['홍길동','박찬호','손흥민'])
df

df.rank()
df.rank(ascending = False)  # 내림차순
df.rank(ascending = False, axis = 1) # 각 행별로 열을 기준으로 점수 비교후 순위
















