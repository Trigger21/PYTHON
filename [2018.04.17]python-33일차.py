#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python-33일차(2018.4.17)
"""
# train_new.txt

#x0,x1,x2,y 
1,2,1,0
1,3,2,0
1,3,4,0
1,5,5,1
1,7,5,1
1,2,5,1
1,6,6,2
1,7,7,2

# -> one_hot_encoding   : OMR 카드     
#x0     x1      x2      y [A B C]
1       2       1          0 0 1
1       3       2          0 0 1
1       3       4          0 0 1
1       5       5          0 1 0
1       7       5          0 1 0
1       2       5          0 1 0
1       6       6          1 0 0
1       7       7          1 0 0


## 33-1. Multi_Classification_one_hot_encoding

import tensorflow as tf
import numpy as np

xy = np.loadtxt('c:/data/train_new.txt', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]


X = tf.placeholder(tf.float32, [None,3]) 
Y = tf.placeholder(tf.int32, [None, 1])

Y_one_hot = tf.one_hot(Y, 3)  # one hot 외형 설정
Y_one_hot = tf.reshape(Y_one_hot, [-1, 3]) # -1 : None, 형 설정


W = tf.Variable(tf.random_normal([3, 3]), name='weight')
b = tf.Variable(tf.random_normal([3]), name='bias')


logits = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logits)

## cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis)))
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=Y_one_hot) # 위랑 같은 기능의 메소드
cost = tf.reduce_mean(cost_i) # 확률적인 부분이라서 평균으로 생각해야 한다

train  = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

prediction = tf.argmax(hypothesis, 1)
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    sess.run(train, feed_dict={X: x_data, Y: y_data})
    if step % 100 == 0:
        loss, acc = sess.run([cost, accuracy], feed_dict={X: x_data, Y: y_data})
        print("Step: {:5}\tLoss: {:.3f}\tAcc: {:.2%}".format(step, loss, acc))


====
test
====


a = sess.run(hypothesis, feed_dict={X:[[1,2,1]]})
print(a, sess.run(tf.argmax(a,1))) #ONE-HOT ENCODING

b = sess.run(hypothesis, feed_dict={X:[[1,7,7]]})
print(b, sess.run(tf.argmax(b,1))) #ONE-HOT ENCODING

c = sess.run(hypothesis, feed_dict={X:[[1,4,5]]})
print(c, sess.run(tf.argmax(c,1))) #ONE-HOT ENCODING

all = sess.run(hypothesis, feed_dict={X:[[1,2,1],
 [1,3,2],
 [1,3,4],
 [1,5,5],
 [1,7,5],
 [1,2,5],
 [1,6,6],
 [1,7,7]]})
print(all, sess.run(tf.argmax(all,1)))


'''
[문제206] http://archive.ics.uci.edu/ml/datasets/zoo 
       zoo data set을 이용해서 분류 프로그램을 만드세요.

# http://archive.ics.uci.edu/ml/datasets/zoo
#   1. animal name
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
#      1 : 포유류, 2 : 조류, 3 : 파충류, 4 : 어류, 5 : 양서류, 6 : 곤충/거미류, 7 : 무척추동물
'''

# 선생님 풀이

import tensorflow as tf
import numpy as np 

tf.set_random_seed(777) 

xy = np.loadtxt('/Users/hbk/data/data_zoo.csv', delimiter=',', dtype=np.float32, skip_header = 20)
x_data = xy[0:99, 0:-1]
y_data = xy[0:99, [-1]]


print(x_data.shape, y_data.shape)

X = tf.placeholder(tf.float32, [None, 16])
Y = tf.placeholder(tf.int32, [None, 1])  

Y_one_hot = tf.one_hot(Y, 7)  
Y_one_hot = tf.reshape(Y_one_hot, [-1, 7]) 

W = tf.Variable(tf.random_normal([16, 7]), name='weight')
b = tf.Variable(tf.random_normal([7]), name='bias')

logits = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logits)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=Y_one_hot))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

prediction = tf.argmax(hypothesis, 1)
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    sess.run(optimizer, feed_dict={X: x_data, Y: y_data})
    if step % 100 == 0:
        loss, acc = sess.run([cost, accuracy], feed_dict={ X: x_data, Y: y_data})
        print("Step: {:5}\tLoss: {:.3f}\tAcc: {:.2%}".format( step, loss, acc))


pred = sess.run(prediction, feed_dict={X: x_data})
  
for p, y in zip(pred, y_data.flatten()):
    print("[{}] Prediction: {} True Y: {}".format(p == int(y), p, int(y)))
    


zoo_hypothesis = sess.run(hypothesis, feed_dict={X:xy[99:100, 0:-1]})
print(zoo_hypothesis, sess.run(tf.argmax(zoo_hypothesis,1)))
   
zoo_hypothesis = sess.run(hypothesis, feed_dict={X:xy[100:101, 0:-1]})
print(zoo_hypothesis, sess.run(tf.argmax(zoo_hypothesis,1)))

zoo_hypothesis = sess.run(hypothesis, feed_dict={X:[[0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0]]})
print(zoo_hypothesis, sess.run(tf.argmax(zoo_hypothesis,1)))






















