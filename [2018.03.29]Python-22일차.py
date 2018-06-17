"""
Python-22일차(2018.3.29)
"""

앞으로 tensorflow 을 통해 신경망 -> 딥러닝(수학&프로그래밍) 공부할 예정
(경사하강법 : 미적분 공부)
tensorflow : 도구
CNN : 눈 (이미지처리)
RNN : 입,귀 (음성처리)


## 22-1. numpy 
''' numerical python 의 약자
 - 고성능 과학 계산 컴퓨팅과 데이터 분석에 필요한 기본 패키지
 - 계산속도가 빠르고 메모리를 효율적으로 사용
 - 벡터 산술연산, 브로드캐스팅(신경망에서 중요함) 기능을 사용하여 다차원 배열을 제공
 - 반복문을 사용할 필요 없이 전체 데이터 배열에 대해서 빠른 연산 제공'''

import numpy as np

# 난수로 정규분포
data = np.random.randn(2,3)  # 2행 3열
data

type(data)  # numpy.ndarray

'''딥러닝은 연구원으로 간다(수학 : 잘해야 함, 영어 : 문서 번역) 논문보는 습관 갖자'''

data.shape  # 행,열
data.dtype  # 원소값 타입
data.ndim  # 행

data*2
data - data
data + data
data / data
data * data

data = [1,2,3,4,5,6]
n = np.array(data)
n

type(data)

n.shape  # (6,)
n.ndim  # 1
n.dtype  # int32

data * 2  # list는 그냥 반복 그래서 for문 또는 내장객체를 사용했었다

n * 2  # R vector처럼 계산됨


data2 = [[1,2,3],[4,5,6]]
n2 = np.array(data2)
n2

np.ones(5)  # 1을 입력값 갯수 만큼 채움
np.ones((3,3))  # 1을 3행 3열로 채움

np.zeros(5)  # 0을 입력값 갯수 만큼 채움
np.zeros((3,3))  # 0을 3행 3열로 채움 
np.zeros((3,2,5))  # 0을 2행 5열 3개로 채움

np.eye(3)  # 단위행렬 Identity Matrix

np.arange(10)  # 0 ~ 9까지 
np.arange(10,20)  # 10 ~ 19까지
np.arange(0,20,5)  # 0 ~ 19까지 5씩 증가


data1 = np.array([[1,2,3],[4,5,6]])
data1

type(data1)
data1.shape  # (2,3)
data1.dtype  # int32


data2 = np.array([[10,20,30],[40,50,60]])
data2


# 스칼라 연산 : 단일값을 기준으로 연산
data1 + data2
data1 - data2
data2 - data1
data1 * data2
data2 / data1
data2 / 5
data1**2


data1 = np.arange(10)
data1

data1[1]  # 인덱싱
data1[0:5]
data1[5] = 50
data1[5:]  # 슬라이싱
data1[:5]


data2 = np.array([[1,2,3],[4,5,6]])

data2[0]
data2[1]
data2[1][2]  # 2행 3열
data2[1,2]  # 2행 3열
data2[1][:2]
data2[1,:2]  # 2행 1~2열
data2[:,1]  # 2열
data2[:,1:]  # 2~3열


data = np.arange(6).reshape(2,3)  # reshape : 축 바꾸기
data

data.T  # 전치행렬


# 행렬의 곱

np.dot(data.T, data) 

data1 = np.arange(24).reshape(2,3,4)  # 2면 3행 4열
data1

data1.transpose(0,2,1)  # 2면 4행 3열로 바뀜
data1.transpose(0,2,1).shape

data1.swapaxes(1,2)  # 1(행), 2(열) 체인지
data1.swapaxes(0,1)


data = np.arange(5)
data


# 제곱근
np.sqrt(data)


# 제곱
data**2
np.square(data)


data1 = np.arange(0,20,2)
data1

data2 = np.arange(0,30,3)
data2

np.add(data1,data2)  # data1 + data2

# 각 배열의 원소 중에 작은값
np.minimum(data1,data2)

