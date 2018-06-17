#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## http://scikit-learn.org/stable/modules/svm.html#

from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd


tbl = pd.read_csv("/Users/hbk/data/bmi.csv")

label = tbl["label"]
w = tbl["weight"] / 100 # 최대 100kg라고 가정
h = tbl["height"] / 200 # 최대 200cm라고 가정
wh = pd.concat([w, h], axis=1)

# 학습 전용 데이터와 테스트 전용 데이터로 나누기 
data_train, data_test, label_train, label_test = train_test_split(wh, label)

# 데이터 학습하기 
clf = svm.SVC()
clf.fit(data_train, label_train)

# 데이터 예측하기 
predict = clf.predict(data_test)

# 결과 테스트하기 
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("정답률 =", ac_score)
print("리포트 =\n", cl_report)