#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python-29일차(2018.4.11)
"""

'''활성화 함수 : affine sum 다음 뉴런으로 넘기기 위해
 - 출력층 활성화 함수 시그모이드 함수도 사용가능(두가지 분류)
 - 다중분류 softmax'''

# 3층 신경망 모델
import numpy as np 

x = np.array([0.1,0.5])
w1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
b1 = np.array([0.1,0.2,0.3]) 

a1 = np.dot(x,w1) + b1
a1

def relu(x):
    return np.maximum(0,x)

z1 = relu(a1)
w2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
b2 = np.array([0.1,0.2])

a2 = np.dot(z1,w2) + b2
a2

z2 = relu(a2)
w3 = np.array([[0.1,0.3],[0.2,0.4]])
b3 = np.array([0.1,0.2])

a3 = np.dot(z2,w3) + b3
a3

def sigmoid(x):
    return 1/(1+np.exp(-x))

sigmoid(a3)


# 선생님 풀이
import numpy as np

def sigmoid(x):
    return 1 / (1+np.exp(-x))

def identity_function(x):
    return x

def init_network():
    network = {}  # 가중치, 편향값 담을 dict
    network['w1'] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
    network['b1'] = np.array([0.1,0.2,0.3])
    network['w2'] = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network['b2'] = np.array([0.1,0.2])
    network['w3'] = np.array([[0.1,0.3],[0.2,0.4]])
    network['b3'] = np.array([0.1,0.2])
    
    return network

def forward(network,x):
    w1 = network['w1']
    w2 = network['w2']
    w3 = network['w3']
    
    b1 = network['b1']
    b2 = network['b2']
    b3 = network['b3']
    
    a1 = np.dot(x,w1) + b1  # 은닉층1
    z1 = sigmoid(a1)    
    
    a2 = np.dot(z1,w2) + b2  # 은닉층2
    z2 = sigmoid(a2)  
  
    a3 = np.dot(z2,w3) + b3  # 출력층
    y = identity_function(a3) # output layer 
   
    return y


network = init_network()
network

x = np.array([1.0,0.5])
y = forward(network,x)
y


'''
[문제 198]  공부시간에 따른 시험 점수를 예측해주세요.

공부시간     2     4     6     8
--------------------------------
시험점수     71    83    91    97
'''

# 백프라파게이션?? 다시 되돌아가서 가중치, 편향 찾자

# 최소제곱법
t = np.array([2,4,6,8])  # 공부시간
t.mean() # 5.0

g = np.array([71,83,91,97])  # 시험점수
g.mean() $ 95.5

def wb(t,g):
    w = sum( (t-t.mean())*(g-g.mean()) )/sum((t-t.mean())**2)  # weight
    b = g.mean() - w * t.mean()  # bias    
    return w,b

def h(x):
    #w = sum( (t-t.mean())*(g-g.mean()) )/sum((t-t.mean())**2)  # weight
    #b = g.mean() - w * t.mean()  # bias
    w,s = wb(t,g)
    return w * x + b  # 4.3 x + 64.0

h(2)
h(4)
h(6)
h(8)
h(9)
h(10)

np.cov(t,g)/np.var(t)


# 출력값이 원하는 값이 나오도록 weight, bias 


