"""
Python-28일차(2018.4.10)
"""

## 28-1. Perceptron 함수
    # 각 논리연산자처럼 결과값이 나올수 있도록 가중치와 임계값을 정의
    
def Perceptron(x1,x2,logic):
    if logic.upper() == 'AND':
        if x1+x2 <= 1:  # w1 = w2 = theta = 1
            return 0
        else:
            return 1
    elif logic.upper() == 'NAND':
        if -x1-x2 <= -2:  # w1 = w2 = -1, theta = -2
            return 0
        else:
            return 1
    elif logic.upper() == 'OR':
        if x1+x2 <= 1/2:  # w1 = w2 = 1, theta = 1/2
            return 0
        else:
            return 1

for i in [0,1]:
    for j in [0,1]:
        print(i,j,Perceptron(i,j,'nand'))


# AND gate
# : 컴퓨터는 두가지의 디지털 값인 0,1을 입력해 하나의 값을 출력하는 회로가 모여 만들어지는데 이 회로를 gate라고 한다.

def AND(x1,x2):
    w1 = 0.7
    w2 = 0.7
    theta = 0.72
    tmp = w1 * x1 + w2 * x2
    if tmp <= theta:
        return 0
    else:
        return 1
# 실행
for i in [0,1]:
    for j in [0,1]:
        print('AND('+str(i)+','+str(j)+') =',AND(i,j))


def NAND(x1,x2):
    w1 = -0.7
    w2 = -0.7
    theta = -0.72
    tmp = w1 * x1 + w2 * x2
    if tmp <= theta:
        return 0
    else:
        return 1
# 실행
for i in [0,1]:
    for j in [0,1]:
        print('NAND('+str(i)+','+str(j)+') =',NAND(i,j))


def OR(x1,x2):
    w1 = 0.7
    w2 = 0.7
    theta = 0.5
    tmp = w1 * x1 + w2 * x2
    if tmp <= theta:
        return 0
    else:
        return 1
# 실행
for i in [0,1]:
    for j in [0,1]:
        print('OR('+str(i)+','+str(j)+') =',OR(i,j))


# 추후에는 가중치, 임계값을 조종한다


## Bias
#  : 퍼셉트론은 입력신호에 가중치를 곱한값과 편향(bias)을 합하여 그 값이 0을 넘으면 1을 출력하고 그렇지 않으면 0을 출력한다.
#    y = wx+b

def AND(x1,x2):
    w1 = 0.7
    w2 = 0.7
    b = -0.72
    tmp = w1 * x1 + w2 * x2 + b
    if tmp <= 0:
        return 0
    else:
        return 1
# 실행
for i in [0,1]:
    for j in [0,1]:
        print('AND('+str(i)+','+str(j)+') =',AND(i,j))


def NAND(x1,x2):
    w1 = -0.7
    w2 = -0.7
    b = 0.72
    tmp = w1 * x1 + w2 * x2 + b
    if tmp <= 0:
        return 0
    else:
        return 1
# 실행
for i in [0,1]:
    for j in [0,1]:
        print('NAND('+str(i)+','+str(j)+') =',NAND(i,j))


def OR(x1,x2):
    w1 = 0.7
    w2 = 0.7
    b = -0.5
    tmp = w1 * x1 + w2 * x2 + b
    if tmp <= 0:
        return 0
    else:
        return 1
# 실행
for i in [0,1]:
    for j in [0,1]:
        print('OR('+str(i)+','+str(j)+') =',OR(i,j))


import numpy as np

x = np.array([0,1])  # input
x

w = np.array([.5,.5])  # weight
w

b = -0.7  # bias

sum(w * x) + b
np.sum(w * x) + b


