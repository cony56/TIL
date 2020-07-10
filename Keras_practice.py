# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 16:16:30 2020

@author: student
"""

import numpy as np
import pandas as pd
from tensorflow.keras.layers import Dense, Input, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras import optimizers, regularizers
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import EarlyStopping


data = pd.read_csv('dataset/3-4.credit_data.csv')
data =np.array(data)
data.shape

x = data[:,:6]
y = data[:,-1]
nHid1=6
nHid2=6
nHid3=4
lr=0.01
trainX, testX, trainY, testY = train_test_split(x,y, test_size=0.2) 

InputX = Input(batch_shape=(None, x.shape[1]))
Hid1 = Dense(nHid1, activation='relu',kernel_regularizer=regularizers.l2(0.05))(InputX)
#Hid1 = Dropout(0.01)(Hid1)
Hid2 = Dense(nHid2, activation='relu',kernel_regularizer=regularizers.l2(0.05))(Hid1)
#Hid2 = Dropout(0.01)(Hid2)
#Hid3 = Dense(nHid3, activation='sigmoid')(Hid2)
#Hid3 = Dropout(0.05)(Hid3)
OutputY = Dense(1, activation='sigmoid', \
                kernel_regularizer=regularizers.l2(0.05))(Hid2)
model = Model(InputX,OutputY)
es = EarlyStopping(monitor='val_loss', mode='min', baseline=0.7,\
                   patience=100, verbose=3)
model.compile(loss='binary_crossentropy',\
              optimizer=optimizers.Adam(lr=lr))
hist = model.fit(trainX, trainY, validation_data=\
                 (testX,testY),epochs=500, batch_size=100, callbacks=[es])

yHat = model.predict(testX)
yHat = np.where(yHat>0.5,1,0)
yHat = yHat.reshape(-1)
acc = (testY==yHat).mean()
print('test_accuracy:{}'.format(acc))


fig = plt.figure(figsize=(10, 4))
p1 = fig.add_subplot(1,2,1)
p2 = fig.add_subplot(1,2,2)

p1.plot(hist.history['loss'], label='Train Loss')
p1.plot(hist.history['val_loss'], label='Test Loss')
p1.legend()
p1.set_title("Loss function")
p1.set_xlabel("epoch")
p1.set_ylabel("loss")

n, bins, patches = p2.hist(yHat, 50, facecolor='blue', alpha=0.5)
p2.set_title("yHat distribution")
plt.show()

