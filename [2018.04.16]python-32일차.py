#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python-32일차(2018.4.16)
"""

'''
[문제204] (Linear Regression) 학습을 통해서 입력값에 대한 예측값을 출력해주세요.



x1    x2     x3     y
---  ----    ---   ---
73   80      75    152
93   88      93    185
89   91      90    180
96   98     100    196
73   66      70    142



print("당신의 점수는", sess.run(hypothesis, feed_dict={x1: 100, x2: 70, x3: 60}))


당신의 점수는 [ 158.90939331]
'''
import numpy as np
x_data = np.array([[73,80,75],[93,88,93],[89,91,90],[96,98,100],[73,66,70]])
x_data.shape
y_data = np.array([[152],[185],[180],[196],[142]])
y_data.shape

import tensorflow as tf

X = tf.placeholder(tf.float32,shape=(None,3))
Y = tf.placeholder(tf.float32,shape=(None,1))

# 은닉층 & 출력층
w1 = tf.Variable(tf.random_normal([3,1],dtype=tf.float32,seed=0),name='weight1')
b1 = tf.Variable(tf.random_normal([1],dtype=tf.float32,seed=0),name='bias1')
output = tf.matmul(X,w1)+b1

#cost = tf.sqrt(tf.reduce_mean(tf.square(Y-output)))
cost = tf.reduce_mean(tf.square(Y-output))
gradient_descent = tf.train.GradientDescentOptimizer(learning_rate=1e-6).minimize(cost) # 1e-6(1*10^-6)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(100000):
        sess.run(gradient_descent, feed_dict={X:x_data,Y:y_data})
        if step % 1000 == 0:
            print(step,sess.run(cost,feed_dict={X:x_data,Y:y_data}))
    res = sess.run(output, feed_dict = {X:x_data})
    print(res)
    print("당신의 점수는", sess.run(output, feed_dict={X:[[100,70,60]]}))

'''제일 잘 나온거
[[152.12527]
 [184.18591]
 [180.86607]
 [196.4867 ]
 [141.12709]]
당신의 점수는 [[163.13193]]
'''

# 선생님 풀이
import tensorflow as tf

x1_data = [73, 93, 89, 96, 73]
x2_data = [80, 88, 91, 98, 66]
x3_data = [75, 93, 90, 100, 70]

y_data = [152, 185, 180, 196, 142]


x1 = tf.placeholder(tf.float32)
x2 = tf.placeholder(tf.float32)
x3 = tf.placeholder(tf.float32)

Y = tf.placeholder(tf.float32)

w1 = tf.Variable(tf.random_normal([1],seed=0), name='weight1')
w2 = tf.Variable(tf.random_normal([1],seed=0), name='weight2')
w3 = tf.Variable(tf.random_normal([1],seed=0), name='weight3')
b = tf.Variable(tf.random_normal([1],seed=0), name='bias')

hypothesis = x1 * w1 + x2 * w2 + x3 * w3 + b
print(hypothesis)

# Hypothesis = H(x) = Wx + b
# cost(W) = 1/m Σ(H(x) - y)²

cost = tf.reduce_mean(tf.square(hypothesis - Y))


# W := W -α*∂cost(W)/∂W
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000001)
train = optimizer.minimize(cost)


sess = tf.Session()

sess.run(tf.global_variables_initializer())

for step in range(100001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train],
                                   feed_dict={x1: x1_data, x2: x2_data, x3: x3_data, Y: y_data})
    if step % 1000 == 0:
        print(step, cost_val,  hy_val)

print("당신의 점수는", sess.run(hypothesis, feed_dict={x1: 100, x2: 70, x3: 60}))

############################


import tensorflow as tf

x_data = [[73, 80, 75],
          [93, 88, 93],
          [89, 91, 90],
          [96, 98, 100],
          [73, 66, 70]]
y_data = [[152],
          [185],
          [180],
          [196],
          [142]]

x_data

X = tf.placeholder(tf.float32, shape=[None, 3])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([3, 1], seed=0), name='weight')
b = tf.Variable(tf.random_normal([1], seed=0), name='bias')


hypothesis = tf.matmul(X, W) + b


cost = tf.reduce_mean(tf.square(hypothesis - Y))


optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000001)
train = optimizer.minimize(cost)


sess = tf.Session()

sess.run(tf.global_variables_initializer())

for step in range(100001):
    cost_val, hy_val, _ = sess.run(
        [cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
    if step % 10000 == 0:
        print(step,  cost_val,  hy_val)


print("당신의 점수는", sess.run(hypothesis, feed_dict={X:[[100, 70, 60]]}))


'''
[문제205]  XOR  Logistic Regression Classifier Tensorflow을 이용해서  프로그램 생성하세요.
          입력층 - 은닉층1 - 은닉층2 - 출력층
'''
# 예측은는 activation function 필요없지만 분류는 해야한다

# XOR
x_data = [[0,0],
          [0,1],
          [1,0],
          [1,1]]
y_data = [[0],
          [1],
          [1],
          [0]]

import numpy as np
x_data = np.array(x_data, dtype=np.float32)
y_data = np.array(y_data, dtype=np.float32)

import tensorflow as tf

# input
X = tf.placeholder(tf.float32, [None,2])
Y = tf.placeholder(tf.float32, [None,1])

# hidden1
w1 = tf.Variable(tf.random_normal([2,10],dtype='float32',seed=0),name='weight1')
b1 = tf.Variable(tf.random_normal([10],dtype='float32',seed=0),name='bias1')
#layer1 = tf.sigmoid(tf.matmul(X,w1)+b1)
layer1 = tf.maximum(tf.zeros([10]),tf.matmul(X,w1)+b1)

# hidden2
w2 = tf.Variable(tf.random_normal([10,10],dtype='float32',seed=0),name='weight2')
b2 = tf.Variable(tf.random_normal([10],dtype='float32',seed=0),name='bias2')
#layer2 = tf.sigmoid(tf.matmul(layer1,w2)+b2)
layer2 = tf.maximum(tf.zeros([10]),tf.matmul(layer1,w2)+b2)

# output
W = tf.Variable(tf.random_normal([10,1],dtype='float32',seed=0),name='weight')
B = tf.Variable(tf.random_normal([1],dtype='float32',seed=0),name='bias')
hypothesis = tf.sigmoid(tf.matmul(layer2,W)+B)

# cross entropy error function (or lenear function)
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis)) 
gradient_descent = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)
# train = tf.train.AdamOptimizer(learning_rate=0.05).minimize(cost) # 이것도 많이 사용한다고 함

predicted = tf.cast(hypothesis > 0.5, dtype=np.float32) # cast : float -> int (반올림) / bool -> 1(True),0(False)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=np.float32))  # 정확도(예측률)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(8999):
        sess.run(gradient_descent, feed_dict = {X:x_data,Y:y_data})  # 이거 꼭 해야됨
        cost_val = sess.run(cost, feed_dict={X:x_data,Y:y_data})
        if step % 1000 == 0:
            print(step,cost_val,'\n')
    res = sess.run(tf.round(hypothesis), feed_dict = {X:x_data})
    print(res)
    h, c, a  = sess.run([hypothesis, predicted, accuracy],feed_dict={X: x_data, Y: y_data})
    print("\nHypothesis: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)



## Logistic(Binary, sigmoid) Classification

#x0     x1      x2      y
1       2       1       0
1       3       2       0
1       3       4       0
1       5       5       1
1       7       5       1
1       2       5       1


import tensorflow as tf
import numpy as np

xy = np.loadtxt('/Users/hbk/data/train_data.txt', unpack=True, skiprows = 1, dtype='float32')
xy
# skiprows = 1(행수) , unpack : 뒤집는다

x_data = xy[0:-1]
y_data = xy[-1] # label

print ('x', x_data)
print( 'y', y_data)

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_normal([1, 3],seed=0), name='weight') # X 
b = tf.Variable(tf.random_normal([1],seed=0), name='bias') 

hypothesis = tf.sigmoid(tf.matmul(W, X)+b)

cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1-Y) * tf.log(1-hypothesis))

train  = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

print ('Learning')
for step in range(1, 4001):
    sess.run(train, feed_dict={X:x_data, Y:y_data})
    if step % 40 == 0:
        print( step, sess.run(cost, feed_dict={X:x_data, Y:y_data}), sess.run(hypothesis, feed_dict={X:x_data}))
   
print('Answer')
print(sess.run(hypothesis, feed_dict={X:[[1], [2], [2]]}))
print(sess.run(hypothesis, feed_dict={X:[[1], [2], [2]]}) > 0.5)
print(sess.run(tf.cast(sess.run(hypothesis, feed_dict={X:[[1], [5], [5]]}) > 0.5, dtype=tf.int32)))
print(sess.run(hypothesis, feed_dict={X:[[1], [5], [5]]}) > 0.5)
print(sess.run(hypothesis, feed_dict={X:[[1], [8], [3]]}) > 0.5)
print(sess.run(hypothesis, feed_dict={X:[[1,1], [4,3], [3,5]]}) > 0.5)



## http://archive.ics.uci.edu/ml/datasets/zoo (동물분류)

#   1. animal name:     (deleted)
#   2. hair     Boolean"
#   3. feathers     Boolean"
#   4. eggs     Boolean"
#   5. milk     Boolean"
#   6. airborne     Boolean"
#   7. aquatic      Boolean"
#   8. predator     Boolean"
#   9. toothed      Boolean"
#  10. backbone     Boolean"
#  11. breathes     Boolean"
#  12. venomous     Boolean"
#  13. fins     Boolean"
#  14. legs     Numeric (set of values: {0",2,4,5,6,8})
#  15. tail     Boolean"
#  16. domestic     Boolean"
#  17. catsize      Boolean"
#  18. type     Numeric (integer values in range [0",6])
#      0 : 포유류, 1 : 조류, 2 : 파충류, 3 : 어류, 4 : 양서류, 5 : 곤충/거미류, 6 : 무척추동물

import pandas as pd
zoo = pd.read_csv("/Users/hbk/data/data_zoo.csv", header = None, skiprows = 20,
                  names = ['hair','feathers','eggs','milk','airborne','aquatic','predator',
                           'toothed','backbone','breathes','venomous','fins','legs','tail',
                           'domestic','catsize','type'])
zoo

#data = np.genfromtxt('/Users/kimseunghyuck/desktop/data_zoo.csv', delimiter=',', encoding='euc-kr')

len(zoo) # 101 

label = zoo[['type']].values
del zoo['type']
label[:80].shape

train = zoo[:80].values
test1 = zoo[80:90].values
test2 = zoo[90:101].values

type(train)
train.shape # (80,16)

import tensorflow as tf

X = tf.placeholder(tf.float32, [None,16])
Y = tf.placeholder(tf.float32, [None,1])

# hidden1
w1 = tf.Variable(tf.random_normal([16,16],dtype=tf.float32,seed=0),name='weight1')
b1 = tf.Variable(tf.random_normal([16],dtype=tf.float32,seed=0),name='bias1')
layer1 = tf.maximum(tf.zeros([16]),tf.matmul(X,w1)+b1)

# output
W = tf.Variable(tf.random_normal([16,1],dtype=tf.float32,seed=0),name='weight')
B = tf.Variable(tf.random_normal([1],dtype=tf.float32,seed=0),name='bias')
hypothesis = tf.nn.softmax(tf.matmul(layer1,W)+B)

# cross entropy error function
cost = -tf.reduce_mean(Y*tf.log(hypothesis) + (1-Y)*tf.log(1-hypothesis))

# gradient_descent
gradient_descent = tf.train.GradientDescentOptimizer(learning_rate = 0.00001).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for step in range(3000):
        sess.run(gradient_descent, feed_dict = {X:train,Y:label[:80]})
        cost_val = sess.run(cost, feed_dict = {X:train,Y:label[:80]})
        if step % 100 == 0:
            print(step,cost_val)


## Lab 6 Softmax Classifier

import tensorflow as tf
import numpy as np
tf.set_random_seed(777)  # for reproducibility

# Predicting animal type based on various features
#xy = np.loadtxt("/Users/hbk/data/data_zoo.csv", delimiter=',', dtype=np.float32)
#xy = pd.read_csv("/Users/hbk/data/data_zoo.csv", header = None, skiprows = 20).values
xy = np.genfromtxt('/Users/hbk/data/data_zoo.csv', delimiter=',', encoding='euc-kr')
xy
x_data = xy[:,:-1]
x_data
y_data = xy[:, [-1]]
y_data

print(x_data.shape, y_data.shape)

nb_classes = 7  # 0 ~ 6

X = tf.placeholder(tf.float32, [None, 16])
Y = tf.placeholder(tf.int32, [None, 1])  # 0 ~ 6
Y_one_hot = tf.one_hot(Y, nb_classes)  # one hot
print("one_hot", Y_one_hot)
Y_one_hot = tf.reshape(Y_one_hot, [-1, nb_classes]) # -1: None
print("reshape", Y_one_hot)

W = tf.Variable(tf.random_normal([16, nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

# tf.nn.softmax computes softmax activations
# softmax = exp(logits) / reduce_sum(exp(logits), dim)
logits = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logits)

# Cross entropy cost/loss
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits,
                                                 labels=Y_one_hot)
cost = tf.reduce_mean(cost_i)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

prediction = tf.argmax(hypothesis, 1)
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Launch graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(2000):
        sess.run(optimizer, feed_dict={X: x_data, Y: y_data})
        if step % 100 == 0:
            loss, acc = sess.run([cost, accuracy], feed_dict={
                                 X: x_data, Y: y_data})
            print("Step: {:5}\tLoss: {:.3f}\tAcc: {:.2%}".format(
                step, loss, acc))

    # Let's see if we can predict
    pred = sess.run(prediction, feed_dict={X: x_data})
    # y_data: (N,1) = flatten => (N, ) matches pred.shape
    for p, y in zip(pred, y_data.flatten()):
        print("[{}] Prediction: {} True Y: {}".format(p == int(y), p, int(y)))


## One-Hot 개념
        
#x0     x1      x2      y [A B C]
1       2       1          0 0 1
1       3       2          0 0 1
1       3       4          0 0 1
1       5       5          0 1 0
1       7       5          0 1 0
1       2       5          0 1 0
1       6       6          1 0 0
1       7       7          1 0 0

# 위 세가지 분류를 저렇게 만드는게 one-hot-encoding 


## Multi Classification(Softmax Classifier) 
#  : 위의 문제를 푸는 방법의 원리를 탐구하기 위해 쉬운예로 풀이

import tensorflow as tf
import numpy as np

xy = np.loadtxt('c:/data/train.txt', unpack=True, dtype='float32')

x_data = np.transpose(xy[0:3]) # 원하는 모양을 되도록 행열 변환 필수!!
y_data = np.transpose(xy[3:])

print('x', x_data)
print('y', y_data)

X = tf.placeholder("float", [None,3]) # x1, x2 and 1 (for bias)
Y = tf.placeholder("float", [None,3]) # A,B,C (for classes)

W = tf.Variable(tf.zeros([3,3])) # 영행렬로 넣어서 초기화 가능(bias 필수는 아님)


hypothesis = tf.nn.softmax(tf.matmul(X, W))  # Softmax

# Cross-Entropy Cost Function
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), reduction_indices=1)) # 요소별 대응대는 값 구하는 것
# reduction_indices : 0을 전달하면 열 합계, 1을 전달하면 행 합계, 아무 것도 전달하지 않으면 전체 합계
# cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1-Y) * tf.log(1-hypothesis)) : 2가지 분류용(위와 똑같은 방식)


train  = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(cost)


sess = tf.Session()
sess.run(tf.global_variables_initializer())

print('Learning')

for step in range(1, 2001):
    sess.run(train , feed_dict={X:x_data, Y:y_data})
    if step % 40 == 0:
        print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data}), sess.run(W))

print('Answer')
a = sess.run(hypothesis, feed_dict={X:[[1, 11, 7]]})
print(a, sess.run(tf.argmax(a,1))) # 최대값(확률값이 높은) 뽑음 : one_hot 기법

b = sess.run(hypothesis, feed_dict={X:[[1, 3, 4]]})
print(a, sess.run(tf.argmax(b,1)))

c = sess.run(hypothesis, feed_dict={X:[[1, 1, 0]]})
print(a, sess.run(tf.argmax(c,1)))

all = sess.run(hypothesis, feed_dict={X:[[1, 11, 7], [1, 3, 4], [1, 1, 0]]})
print(all, sess.run(tf.argmax(all,1)))


sess.close()


# 숙제 : 유방암 자료를 가지고 신경망으로 분류해보기 (데이터 표준화 또는 정규화도 생각해 보자)