def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.7,0.7])
    b = -0.72
    tmp = np.sum(w * x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

# 실행  
for i,j in ([0,0],[0,1],[1,0],[1,1]):
    print('AND('+str(i)+','+str(j)+') =',AND(i,j))


def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.7,-0.7])
    b = 0.72
    tmp = np.sum(w * x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

# 실행  
for i,j in ([0,0],[0,1],[1,0],[1,1]):
    print('NAND('+str(i)+','+str(j)+') =',NAND(i,j))


def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.7,0.7])
    b = -0.5
    tmp = np.sum(w * x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

# 실행  
for i,j in ([0,0],[0,1],[1,0],[1,1]):
    print('OR('+str(i)+','+str(j)+') =',OR(i,j))



# XOR : eXclusive OR 배타적논리합
# 같으면 0 다르면 1, 한쪽만 1일때만 1을 출력함

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    return AND(s1,s2)

for i,j in ([0,0],[0,1],[1,0],[1,1]):
    print('XOR('+str(i)+','+str(j)+') =',XOR(i,j))


# 퍼셉트론(단층퍼셉트론)은 직선 하나로 나눈 영역만 표현할 수 있다는 한계가 있다.
#  - 선형 : 직선의 영역을 선형영역
#  - 비선형 : 곡선의 영역을 비선형영역
# 다층퍼셉트론으로 비선형 분류를 할 수 있다.
# XOR 단층 퍼셉트론으로 비선형 분류를 할 수 없다. 해결방법은 XOR = (NAND) AND (OR) 조합으로
# 층을 쌓으면 XOR게이트를 구현할 수 있다.


## Step Function
#  : 임계값을 경계로 출력이 바뀌는 함수, 입력이 0을 넘으면 1 출력 그외에는 0 출력     

def step_func(x):
    if x > 0:
        return 1
    else:
        return 0

step_func(1)
step_func(-1)
step_func(np.array([1.0,2.0]))  # array로 들어온다면 어떻게 넣어서 처리하지?

# [해결방법]
x = np.array([-1.0,1.0,2.0])
y = x > 0

# bool -> int(True -> 1, False -> 0)
y = y.astype(np.int)  # 자료형 변환
y


def step_func(x):  # 이렇게 해결(이게 for문 안 사용하고 작성해서 좋다)
    y = x > 0
    return y.astype(np.int)
step_func(np.array([-1.0,1.0,2.0]))


def step_func(x):
    return np.array(x>0,dtype=np.int)
step_func(np.array([-1.0,1.0,2.0]))

import matplotlib.pylab as plt

x = np.arange(-5.0,5.0,0.1)  # -5.0 ~ 5.0 0.1+
y = step_func(x)

plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()



## Sigmoid Function
#  : 신경망에서는 활성화 함수로 시그모이드 함수를 이용하여 신호를 변환하고 그 변환된 신호를 다음 뉴런에 전달한다.

def sigmoid(x):
    return 1/(1+np.exp(-x))

import math
Pi = math.pi
sigmoid(Pi)
sigmoid(0)


x = np.arange(-5.0,5.0,0.1)
y = sigmoid(x)

plt.grid()
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()


# 정리 
# : 계단함수는 0과 1 중 하나의 값만 전달한다. 
#   시그모이드 함수는 0과 1사이의 실수값으로 전달한다.

# 공통점
# - 시그모이드 함수는 곡선, 계단함수는 계단처럼 구브러진 직선으로
#   동시에 비선형함수로 분류된다.(그래서 신경망에서 사용가능 / 선형함수는 직선하나로 표현한다.)
# - 신경망에서는 활성화함수로 비선형함수를 사용해야 한다.
# - 비선형함수를 사용해야 은닉층을 표현할 수 있다.


## ReLU(Rectified Linear Unit)
#  : 입력이 0을 넘으면 그 입력을 그대로 출력하고 0이하면 0을 출력한다.

x : x > 0
0 : x <= 0


def relu(x):
    return np.maximum(0,x)

relu(2)
relu(0)
relu(-3)


a = np.array([1,2,3,4])
a
np.ndim(a)  # 배열의 차수
a.shape  # 배열의 모양 행(가로) * 열(세로)

b = np.array([[1,2],[3,4],[5,6]])
b
np.ndim(b)
b.shape  # (3,2)


a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

np.dot(a,b)  # 행렬곱


a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2],[3,4],[5,6]])

a.shape
b.shape

np.dot(a,b)
np.dot(b,a)


a = np.array([[1,2],[3,4],[5,6]])
b = np.array([7,8])

a.shape
b.shape

np.dot(a,b)


x = np.array([1.0,0.5])  # 입력층 2개
w1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])  # 가중치
b1 = np.array([0.1,0.2,0.3])  # 편향

# 은닉층 생성
a1 = np.dot(x,w1) + b1
a1  # 3개

# Activation Function
z1 = sigmoid(a1)  
z1

# 다음층으로 넘기는데 은닉층을 생성하고자 한다면
w2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
w2
w2.shape

b2 = np.array([0.1,0.2])
b2

a2 = np.dot(z1,w2) + b2  # 은닉층
a2

# Activation Function
z2 = sigmoid(a2)
z2

# 다음층(출력층)으로 넘기려고 해도 가중치, 편향 계산
w3 = np.array([[0.1,0.3],[0.2,0.4]])
b3 = np.array([0.1,0.2])

a3 = np.dot(z2,w3) + b3
a3


## identity_function : input = output
def identity_function(x):
    return x

y = identity_function(a3)
y


## softmax function : 입력값(최종값)을 받아서 확률값으로 출력

a = np.array([0.3,2.9,4.0])

exp_a = np.exp(a)  # 지수함수
exp_a

sum_exp_a = np.sum(exp_a)  # 지수값의 합
sum_exp_a

# output 
y = exp_a / sum_exp_a  # 지수값/지수값의 합
y

sum(y) # 1
np.sum(y)


def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))

softmax(a)

# 다중분류시 softmax 사용



