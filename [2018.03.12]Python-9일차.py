"""
Python-9일차(2018.3.12)
"""
'''
[문제107] lst 변수에 2,6,1,8,7,9 가 입력 되어 있습니다. 
lst변수를 입력하면 최대값을 리턴 해주는 maxF함수를 생성하세요.
'''
lst = [2,6,1,8,7,9]

# sol.1 : sorted 사용
def maxF(v):
    v1 = sorted(v, reverse = True)
    return v1[0]
maxF(lst)
lst

# sol.2 : 전체비교로 찾기
def maxF(v):
    Max = v[0]
    for i in range(1,len(v)):
        if v[i] > Max:
            Max = v[i]
    return Max
maxF(lst)

# sol.3 : 부분비교후 최종 2개 비교(입력값이 엄청 많을 경우)
def maxF(v):
    n = len(v)
    Max1 = v[0]
    Max2 = v[n//2]
    for i in range(1,n//2):
        if v[i] > Max1:
            Max1 = v[i]
    for j in range(n//2,n):
        if v[j] > Max2:
            Max2 = v[j]
    if Max1 < Max2:
        return Max2
    else:
        return Max1


'''
[문제108] lst 변수에 2,6,1,8,7,9 가 입력 되어 있습니다. 
lst변수를 입력하면 최소값을 리턴 해주는  minF함수를 생성하세요.
'''
lst = [2,6,1,8,7,9]

# sol.1 : sorted 사용
def minF(v):
    v1 = sorted(v, reverse = False)
    return v1[0]
minF(lst)

# sol.2 
def minF(v):
    Min = v[0]
    for i in range(1,len(v)):
        if v[i] < Min:
            Min = v[i]
    return Min
minF(lst)

# sol.3 : 부분비교후 최종 2개 비교(입력값이 엄청 많을 경우)
def maxF(v):
    n = len(v)
    Min1 = v[0]
    Min2 = v[n//2]
    for i in range(1,n//2):
        if v[i] < Min1:
            Min1 = v[i]
    for j in range(n//2,n):
        if v[j] < Min2:
            Min2 = v[j]
    if Min1 < Min2:
        return Min1
    else:
        return Min2
minF(lst)



import random
susu = random.sample(range(1,100000000000), 1000000)

maxF(susu)
minF(susu)
max(susu)
min(susu)


'''
[문제109] 단어, 알파벳을 입력값으로 넣어서 단어 안에 알파벳 수를 출력하세요

<화면예>
wordF('happy','p')
2
'''
def wordF(w,a):
    count = 0
    for i in range(len(w)):
        if w[i] == a:
            count += 1
    return count
wordF('happy','p')


'''
[문제110] 단어를 입력값으로 넣어서 알파벳을 출력하는데 중복되는 알파벳은 하나만 출력하세요.

alphaF('happy')
['h', 'a', 'p', 'y']

alphaF('intelligence')
['i', 'n', 't', 'e', 'l', 'g', 'c']
'''        
def alphaF(w):
    res = []
    for i in range(len(w)):
        x = w[i]
        if not x in res:  # x not in res
            res.append(x)
    return res

alphaF('happy')
alphaF('intelligence')
alphaF('iiiiiiiiiiiiiii')


'''
[문제111] 단어 철자의 빈도수를 출력하세요.

alphaF('intelligence')
{'i': 2, 'n': 2, 't': 1, 'e': 3, 'l': 2, 'g': 1, 'c': 1}

alphaF('happy')
{'h': 1, 'a': 1, 'p': 2, 'y': 1}
'''
def alphaF(w):
    dict = {}
    for i in w:
        if i not in dict:  # dict key에 존재 안 하면
            dict[i] = 1
        else:              # dict key에 존재 하면
            dict[i] += 1
    print(dict)
alphaF('intelligence')
alphaF('happy')



## 9-1. pandas
 - 데이터 분석 기능을 제공하는 라이브러리
 - 1차원 배열 : Series
 - 2차원 배열 : DataFrame

import pandas as pd  # module 축약어 지정(session 상)
from pandas import Series, DataFrame

# Series 
 - 1차원 배열 구조
 - index(색인) 배열의 데이터에 연관된 이름을 가지고 있다

s = Series([10,20,30,40])
s

s.index  # 색인 
s.values  # 값 

s.index = ['a','b','c','d']  # index change / R : rownames()
s

s['a']
s['b']


s2 = Series([10,20,30,40], index = ['a','b','c','d'])  # index 지정하면서 생성
s2

s2['c']  # 30
s2[['a','b']]  # index 2개 이상 보고 싶을 때(리스트 형으로 입력)
s2[0]  # 10

s2[0:3]  # 0~2행까지 슬라이싱
s2[s2 > 20]  # 안에 범위(논리식) 지정가능


'a' in s2  # True
'e' in s2  # False

10 in s2.values  # True


dict = {'a':10,'b':20,'c':30,'d':40}

s3 = Series(dict)  # dict -> Series 변환
s3

s4 = {'a','b','c','d'}  # set
s5 = Series(dict, index = s4)  # index mapping 가능한 데이터만 만들어짐

s4 = {'a','b','c','z'} 
s5 = Series(dict, index = s4)  # z mapping 값이 없으므로 NaN(Not a Number) 저장 
s5

# NaN 찾는 함수는 isnull, notnull (pandas 제공)

pd.isnull(s5)  # s5 안에 NaN이 있으면 True
pd.notnull(s5)  # s5 안에 NaN이 있으면 False


dict = {'서울':3000, '부산':2000, '인천':1000, '제주':500}
s6 = Series(dict)
s6

city = ['서울','대구','인천','제주']
s7 = Series(dict, index = city)
s7

s6.index = ['서울','부산','인천','제주']  # Series index만 바뀜
s6


# DataFrame
 - 2차원 배열
 - 표 같은 스프레드시트 형식의 자료구조
 - 각 컬럼은 서로 다른 종류의 값(숫자, 문자, 불리언)
 - R 언어의 data.frame
 
df1 = DataFrame([[1,2,3],[4,5,6],[7,8,9]])
df1

data = {'도시':['서울','광주','부산','인천'],
        '인구수':[2000,1000,1500,500]}
df2 = DataFrame(data)
df2

df2 = DataFrame({'도시':['서울','광주','부산','인천'],'인구수':[2000,1000,1500,500]})
df2

df3 = DataFrame(data, columns = ['인구수','도시'], index = ['one','two','three','four'])
df3

df3.도시
df3['도시']
df3.인구수
df3['인구수'] * 10  # 연산가능

df3.columns  # colums information
df3.index    # index information

df3.ix['one']  # 특정 row / index 만 보려면 
df3.ix[0]


v = Series([1000,2000,3000,4000], index = ['one','two','three','four'])

df3  # 여기다 cbind 하려면 index 기준(미일치 -> NaN)

df3['부채'] = v  # cbind(df3,v)
df3

del df3['부채']  # column delete
df3


data = {'서울':{2001:200,2002:300},'부산':{2000:10,2001:20,2002:30}}
df4 = DataFrame(data)
df4
'''
Out[221]: 
      부산  서울
2000  10    NaN
2001  20    200.0
2002  30    300.0
'''

df4.T  # 전치행렬(display용, 적용하려면 대입해서 저장)

df4.columns
df4.index 
df4.values 


obj = Series([10,20,30,40], index = ['c','d','a','b'])
obj

# reindex(재색인) : 새로운 색인에 맞도록 객체를 새로 생성하는 기능

obj2 = obj.reindex(['a','b','c','d'])
obj2

obj3 = obj.reindex(['a','b','c','d','f'])
obj3

obj4 = obj.reindex(['a','b','c','d','f'], fill_value = 0)  # fill_value NaN값 값부여
obj4


## 9-2. numpy
 - 데이터 대용량일 때 속도 빠름
 
import numpy as np
np.arange(4)

# ex.1 
df = DataFrame(np.arange(9).reshape(3,3), index = ['a','b','c'], columns = ['x','y','z'])  # 0 ~ 8을 3*3 matrix
df 

df2 = df.reindex(['a','b','c','d'], method = 'ffill')  # NaN 앞의 값으로 채워줌
df2

df2 = df.reindex(['a','b','c','d'], method = 'pad')  # NaN 앞의 값으로 채워줌
df2

df2 = df.reindex(columns = ['y','x','z'])  # column 기준 바뀜
df2


# ex.2
obj = Series(['blue','red','yellow'], index = [0,2,4])
obj

obj2 = obj.reindex(range(6))  # index 기준으로 mapping 없으면 NaN
obj2

obj2 = obj.reindex(range(6), method = 'ffill')  # NaN 앞의 값으로 채워줌
obj2

obj2 = obj.reindex(range(6), method = 'pad')  # NaN 앞의 값으로 채워줌
obj2

obj2 = obj.reindex(range(6), method = 'bfill')  # NaN 뒤의 값으로 채워줌
obj2

obj2 = obj.reindex(range(6), method = 'backill')  # NaN 뒤의 값으로 채워줌
obj2

obj2[5]  # nan

obj2[5] = 'blue'  # 직접입력 가능
obj2


# ex.3 : 행 삭제
obj = Series(np.arange(5), index = ['a','b','c','d','e'])
obj

obj.drop('e')  # index 'e' 값 삭제한 결과 display (실제 적용은 아직)
obj = obj.drop('e')

obj = obj.drop(['c','d'])
obj


# ex.4 : 행 & 열 삭제
df = DataFrame(np.arange(16).reshape(4,4), 
               index = ['w','x','y','z'], 
               columns = ['one','two','three','four'])
df

df2 = df.drop(['x','z'], axis = 0)  # axis = 0 : row(index)
df2

df2 = df.drop(['four'], axis = 1)  # axis = 1 : column
df2

df2 = df.drop(['one','four'], axis = 1)
df2


---------

obj = Series([10,20,30,40], index = ['a','b','c','d'])
obj

obj['a']  # 10
obj[0]

obj[1:3]  # 1~2 
obj['b':'c']  # 'b'~'c' 

obj[['a','c']]  # 'a', 'c'
obj[[0,2]]  # 0, 2

obj[obj < 30]  # 30보다 작은 값만 보여줘


df = DataFrame(np.arange(16).reshape(4,4),
               index = ['w','x','y','z'],
               columns = ['one','two','three','four'])
df

df['one']  # column : 'one'
df[['one','two']]  # column : 'one', 'two'

df[2:]  # index : 2 ~
df[0:2]  # index : 0 ~ 1

df[df['one'] < 5]  # df['one'] 값 중에 5보다 작은 
df[df < 5]  # 해당 안 하면 NaN

df[df < 5] = 0  # 해당 부분에 0 입력(해당값 중 5보다 작은 곳에 0을 넣어라)
df

df.ix['x']
df.ix[1]

df.iloc[1]   # iloc : index num 기준
df.loc['x']  # loc : index name 기준

df.ix['x','one']  # 1행 0열
df.loc['x','one']

df.ix[0,'one']  # 0행 0열
df.iloc[0,1]

