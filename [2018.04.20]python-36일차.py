#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python-36일차(2018.4.20)
"""

## 20-1. CNN 작동원리 코드

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
%matplotlib inline

sess = tf.InteractiveSession()  # 주거니 받거니 처리(sess.run 안해도 됨), 대화식 처리

image = np.array([[[[1],[2],[3]],
                 [[4],[5],[6]],
                 [[7],[8],[9]]]],dtype = np.float32)

print(image.shape)  # (1,3,3,1) : 1(이미지 갯수), 3(행), 3(열), 1(색,채널) <- 이미지 불러오면 보여지는 양식

# 그래프를 그려보자
plt.imshow(image.reshape(3,3),cmap="Greys")

# filter
weight = tf.constant([[ [[1]], [[1]] ],[ [[1]],[[1]] ]], dtype = tf.float32)
#tf.constant([[ [[1.]], [[1.]] ],[ [[1.]],[[1.]] ]])
weight.shape # (2,2,1,1) : 2 by 2, 색수, 필터수

'''
1 2 3
4 5 6    1  1    -> 12  16
7 8 9    1  1       24  28
'''

#conv2d = tf.nn.conv2d(image, weight, strides=[1,1,1,1], padding = 'VALID')  # VALID : padding 하지마
conv2d = tf.nn.conv2d(image, weight, strides=[1,1,1,1], padding = 'SAME') # SAME : padding 해라

conv2d_img = conv2d.eval()  # InteractiveSession()일 때 tf 변수 사용방법
conv2d_img.shape # 이미지 1, 2 by 2, 색상 1

conv2d_img = np.swapaxes(conv2d_img,0,3) # 전치행렬 변환

for i, one_img in enumerate(conv2d_img): # index, values 다 출력
    print(one_img.reshape(2,2))
    plt.subplot(1,2,i+1),plt.imshow(one_img.reshape(2,2),cmap="Greys")

# 이미지 수집, 이미지 라벨 다는게 제일 힘들다.


image = np.array([[[[4],[3]],
                   [[2],[1]]]], dtype = np.float32)

pool = tf.nn.max_pool(image, ksize = [1,2,2,1], strides = [1,1,1,1], padding = 'VALID')
pool = tf.nn.max_pool(image, ksize = [1,2,2,1], strides = [1,1,1,1], padding = 'SAME')

pool.shape
pool.eval() # 4.


# 30분 안에 이미지 분석

Kaggle MNist Dataset

leaky_relu
epoch


## 20-2. Autoencoder
'''
머신러닝
- 지도 학습(supervised learning) 
  - 프로그램에게 원하는 결과를 알려주는 학습
  - x와 y(label) 둘다 있는 상태
- 비지도 학습 (unsupervised learning)
  - 입력값으로 부터 테이터의 특징을 찾아내는 학습
  - x만 있는 상태에서 학습
  
Autoencoder 
- Unsupervised learning
- 오토인코더는 입력값 출력값을 같게 하는 신경망
- 입력층으로 들어온 데이터를 인코더를 통해 은닉층으로 내보내고 은닉층 데이터를
  디코더를 통해 출력층으로 내보낸뒤 만들어진 출력값을 입력값과 비슷해지도록
  가중치를 찾아낸다.
- 입력값 = 출력값 같게하는 신경망
'''

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

#########
# 옵션 설정
#########
learning_rate = 0.01
training_epoch = 20 # 전체 데이터를 학습할 총횟수
batch_size = 100 # 한번에 학습할 데이터(이미지) 개수

# 신경망 레이어 구성 옵션
n_hidden = 256  # 히든 레이어의 뉴런 갯수
n_input = 28*28   # 입력값 크기 - 이미지 픽셀수 784

##############
# 신경망 모델 구성
##############

X = tf.placeholder(tf.float32, [None, n_input])

# 인코더 레이어와 디코더 레이어의 가중치와 편향 변수를 설정합니다.
# 다음과 같이 이어지는 레이어를 구성하기 위한 값들 입니다.
# input -> encode -> decode -> output
W_encode = tf.Variable(tf.random_normal([n_input, n_hidden]))
b_encode = tf.Variable(tf.random_normal([n_hidden]))
# sigmoid 함수를 이용해 신경망 레이어를 구성합니다.
# sigmoid(X * W + b)
# 인코더 레이어 구성
encoder = tf.nn.sigmoid(
                tf.add(tf.matmul(X, W_encode), b_encode))

# encode 의 아웃풋 크기를 입력값보다 작은 크기로 만들어 정보를 압축하여 특성을 뽑아내고,
# decode 의 출력을 입력값과 동일한 크기를 갖도록하여 입력과 똑같은 아웃풋을 만들어 내도록 합니다.
# 히든 레이어의 구성과 특성치을 뽑아내는 알고리즘을 변경하여 다양한 오토인코더를 만들 수 있습니다.
W_decode = tf.Variable(tf.random_normal([n_hidden, n_input]))
b_decode = tf.Variable(tf.random_normal([n_input]))
# 디코더 레이어 구성
# 이 디코더가 최종 모델이 됩니다.
decoder = tf.nn.sigmoid(
                tf.add(tf.matmul(encoder, W_decode), b_decode))

# 디코더는 인풋과 최대한 같은 결과를 내야 하므로, 디코딩한 결과를 평가하기 위해
# 입력 값인 X 값을 평가를 위한 실측 결과 값으로하여 decoder 와의 차이를 손실값으로 설정합니다.
cost = tf.reduce_mean(tf.pow(X - decoder, 2))
optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(cost) # RMSProp 도 있다

###############
# 신경망 모델 학습
###############
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

total_batch = int(mnist.train.num_examples/batch_size)

for epoch in range(training_epoch):
    total_cost = 0

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        _, cost_val = sess.run([optimizer, cost],
                               feed_dict={X: batch_xs})
        total_cost += cost_val

    print('Epoch:', '%04d' % (epoch + 1),
          'Avg. cost =', '{:.4f}'.format(total_cost / total_batch))

print('최적화 완료!')

#########
# 결과 확인
#########

sample_size = 10

samples = sess.run(decoder,
                   feed_dict={X: mnist.test.images[:sample_size]})

fig, ax = plt.subplots(2, sample_size, figsize=(sample_size, 2))

for i in range(sample_size):
    ax[0][i].set_axis_off()
    ax[1][i].set_axis_off()
    ax[0][i].imshow(np.reshape(mnist.test.images[i], (28, 28)))
    ax[1][i].imshow(np.reshape(samples[i], (28, 28)))

plt.show()

# 사비에르가 무엇인가?
# : 입력층 나에게 오는 갯수를 루트를 씌오고 역수 1/sqrt(n)
# 오버피팅을 방지하는 방법은 데이터셋을 많이 해야지 확률이 높아진다.
                                                                                                                                     








