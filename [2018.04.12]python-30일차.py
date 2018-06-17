#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python-30일차(2018.4.12)
"""

# 선생님 왈 : 분석솔루션 회사에서 솔루션 개발팀이 아니라 정제만 하는 업무면 배울게 없는거다 
# learning rate : 너무 작으면 너무 오래걸려 너무 크면 오버됨 
# 모듈식 개발로 해야함


## 30-1. TensorFlow
#  : 구글이 오픈소스로 공개한 머신러닝(machine learning) 라이브러리
#  : 다차원 행렬계산(tensor), 대규모 숫자계산 작업을 수행한다. 
#  : 딥러닝을 비롯한 어러 머신러닝에 사용되는 라이브러리 제공
#  : C++ 로 만들어진 라이브러리(그래서 계산이 빠름)
#  : CPU, GPU 모드로 동작
#  : PYTHON을 지원한다.
# https://www.tensorflow.org
 
import tensorflow as tf

tf.__version__  # version 1.7.0

hello = tf.constant("hello tensorflow")  # constant : tensor 상수
hello # 자료형 정보만 보인다

hello = "hello" # 값이 들어가진다(파이썬 변수처럼 변함) 주의해야함

# 세션 시작
# 클라이언트 프로그램이 텐서플로 런타임 시스템과 통신하기 위해서는 세션이 생성되어야 한다.
sess = tf.Session() 
sess.run(hello) # b : binary 형식이라고 표현
sess.close()


a = tf.constant(1234)
b = tf.constant(5678)

add_op = a + b
add_op

sess = tf.Session()
sess.run(add_op)
sess.run([a,b,add_op])

sess.close()


a = tf.constant(2)
b = tf.constant(3)
c = tf.constant(4)

x1 = a+b+c
x2 = (a+b)*c

sess = tf.Session()
z1 = sess.run(x1)
z2 = sess.run(x2)
z1
z2

sess.close()


a = tf.constant(120,name='a')
b = tf.constant(130,name='b')
c = tf.constant(140,name='c')
v = tf.Variable(0,name = 'v')  # tf 변수

x1 = a+b+c
x1

assign_op = tf.assign(v,x1)
v

sess = tf.Session()

# 이 순서는 오류남
#sess.run(v)
#sess.run(assign_op)

sess.run(tf.global_variables_initializer())
sess.run(x1)
sess.run(v) # 0
sess.run(assign_op) # 390

sess.run(assign_op)
sess.run(v)

sess.run(x1)

sess.close()


x = [[1,2,3],[4,5,6]]  # python var
y = tf.Variable([[1,2],[3,4],[5,6]])  # tf var
x
y

sess = tf.Session()
sess.run(y)

import numpy as np
np.dot(x,sess.run(y))

z1 = tf.Variable(0)
x = [[1,2,3],[4,5,6]]  # python var(2*3)
y = tf.Variable([[1,2],[3,4],[5,6]])  # tf var(3*2)
z = tf.matmul(x,y)

assign_op = tf.assign(z1,z)  # 자료형이 안맞으면 오류남

sess = tf.Session()
sess.run(tf.global_variables_initializer())  # 모든변수 글로벌하게 초기화해야 다음이 수행됨
sess.run(z)
sess.run(z1)

sess.close()


# placeholder : 프로그램 실행중에 값을 넣고 변경할 수 있는 공간

p1 = tf.placeholder("int32") # 아무것도 없는 공간만 선언
p2 = tf.placeholder("int32")


y = tf.add(p1,p2) # +

sess = tf.Session()
sess.run(y,feed_dict={p1:10,p2:20}) # 30


# 함수
'''
tf.add             +
tf.subtract        -
tf.multiply        *
tf.div             /(몫)
tf.truediv         /
tf.mod             /(나머지)
tf.abs             | |
tf.negative        음수
tf.sign            부호(음수: -1, 양수: 1,0)
tf.reciprocal      역수(실수형으로 넣어야 됨)
tf.square          ^2(**2)
tf.round           반올림
tf.sqrt            제곱근(실수형으로 넣어야 됨)
tf.pow             거듭제곱
tf.exp             지수값(실수형으로 넣어야 됨)
tf.log             로그값
tf.maximum         최대값(두가지 값만 비교가능)
tf.minimum         최소값(두가지 값만 비교가능)
tf.cos             코사인(실수형으로 넣어야 됨)
tf.sin             사인(실수형으로 넣어야 됨)
'''

sess = tf.Session()
sess.run(tf.pow(3,2))
sess.run(tf.sign(-4))
sess.run(tf.div(6,4))
sess.run(tf.truediv(6,4))
sess.run(tf.mod(6,4))
sess.run(tf.abs(-5))
sess.run(tf.reciprocal(4.0))
sess.run(tf.square(5))
sess.run(tf.round(5.53))
sess.run(tf.sqrt(2.0))
sess.run(tf.exp(1.0))
sess.run(tf.log(2.7182817))
sess.run(tf.maximum(0,1))
sess.run(tf.minimum(0,1))
sess.run(tf.cos(1.57))
sess.run(tf.sin(np.pi/2))
sess.run(tf.subtract(1,2))

'''
[문제199] tensorflow 상수를 이용해서 아래와 같이 결과를 출력하는 프로그램을 만드세요.

a + b =  6
a * b =  6
'''
import tensorflow as tf

x = tf.constant(3)
y = tf.constant(3)

sess = tf.Session()
#sess.run(tf.global_variables_initializer())
a = sess.run(x)+sess.run(tf.sqrt(3.0))
a
b = sess.run(y)-sess.run(tf.sqrt(3.0))
b

a + b
a * b

sess.close()


x = tf.placeholder('float64')
y = tf.placeholder('float64')
r = tf.sqrt(3.0)

c1 = tf.add(x,y)
c2 = tf.multiply(x,y)

sess=tf.Session()
a = sess.run(x) + sess.run(r)
b = sess.run(y) - sess.run(r)

sess.run(c1,feed_dict={a:3+sess.run(tf.sqrt(3.0)),b:3-sess.run(tf.sqrt(3.0))})

sess.run(tf.sqrt(3.0))



a = tf.constant(2)
b = tf.constant(4)
c = a+b

sess = tf.Session()
sess.run(c)

print("a + b = %d" %sess.run(c))


'''
[문제200] tensorflow 변수를 이용해서 아래와 같이 결과를 출력하는 프로그램을 만드세요. 
단 두 변수의 입력값은 실행시에 넣도록하는 변수를 이용하세요.

Add :  6
Multiply :  8
'''

import tensorflow as tf

a = tf.placeholder(tf.int32)
b = tf.placeholder(tf.int32)

add = tf.add(a,b)
mul = tf.multiply(a,b)

sess= tf.Session()
printAdd = sess.run(add,feed_dict={a:2,b:4})
printMul = sess.run(mul,feed_dict={a:2,b:4})

print("Add : ",printAdd)
print("Multiply : ",printMul)

sess.close()

====================

# 변수성질
x = tf.Variable(0)
y = tf.assign(x,1)

with tf.Session() as sess:  # sess.close() 자동
    sess.run(tf.global_variables_initializer())
    print(sess.run(x))
    print(sess.run(y))
    print(sess.run(x))


x = tf.placeholder("float32") # 실수형 타입
y = tf.placeholder("float32")
z = tf.multiply(x,y)

with tf.Session() as sess:
    print(sess.run(z,feed_dict={x:[3,3],y:[5,5]}))


x = tf.placeholder(tf.float32, shape=(2,2)) # 실수형 타입
y = tf.placeholder(tf.float32, shape=(2,2))
z = tf.multiply(x,y)

with tf.Session() as sess:
    print(sess.run(z,feed_dict={x:[[3.,3.],[3.,3.]], y:[[5.,5.],[5.,5.]]}))


# 텐서는 텐서플로의 기본 자료구조
# 텐서는 다차원배열, 리스트로 구성
# 텐서는 학습데이터가 저장되는 댜차원배열
    
## 30-2. 1차원 텐서(tensor)
    
import numpy as np
import tensorflow as tf

arr_1 = np.array([1.5,1,5.0,10])
arr_1
arr_1[0]
arr_1[:3]

arr_1.ndim # 차원
arr_1.shape # 모양
arr_1.dtype # 원소 자료형

arr_tf = tf.convert_to_tensor(arr_1,dtype=tf.float64)  # numpy array -> tensor로 변환
arr_tf

arr_tf = tf.constant(arr_1)
arr_tf

with tf.Session() as sess:
    print(sess.run(arr_tf))
    print(sess.run(arr_tf[0]))
    print(sess.run(arr_tf[3]))



## 30-3. 2차원 텐서

import numpy as np

arr_2 = np.array([(1,2,3,4),(5,6,7,8),[9,10,11,12],(13,14,15,16)]) # ()로 해도 똑같다
arr_2

arr_2[1,2]
arr_2[1][2]
arr_2[:2,:2]
arr_2[1:3,1:3]

arr_2.dtype  # int64
arr_2.ndim  # 2
arr_2.shape  # 4,4

matrix1 = np.array([(1,1,1),(1,1,1),(1,1,1)], dtype = "int32")
matrix1

matrix2 = np.array([(2,2,2),(2,2,2),(2,2,2)], dtype = "int32")
matrix2

type(matrix1)


tm1 = tf.constant(matrix1)  # 행렬은 바로 tensor 상수가 되는구나
tm1

tm2 = tf.constant(matrix2)
tm2

tm_product = tf.matmul(tm1,tm2) # 행렬곱
tm_add = tf.add(tm1,tm2)

with tf.Session() as sess:
    print(sess.run(tm_product))
    print(sess.run(tm_add))
    
    
## 30-4. 3차원의 텐서

import numpy as np

arr_3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
arr_3

arr_3.ndim
arr_3.shape  # (면,행,열)
    
arr_3[0,0,0] # [plane,row,column]
    
    
tm_3 = tf.constant(arr_3)    

with tf.Session() as sess:
    print(sess.run(tm_3))
    print(sess.run(tm_3)[0,0,0])


'''
공부시간     2     4     6     8
--------------------------------
시험점수     71    83    91    97

4.3 x + 64.0
'''

ab = [4.3,64]
data = [[2,71],[4,83],[6,91],[8,97]]

x = [i[0] for i in data]
y = [i[1] for i in data]
x,y

def predict(x):
    return ab[0]*x + ab[1]

predict(2) # 72.6
predict(4) # 81.2
predict(6) # 89.8
predict(7) # 94.1
predict(8) # 98.4

# 오차들에 대한 합
# 선형회귀 : 임의의 직선을 그어서 이에 대한 평균제곱근오차를 구하고, 이 값을 가장 작게 만들어 주는 기울기와 절편을 찾아가는 작업
# RMSE(Root Mean Squared Error) : 평균제곱근오차
# - 경사하강법시 결과 판단하는 기준으로 해서 기울기와 절편을 찾아가는 방법이다

def rmse(p,a):
    return np.sqrt(((p-a)**2).mean())

def rmse_val(predict_result,y):
    return rmse(np.array(predict_result),np.array(y))

predict_res = []
for i in range(len(x)):
    predict_res.append(predict(x[i]))
    print("공부시간 : %.f, 실제점수 : %.f, 예측점수 : %.f" %(x[i],y[i],predict(x[i])))


predict_result = [predict(i) for i in x]
predict_result

rmse_val(predict_result, y) # 결과 : 1.5165750888103096
print("RMSE :",rmse_val(predict_result, y))    
    
    
# 어떤 직선을 생각해보자
ab = [5,70]
predict_result = [predict(i) for i in x]
print("RMSE :",rmse_val(predict_result, y)) # 9.746794344808963

ab = [4,60]
predict_result = [predict(i) for i in x]
print("RMSE :",rmse_val(predict_result, y)) # 5.744562646538029


==================

# 텐서에서 해보자
import tensorflow as tf
data = [[2,71],[4,83],[6,91],[8,97]]
data = [[2,34],[4,50],[6,57],[8,90]]

x_data = [i[0] for i in data]
y_data = [i[1] for i in data]

# 기울기 a와 절편 b의 값을 임의로 뽑는다
a = tf.Variable(tf.random_uniform([1],0,10,dtype=tf.float64,seed=0)) # 기울기 대략적 범위설정
'''[1],0,10,dtype=tf.float64,seed=0 
- 0~10 사이 숫자 [1]개만 뽑아(실수형)
- seed : 난수값 뽑아낼 경우 달라질 경우 방지(동일하게 나오자)'''

b = tf.Variable(tf.random_uniform([1],0,100,dtype=tf.float64,seed=0)) # 편차 대략적 범위설정

y = a * x_data + b  # 선형직선

rmse = tf.sqrt(tf.reduce_mean(tf.square(y - y_data))) # 평균제곱근오차

learning_rate = 0.1  # 단계범위

# rmse를 최소화 시키는 기울기를 learning_rate 단위로 찾아나서자
gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(100000): # 몇번 학습할지 지정
        sess.run(gradient_decent) # 
        if step % 1000 == 0:
            print('단계',step)
            print('오차',sess.run(rmse))
            print(sess.run(a),sess.run(b))
            

