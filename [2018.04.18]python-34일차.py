#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python-34일차(2018.4.18)
"""

'''
[문제207] bmi.csv 내용을 신경망을 이용해서 분류해 보세요.

#BMI
# BMI = 몸무게 / (키*키)
# 18.5 이상 25미만이면 표준
#label : thin(저체중), normal(정상), fat(비만)
'''

import tensorflow as tf
import numpy as np
from sklearn.preprocessing import MinMaxScaler

tf.reset_default_graph()
tf.set_random_seed(777)

data1=np.genfromtxt('c:/python/bmi.csv',dtype=(str),
                   delimiter=',',skip_header=1,encoding='euc-kr')
data2=np.genfromtxt('c:/python/bmi.csv',dtype=(float),
                   delimiter=',',skip_header=1,encoding='euc-kr')
data1
data2

def logical(x):
    if x=='thin':
        return 0
    elif x=='normal':
        return 1
    else:
        return 2

label=np.array([logical(i) for i in data1[:,2]]).reshape(-1,1)
#label의 'fat','normal','thin'을 숫자화함

traindata=data2[:,:2]
traindata #트레인 데이터 셋을 가져옴


#traindata set을 0~1로 표준화
scaler=MinMaxScaler(feature_range=(0,1))
train = scaler.fit_transform(traindata)
train 



#logistic regression
X=tf.placeholder(tf.float32,[None,2])
Y=tf.placeholder(tf.int32,[None,1])

Y_one_hot = tf.one_hot(Y,3)
Y_one_hot = tf.reshape(Y_one_hot,[-1,3])


# 입력층 Input Layer
W1 = tf.Variable(tf.random_normal([2, 10]), name='weight') 
b1 = tf.Variable(tf.random_normal([10]), name='bias')   
layer1 = tf.nn.relu(tf.matmul(X,W1)+b1)

# 은닉층1 Hidden Layer1
W2 = tf.Variable(tf.random_normal([10,40]), name='weight') 
b2 = tf.Variable(tf.random_normal([40]), name='bias')
#layer2 = tf.nn.relu(tf.matmul(layer1,W2)+b2) # Activation Function ReLu 함수
layer2 = tf.nn.relu(tf.matmul(layer1,W2)+b2) # Activation Function ReLu 함수


# 은닉층2 Hidden Layer2
W3 = tf.Variable(tf.random_normal([40,3]), name='weight') 
b3 = tf.Variable(tf.random_normal([3]), name='bias')
#layer2 = tf.nn.relu(tf.matmul(layer1,W2)+b2) # Activation Function ReLu 함수
layer3 = tf.nn.relu(tf.matmul(layer2,W3)+b3) # Activation Function ReLu 함수


# 출력층 Output Layer
W4 = tf.Variable(tf.random_normal([3,3]), name='weight') 
b4 = tf.Variable(tf.random_normal([3]), name='bias')
logits=tf.matmul(layer3,W4)+b4
hypothesis = tf.nn.softmax(tf.matmul(layer3,W4)+b4) #분류!




cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=Y_one_hot)) 
optimizer = tf.train.AdamOptimizer(learning_rate=0.009).minimize(cost) 

prediction = tf.argmax(hypothesis, 1) 
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1)) 
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32)) 

sess = tf.Session() 
sess.run(tf.global_variables_initializer()) 

for step in range(10001): 
    sess.run(optimizer, feed_dict={X: train, Y: label}) 
    if step % 100 == 0: 
        loss, acc = sess.run([cost, accuracy], feed_dict={X: train, Y: label}) 
        print("Step: {:5}\tLoss: {:.3f}\tAcc: {:.2%}".format(step, loss, acc)) 



# overfitting이 안나려면! 다양한 학습 데이터가 필요하다.
# overshooting은 learning rate값이 좋지 않으면, loss값이 튕겨나간다!





#################선생님 풀이1
        
import pandas as pd
import numpy as np
import tensorflow as tf

bmi = pd.read_csv("c:/python/bmi.csv")

# height 데이터 정규화 
h = bmi["height"]

h_mean = sum(h)/len(h)
h_std_dev = (1/len(h) * sum([ (x_i - h_mean)**2 for x_i in h]))**0.5
h_normalization = [(x_i - h_mean)/h_std_dev for x_i in h]

bmi["height"] = h_normalization 

'''
h_np = np.asarray(bmi["height"])
bmi["height"] = (h_np - h_np.mean()) / h_np.std()
'''



# weight 데이터 정규화

w = bmi["weight"]

w_mean = sum(w)/len(w)
w_std_dev = (1/len(w) * sum([ (i - w_mean)**2 for i in w]))**0.5
w_normalization = [(i - w_mean)/w_std_dev for i in w]

bmi["weight"] = w_normalization

'''
w_np = np.asarray(bmi["weight"])
bmi["weight"]= (w_np - h_np.mean()) / w_np.std()
'''



# 레이블을 배열로 변환하기
# thin=(1,0,0) / normal=(0,1,0) / fat=(0,0,1)
bclass = {"thin": [1,0,0], "normal": [0,1,0], "fat": [0,0,1]}
bmi["label_pat"] = bmi["label"].apply(lambda x : np.array(bclass[x]))
print(len(bmi))

#testdata set만드는 작업
test_csv = bmi[15000:20000] 
test_pat = test_csv[["weight","height"]]
test_ans = list(test_csv["label_pat"])

 
x = tf.placeholder(tf.float32, [None, 2]) 
y = tf.placeholder(tf.float32, [None, 3]) 


w1 = tf.Variable(tf.random_normal([2, 3],seed=0), name='weight1') 
b1 = tf.Variable(tf.random_normal([3],seed=0), name='bias1')


hypothesis = tf.nn.softmax(tf.matmul(x, w1) + b1)


cross_entropy = tf.reduce_mean(-tf.reduce_sum(y * tf.log(hypothesis)))

#train = tf.train.GradientDescentOptimizer(learning_rate=0.00001).minimize(cross_entropy)
train = tf.train.AdamOptimizer(learning_rate=0.01).minimize(cross_entropy) 

predict = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))


sess = tf.Session()
sess.run(tf.global_variables_initializer()) 


for step in range(10001):
    rows = bmi[0:15000]
    x_pat = rows[["weight","height"]]
    y_ans = list(rows["label_pat"])
    fd = {x: x_pat, y: y_ans}
    sess.run(train, feed_dict=fd)
    if step % 1000 == 0:
        cre = sess.run(cross_entropy, feed_dict=fd)
        acc = sess.run(accuracy, feed_dict={x: test_pat, y: test_ans})
        print("step=", step, "cre=", cre, "acc=", acc)


acc = sess.run(accuracy, feed_dict={x: test_pat, y: test_ans})
print("정답률 =", acc)






#################선생님 풀이2
import pandas as pd
import numpy as np
import tensorflow as tf

bmi = pd.read_csv("c:/python/bmi.csv")



# height 데이터 정규화 
h = bmi["height"]

#bmi["height"] = [(i - min(h)) / (max(h) - min(h)) for i in h]

# Min-Max scaling
h_np = np.asarray(h)
bmi["height"] = (h_np - h_np.min()) / (h_np.max() - h_np.min())



# weight 데이터 정규화

w = bmi["weight"]
# bmi["weight"] = [(i - min(w)) / (max(w) - min(w)) for i in w]

w_np = np.asarray(w)
bmi["weight"] = (w_np - h_np.min()) / (w_np.max() - w_np.min())


# 레이블을 배열로 변환하기
# thin=(1,0,0) / normal=(0,1,0) / fat=(0,0,1)
bclass = {"thin": [1,0,0], "normal": [0,1,0], "fat": [0,0,1]}
bmi["label_pat"] = bmi["label"].apply(lambda x : np.array(bclass[x]))
print(len(bmi))


test_csv = bmi[15000:20000]
test_pat = test_csv[["weight","height"]]
test_ans = list(test_csv["label_pat"])

 
x = tf.placeholder(tf.float32, [None, 2]) 
y = tf.placeholder(tf.float32, [None, 3]) 


w1 = tf.Variable(tf.random_normal([2, 3],seed=0), name='weight1') 
b1 = tf.Variable(tf.random_normal([3],seed=0), name='bias1')


hypothesis = tf.nn.softmax(tf.matmul(x, w1) + b1)


cross_entropy = tf.reduce_mean(-tf.reduce_sum(y * tf.log(hypothesis)))

#train = tf.train.GradientDescentOptimizer(learning_rate=0.00001).minimize(cross_entropy)
train = tf.train.AdamOptimizer(learning_rate=0.01).minimize(cross_entropy) 

predict = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))


sess = tf.Session()
sess.run(tf.global_variables_initializer()) 


for step in range(10001):
    rows = bmi[0:15000]
    x_pat = rows[["weight","height"]]
    y_ans = list(rows["label_pat"])
    fd = {x: x_pat, y: y_ans}
    sess.run(train, feed_dict=fd)
    if step % 1000 == 0:
        cre = sess.run(cross_entropy, feed_dict=fd)
        acc = sess.run(accuracy, feed_dict={x: test_pat, y: test_ans})
        print("step=", step, "cre=", cre, "acc=", acc)


acc = sess.run(accuracy, feed_dict={x: test_pat, y: test_ans})
print("정답률 =", acc)