# 각 배열의 원소 중에 작은값
np.maximum(data1,data2)


name = np.array(['홍길동','박찬호','손흥민','윤건','홍길동','윤건','나얼','김건모'])

name
type(name)
name.ndim

name == '홍길동'


data = np.arange(24).reshape(8,3)

data
type(data)
data.dtype
data.ndim


data[name=='홍길동']
data[name!='홍길동']


condition = (name == '나얼')|(name == '윤건')
condition

data[condition]

data[data>10]

data[name == '홍길동'] = 0  # 0으로 다 채워짐(R하고 비슷)
data


arr = np.arange(10)
arr

arr.shape
arr.reshape((5,2),order='C')  # 행 우선
arr.reshape((5,2),order='F')  # 열 우선

arr = np.arange(10).reshape((5,2))
arr.ravel('F')  # 열 우선
arr.ravel('C')  # 행 우선

arr.flatten('F')  # 열 우선
arr.flatten('C')


-------

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
arr1
arr2


# 행렬 append
np.concatenate((arr1,arr2),axis=0) # 행기준
np.concatenate((arr1,arr2),axis=1) # 열기준
np.concatenate([arr1,arr2],axis=0) # 행기준
np.concatenate([arr1,arr2],axis=1) # 열기준


np.vstack((arr1,arr2)) # 행기준
np.hstack((arr1,arr2)) # 열기준


# 반복
arr = np.arange(3)
arr
arr.repeat(2)  # 원소별 각각 반복
arr.repeat([2,3,4])  # 0:2번, 1:3번, 2:4번 반복



arr = np.random.randn(2,2)  # 정규분포 난수
arr

arr.repeat(2, axis = 0)  # 행단위 반복
arr.repeat(2, axis = 1)  # 열단위 반복
arr.repeat([2,3], axis = 1) # 열단위 각각 2번, 3번 반복


np.tile(arr,2) # 통채로 반복

a = np.array([[1,2],[3,4]])
a

np.sum(a)
np.sum(a,axis=0) # rowSum
np.sum(a,axis=1) # colSum

np.mean(a)
np.mean(a,axis=0) # rowMean
np.mean(a,axis=1) # colMean

np.var(a)
np.std(a)

np.cumsum(a)  # 누적합
np.cumsum(a,axis=0)  # 누적 rowSum
np.cumsum(a,axis=1)  # 누적 colSum


np.prod(a)  # 곱셈
np.prod(a,axis=0)  # rowProd
np.prod(a,axis=1)  # colProd


# broadcasting
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
y = np.array([1,0,1])
z = np.empty_like(x)  # x와 동일한 shape를 가진 행렬을 생성(1행 1열은 난수)
z = np.zeros((4,3))  # 모두다 0으로 바뀜
x
y
z

x + y

z = x + y
z

for i in range(4):
    z[i,:] = x[i,:] + y  # broadcasting 원리 1
z

x + np.tile(y,4).reshape(4,3)  # broadcasting 원리 2


x = np.array([3,3,3,2,2,1,1,4,4,4,5,5,5,5,1,8,1,8])
x

np.unique(x)  # 중복값 제거 정렬

set(x)


x = np.array([1,2,3,4,5,6])
np.in1d(x,[2,3,4])  # 일치여부 boolean으로 보여줌

np.intersect1d([1,3,4,3],[3,1,2,1])  # 교집합

np.setdiff1d([1,3,4,3],[3,1,2,1])  # 차집합

x = np.array([[1,2,3],[4,5,6]])
y = np.array([[2,3,5],[7,8,6]])

np.setdiff1d(x,y)  # 차집합
np.intersect1d(x,y)  # 교집합
np.union1d(x,y)  # 합집합


x = np.array([5,2,4,3,1])
sorted(x)
sorted(x, reverse = True)
ix = x.argsort()  # 정렬시 인덱스 
ix

x[ix]


x = np.random.randn(3,4)
sorted(x, key = lambda x : x)

x[:,x[0].argsort()]  # 1행만 정렬시키려고 열에 대한 정렬실시

