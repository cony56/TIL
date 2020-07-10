# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 17:29:47 2020

@author: student
"""
import pandas as pd
import numpy as np
from tensorflow.keras.layers import Input, Dense
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
cosine_similarity(dt,yhat)
np.dot(dt,yhat.T)
dt.shape,yhat.shape


