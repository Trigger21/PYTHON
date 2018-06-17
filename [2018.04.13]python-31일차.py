#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python-31일차(2018.4.13)
"""

'''
[문제201] x 변수는 1행 3열 모양의 1,2,3을 입력,
        w 변수는 3행 1열 모양의 2,2,2를 입력,
        y 변수는 x와 w를 행렬의 곱을 이용한 결과를 수행하는 프로그램을 작성하세요.
'''
import numpy as np

x = np.array([[1,2,3]])
x
x.shape

w = np.array([[2],[2],[2]])
w
w.shape

y = np.dot(x,w)
y


import tensorflow as tf
x = np.array([[1,2,3]],dtype='int32')
w = np.array([[2],[2],[2]],dtype='int32')

x = tf.constant(x)
x

w = tf.constant(w)
w

y = tf.matmul(x,w) # int64(array 기본값)은 안되네

sess = tf.Session()
sess.run(x)
sess.run(w)
sess.run(y)
sess.close()

with tf.Session() as sess:
    print(sess.run(y))


x = tf.placeholder(dtype=tf.float32,shape=(1,3))
x

w = tf.placeholder(dtype=tf.float32,shape=(3,1))
w

y = tf.matmul(x,w)

with tf.Session() as sess:
    print(sess.run(y, feed_dict={x:[[1,2,3]],w:[[2],[2],[2]]}))


# 선생님 풀이
import tensorflow as tf

x = tf.constant([[1.0, 2.0, 3.0]])
w = tf.constant([[2.0],[2.0],[2.0]])
y = tf.matmul(x,w)

print(x.get_shape())
print(w.get_shape())
sess = tf.Session()
print(sess.run(x))
print(sess.run(w))
print(sess.run(y))
sess.close()


import tensorflow as tf

x = tf.Variable([[1., 2., 3.]])
w = tf.Variable([[2.],[2.],[2.]])
y = tf.matmul(x, w)

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op) # 변수 초기화
    result = sess.run(y)
    print(result)
    



'''
[문제202] (Linear Regression) 학습을 통해서 입력값에 대한 예측값을 출력해주세요.


x(입력)   y(출력)
-------  --------
1	      2
2	      4
3	      6
4	      8
5	      10
6	      12



print(sess.run(hypothesis, feed_dict={X:7}))

[ 13.99977493]


print(sess.run(hypothesis, feed_dict={X:8}))

[ 15.99969196]
'''

import tensorflow as tf
x = tf.constant([1,2,3,4,5,6])
y = tf.constant([2,4,6,8,10,12])



with tf.Session() as sess:
    print(sess.run(x))
















# 선생님 풀이
    
## 31-1. Linear Regression

import tensorflow as tf

x_data = [1, 2, 3, 4, 5, 6]
y_data = [2, 4, 6, 8, 10, 12]


X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_normal([1],seed=0), name='weight') # 정규분포 난수
b = tf.Variable(tf.random_normal([1],seed=0), name='bias')


hypothesis = X * W + b

cost = tf.reduce_mean(tf.square(hypothesis - Y)) # 오차값


optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
train = optimizer.minimize(cost)


sess = tf.Session()
sess.run(W)

sess.run(tf.global_variables_initializer()) # 변수 초기화


for step in range(2001):
    cost_val, W_val, b_val, _ = sess.run([cost, W, b, train],feed_dict={X: x_data, Y: y_data})
    if step % 20 == 0:
        print(step, cost_val, W_val, b_val)



print(sess.run(hypothesis, feed_dict={X:7}), cost_val,W_val,b_val)



'''
x1 공부시간  2     4     6     8
x2 학원수   0     4     2     3
y_data 점수    71    93    91    97
'''
data = [[2,0,71],[4,4,93],[6,2,91],[8,3,97]]

x1 = [i[0] for i in data]
x1

x2 = [i[1] for i in data]
x2

y_data = [i[2] for i in data]
y_data


# y = a1 * x1 + a2 * x2 + b

a1 = tf.Variable(tf.random_uniform([1],0,10,dtype=tf.float64,seed=0))
a2 = tf.Variable(tf.random_uniform([1],0,10,dtype=tf.float64,seed=0))
b = tf.Variable(tf.random_uniform([1],0,100,dtype=tf.float64,seed=0))

y = a1 * x1 + a2 * x2 + b  # y는 예측값

rmse = tf.sqrt(tf.reduce_mean(tf.square(y - y_data)))  # 오차값

learning_rate = 0.1  # 학습률

gradient_descent = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(2000):
        sess.run(gradient_descent)
        w1 = sess.run(a1)
        w2 = sess.run(a2)
        b1 = sess.run(b)
        if step % 100 == 0:
            print(step,sess.run(rmse),sess.run(a1),sess.run(a2),sess.run(b))
          
w1*3+w2*5+b1 # 공부시간 3, 학원 5 인 점수예측


# 추가 연구
data = [[2,0,71],[4,4,93],[6,2,91],[8,3,97]]

x1 = [i[0] for i in data]
x1

x2 = [i[1] for i in data]
x2

y_data = [i[2] for i in data]
y_data


X = tf.placeholder(tf.float32,shape=(2,1))
Y = tf.placeholder(tf.float32)

#w1 = tf.Variable(tf.random_uniform([1],0,10,dtype=tf.float32,seed=0))
#w2 = tf.Variable(tf.random_uniform([1],0,10,dtype=tf.float32,seed=0))
#W = tf.placeholder(tf.float32,shape=(1,2))

W = tf.Variable(tf)

b = tf.Variable(tf.random_uniform([1],0,100,dtype=tf.float32,seed=0))

H = tf.matmul(W,X) + b

rmse = tf.sqrt(tf.reduce_mean(tf.square(H-Y))) 
learning_rate = 0.1
gradient_descent = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(2000):
        sess.run(W,feed_dict={[w1,w2]})
        sess.run(gradient_descent)
        if step % 100 == 0:
            print(step,sess.run(W))
    
    
sess = tf.Session()    
sess.run(W,feed_dict={1,2})    



# logistic regression

'''
공부시간                 2   4   6   7   8   10   12   14
합격(1)/불합격(0)         0   0   0   ?   1   1    1    1
'''
# 시그모이드로 경사하강법 사용시 오차발생시 제곱을 해버리면 안됨(구브러져버림?)
# 그래서 로그를 써야된다고 함


data = [[2,0],[4,0],[6,0],[8,1],[10,1],[12,1],[14,1]]

x_data = [i[0] for i in data] 
x_data

y_data = [i[1] for i in data]
y_data

# 이제 기울기, 절편을 찾아나서자
import tensorflow as tf
a = tf.Variable(tf.random_normal([1],dtype=tf.float64,seed=0))
b = tf.Variable(tf.random_normal([1],dtype=tf.float64,seed=0))

# hypothesis
y = a * x_data + b

# sigmoid function
import numpy as np
y = 1/(1 + np.e**-(a*x_data+b))

# cross entropy error function : 두가지 범위를 구분해서 합해놓은 것
cost = -tf.reduce_mean( np.array(y_data) * tf.log(y) + (1-np.array(y_data)) * tf.log(1-y) )

learning_rate = 0.1
gradient_descent = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(5000):
        sess.run(gradient_descent)
        if step % 100 == 0:
            print(step,sess.run(cost),sess.run(a),sess.run(b))

1/(1+np.exp(-1))
1/(1+np.e**-1)

1/(1+np.exp(-1.55135671*7+10.67100171))



'''
[문제203]  XOR  Logistic Regression Classifier Tensorflow을 이용해서  프로그램 생성하세요.
'''
# XOR : 은닉층이 필요하다
  0 0 0
  0 1 1
  1 0 1
  1 1 0

import numpy as np
x = np.array([[0,0],[0,1],[1,0],[1,1]],dtype=np.float32)
x

y = np.array([[0],[1],[1],[0]],dtype=np.float32)
y



import tensorflow as tf

def step(x):
    if sess.run(x) > 0:
        return 1
    else:
        return 0
    
x = tf.Variable(x)
x

w1 = tf.Variable(tf.random_uniform((2,1),dtype=tf.float32,seed=0))
w1

b = tf.Variable(tf.random_uniform((4,1),dtype=tf.float32,seed=0))
b

h1 = tf.matmul(x,w1) + b
h1
    
y_nand = tf.constant([[1.],[1.],[1.],[0.]])
y_nand
    
cost = -tf.reduce_mean( np.array(y_nand) * tf.log(h1) + (1-np.array(y_nand)) * tf.log(1-h1) )

gradient_descent = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(2000):
        print(sess.run(cost))



x1 = tf.constant([0,1,0,1],dtype=tf.float32)
x2 = tf.constant([0,0,1,1],dtype=tf.float32)

w1 = tf.Variable(tf.random_normal([1],dtype=tf.float32,seed=0))
w2 = tf.Variable(tf.random_normal([1],dtype=tf.float32,seed=0))
b = tf.Variable(tf.random_normal([1],dtype=tf.float32,seed=0))

h1 = w1*x1 + w2*x2 + b
h1 = 1/(1+np.e**-(w1*x1 + w2*x2 + b))

y_nand = tf.constant([1,1,1,0],dtype=tf.float32)
y_nand
    
cost = -tf.reduce_mean( np.array(y_nand) * tf.log(h1) + (1-np.array(y_nand)) * tf.log(1-h1) )

gradient_descent = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

tf.subscribe


# 선생님 풀이
import tensorflow as tf
import numpy as np

tf.set_random_seed(777)  # seed 미리 설정할 수 있다 (seed=0 하는거랑 같다) 


x_data = [[0, 0],
          [0, 1],
          [1, 0],
          [1, 1]]
y_data = [[0],
          [1],
          [1],
          [0]]

x_data = np.array(x_data, dtype=np.float32)
y_data = np.array(y_data, dtype=np.float32)

X = tf.placeholder(tf.float32, [None, 2])  # 열 2개로 고정 
Y = tf.placeholder(tf.float32, [None, 1])  # 열 1개로 고정

W1 = tf.Variable(tf.random_normal([2, 2]), name='weight1')  # 2행(입력값 수) 2열(은닉층 노드수) 행렬구조
b1 = tf.Variable(tf.random_normal([2]), name='bias1')
layer1 = tf.sigmoid(tf.matmul(X, W1) + b1)  # 은닉층1     

W2 = tf.Variable(tf.random_normal([2, 1]), name='weight2')
b2 = tf.Variable(tf.random_normal([1]), name='bias2')
hypothesis = tf.sigmoid(tf.matmul(layer1, W2) + b2) # 출력층


cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))

train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)


with tf.Session() as sess:
    
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        sess.run(train, feed_dict={X: x_data, Y: y_data})
        if step % 1000 == 0:
            print(step, sess.run(cost, feed_dict={X: x_data, Y: y_data}), sess.run([W1, W2]))

  
    h  = sess.run(hypothesis,feed_dict={X: x_data, Y: y_data})
    print("\nHypothesis: ", h)



    