# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 17:29:47 2020

@author: student
"""
import pandas as pd
import numpy as np
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('dataset/creditcard(fraud).csv')
df.shape

dataX=df.iloc[:,1:-1]
dataX = (dataX- dataX.mean()) / dataX.std()
dt=np.array(dataX).astype(np.float32)

nFeature=dt.shape[1]
inputX = Input(batch_shape=(None,nFeature))
Xencode = Dense(12, activation='relu')(inputX)
Xdecode = Dense(nFeature, activation='linear')(Xencode)
model = Model(inputX, Xdecode)
model.compile(loss='mse', optimizer=Adam(lr=0.001))
h = model.fit(dt,dt,epochs=300, batch_size=1000, shuffle=True)
yhat=model.predict(dt)

dist_list=[]
for i in range(len(yhat)):
    dist = cosine_similarity([dt[i]],[yhat[i]])
    dist_list.append(dist)

dist_list2 = dist_list.copy()
maxN=492
max_dict={}
for i in range(maxN):
    max_index = dist_list2.index(max(dist_list2))
    max_value = dist_list2.pop(max_index)
    dist_list2.insert(max_index,0)
    max_dict[max_index]=max_value

actual =set(df[df['Class']==1].index)
predicted = set(max_dict.keys())
print('실제로 비정상인 데이터 수:',len(actual))
print('실제 비정상인데 비정상으로 예측한 데이터 수:',len(actual.intersection(predicted) )
print('precision={}'.format(len(actual.intersection(predicted))/len(actual)) )



"""
Isolation forest의 confusion matrix
confusion matrix :
                 pred_normal  pred_abnormal
actual_normal         283969            346
actual_abnormal          359            133
실제 정상 데이터를 비정상으로 잘못 판정한 비율 = 0.0012
실제 비정상 데이터를 정상으로 잘못 판정한 비율 = 0.7297
accuracy = 0.9975
[[283969    346]
 [   359    133]]
              precision    recall  f1-score   support

         0.0       1.00      1.00      1.00    284315
         1.0       0.28      0.27      0.27       492

    accuracy                           1.00    284807
   macro avg       0.64      0.63      0.64    284807
weighted avg       1.00      1.00      1.00    284807
"""