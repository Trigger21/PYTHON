#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
python-27일차(2018.4.5)
"""

'''
[문제194] 양의 정수값만 입력 받아서 나누기를 수행하는 positive_divide 함수를 생성하세요.


print(positive_divide())
 
분자 숫자를 입력하세요 : 10
 분모 숫자를 입력하세요 : 2
5.0

print(positive_divide()) 
 
 분자 숫자를 입력하세요 : 10
 분모 숫자를 입력하세요 : -2
오류  - 음수로 나눌수 없습니다. -2


print(positive_divide())

 분자 숫자를 입력하세요 : 10
 분모 숫자를 입력하세요 : 0
오류 -  0으로 나눌수 없습니다. division by zero
'''

def positive_divide():
    num1 = int(input("분자 숫자를 입력하세요 : "))
    num2 = int(input("분모 숫자를 입력하세요 : "))
    try:
        #elif num1 < 0 and num2 > 0:
            #raise Exception("{}".format(num1))
        if num1 > 0 and num2 < 0:
            raise ValueError("{}".format(num2))  
        return num1/num2
    except ValueError as err1:
        print("오류 - 음수로 나눌수 없습니다. {}" .format(err1))
        print("오류 - 음수로 나눌수 없습니다.",num2)
    except ZeroDivisionError as err2:
        print("오류 - 0으로 나눌수 없습니다.",err2)

positive_divide()  # 그냥 Exception 하면 모든 예외사항이 거기로 감


# 선생님 풀이
def  positive_divide():
    try:
      
        x = int(input(' 분자 숫자를 입력하세요 : '))
        y = int(input(' 분모 숫자를 입력하세요 : '))
        
        if(y < 0):  
            raise ValueError
        return  x / y
    except ValueError:
        print('오류  - 음수로 나눌수 없습니다.', y)
    except ZeroDivisionError as error:
        print('오류 -  0으로 나눌수 없습니다.',error)

positive_divide()

# 예외사항 표준화시 클래스로 만듬(plsql spec처럼)
class NegativeDivisionError(Exception): # 예외사항 발생시 초기생성자 생성(Exception->value)
    def __init__(self, value):
        self.value = value
        
def  positive_divide():
    try:
        n = NegativeDivisionError  # 인스터스화
        
        x = int(input(' 분자 숫자를 입력하세요 : '))
        y = int(input(' 분모 숫자를 입력하세요 : '))
        
        if(y < 0):  
            raise n(y)
        return  x / y
    except n as error:
        print('오류  - 음수로 나눌수 없습니다.', error)
    except ZeroDivisionError as error:  # ZeroDivisionError도 사실 class
        print('오류 -  0으로 나눌수 없습니다.', error)

print(positive_divide())


'''pl/sql에서 spec만 만드는 경우 : 
    1. 상수를 처리할 때
    2. exception 이름을 표준화'''

'''딥러닝(텐서플로우) : 2주
   리눅스 하둡 : 2주
   R : 1주'''


'''
[문제195] 성별, 키, 몸무게 데이터프레임 생성한 후  
           키 기준으로 오름차순 정렬해서 출력하세요.
           몸무게 기준으로 정렬할때는 내림차순 결과로 출력하세요.

    gender  height  weight
0      남     170    70.0
1      남     180    80.4
2      여     165    55.5
3      여     150    45.9
4      남     174    70.2
5      여     160    52.6
'''
import pandas as pd
from pandas import DataFrame

df = DataFrame([['남',170,70.0],['남',180,80.4],['여',165,55.5],['여',150,45.9],['남',174,70.2],['여',160,52.6]], columns = ['gender','height','weight'])

df.sort_values('height')  # 키 기준 오름차순  
df.sort_values('weight',ascending = False)  # 몸무게 기준 내림차순


'''
[문제196] knn 프로그램을 작성하세요.
        
      pointlist[(1,1),(1,0),(2,0),(0,1),(2,2),(1,5),(2,3)]
       

        <수행>
        knn([2,1],2,pointlist)

        <결과>
	[(1, 1), (2, 0)]
'''

pow(3,4)
3**2
import math
math.sqrt(2)

pointlist = [(1,1),(1,0),(2,0),(0,1),(2,2),(1,5),(2,3)]

def knn(arg,num,lst):
    dict = {}
    res = []
    
    for i,j in lst:
        d = (arg[0]-i)**2 + (arg[1]-j)**2
        dict[(i,j)] = d
        
    for k,v in sorted(dict.items(), key = lambda x : x[1])[:num]:
        res.append(k)
    return res

knn([2,1],2,pointlist)    
 
   
# 선생님 풀이
import numpy as np
import operator
from math import sqrt

point = [2,1]
k = 2
pointlist=[(1,1),(1,0),(2,0),(0,1),(2,2),(1,5),(2,3)]


def knn(point, lists, k):
    
    dic = {}
    
    for p in lists:
        d = dist(point, p)
        dic[p] = d    
  
    res = []
    sorted_dic = sorted(dic.items(), key = operator.itemgetter(1))  # value를 기준으로 오름차순 정렬    
      
    for key in sorted_dic:
        if len(res) < k: # 갯수 제한           
            res.append(key[0])
            
    return res

# 유클리드 거리 구하는 함수 
def dist(x, y):
    x = np.array(x)
    y = np.array(y)
    
    return  sqrt(sum(pow(x - y,2)))

knn(point,pointlist,k)


'''
[문제197] 

[1.0, 2.0], [1.0, 4.0], [4.0, 1.0], [4.0, 2.0] ])
['추리소설', '추리소설', '경제', '경제']

>>> result = classify([1.0, 2.0], group, labels, 3)
>>> print(result)
추리소설
'''
group = [[1.0, 2.0], [1.0, 4.0], [4.0, 1.0], [4.0, 2.0]]
labels = ['추리소설', '추리소설', '경제', '경제']

from pandas import Series,DataFrame

def classify(test,group,labels,k):
    num = 0
    dic = DataFrame(index = labels,columns = ['거리'])
    res = []
    for i,j in group:
        d = (test[0]-i)**2 + (test[1]-j)**2  # 거리제곱
        dic.loc[labels[num]] = d
        num += 1
    dic = dic.sort_values('거리')
    res = Series(dic[:k].index)
    return res.value_counts(0).index[0]
    
    
classify([1.0, 2.0], group, labels, 3)

# 연철
def classify(dot,group,labels,num):
    x = np.array(dot)
    
    distance = []
    
    for i in group:
        y = np.array(i)
        
        distance.append(sqrt(sum(pow(x - y,2))))
        
    data = {'point' : group,
            'label' : labels,
            'distance' : distance}
    
    data1 = DataFrame(data)
    
    data2 = data1.sort_values(['distance'])[0:num]

    dic = {}
    for i in data2['label']:
        try:
            dic[i] += 1
        except:
            dic[i] = 1
    
    for label, cnt in dic.items():
        if cnt == max(dic.values()):  # 최대빈도수 값에 해당하는 라벨 리턴
            return label

classify([1.0, 2.0], group, labels, 3)

# 상욱형
group = [[1.0, 2.0], [1.0, 4.0], [4.0, 1.0], [4.0, 2.0]]
labels = ['추리소설', '추리소설', '경제', '경제']

def classify(arg1,arg2,arg3,num):
    v = []
    d = {}
    l = []
    t = {}
    for i in arg2:
        v.append(math.sqrt((arg1[0]-i[0])**2+(arg1[1]-i[1])**2))  # 거리 v에 저장
    for i in range(len(v)):
        d[v[i]] = arg2[i]  # key : 거리, value : group
    dic = sorted(d.items(), key=operator.itemgetter(0)) # 거리를 기준으로 dic 오름차순
    print(dic)
    for i in dic:
        l.append(arg3[arg2.index(i[1])]) # 정렬된 dic 원소의 원래 인덱스에 해당하는 라벨 저장
        print(i[1])
    for i in l[:num]: # k개 만큼 제한해서 t에 카운트 값 저장
        if i in t: 
            t[i] += 1
        else:
            t[i] = 1
    dic2 = sorted(t.items(), key=operator.itemgetter(1))  # 카운트 순대로 오름차순 정렬
    return dic2[-1][0]  # 제일 뒤 값(제일 빈도수 높은) 라벨 리턴

classify([1.0, 2.0], group, labels, 3)

# 승혁형
def classify(x, group, labels, k):
    import pandas as pd
    lst=[]
    for i in group:
        lst.append((i[0]-x[0])**2+(i[1]-x[1])**2)
    df=pd.DataFrame({'label':labels, 'distance':lst})
    print(df)
    res=df.sort_values(by='distance', ascending=True)[:k]['label'].value_counts().idxmax() # 빈도수 높은 값의 index
    print(df.sort_values(by='distance', ascending=True)[:k]['label'].value_counts())
    return res

classify([1.0, 2.0], group, labels, 3)   


# 선생님 풀이
import numpy as np
import operator

def createdataset():
    group = np.array([ [1.0, 2.0], [1.0, 4.0], [4.0, 1.0], [4.0, 2.0] ])
    labels = ['추리소설', '추리소설', '경제', '경제']
    return group, labels

# 유클리드 거리를 기준으로 오름차순된 인덱스 리턴하는 함수
def distance(ix, dataset, labels):
    dist = np.sqrt((pow(ix-dataset,2)).sum(axis=1))
    #print(dist)
    sortdist = dist.argsort() # 오름차순한 인덱스 번호를 리턴
    return sortdist

distance([1.0, 2.0], group, labels) # array([0, 1, 3, 2])

# 거리가 근접한 해당 k개 중 빈도값을 기준으로 내림차순 리턴
def findclass(ix, dataset, labels, k, sortdist):
    booklevel = {}

    for i in range(k): # k개 제한
        lab = labels[sortdist[i]] 
        booklevel[lab] = booklevel.get(lab,0) + 1  # get : key에 해당하는 value 값 찾기
        #print(booklevel)
    return sorted(booklevel.items(), key=operator.itemgetter(1), reverse=True)

findclass([1.0, 2.0], group, labels, 3, distance([1.0, 2.0], group, labels)) # [('추리소설', 2), ('경제', 1)]

# 최종 결과
def classify(ix, dataset, labels, k):
    sd = distance(ix, dataset, labels)
    sc = findclass(ix, dataset, labels, k, sd)
    return sc[0][0]  # 빈도수 많은 라벨값 리턴


group, labels = createdataset()
result = classify([1.0, 2.0], group, labels,3)
print(result)
