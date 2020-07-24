# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:11:03 2020

@author: student
"""


from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Embedding, Concatenate
from tensorflow.keras.layers import Conv1D, GlobalMaxPooling1D
from tensorflow.keras.datasets import imdb
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.layers import Input, Dense, Embedding, Bidirectional, LSTM

max_features = 6000
max_length = 400

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

x_train = sequence.pad_sequences(x_train, maxlen=max_length)
x_test = sequence.pad_sequences(x_test, maxlen=max_length)

x_Input = Input(batch_shape=(None, max_length))
LstmEmbed = Embedding(max_features, 60)(x_Input)
Lstm = Bidirectional(LSTM(64))(LstmEmbed)
L_Flat = Flatten()(Lstm)

CnnEmbed = Embedding(max_features,60,input_length = max_length)(x_Input)
Conv = Conv1D(filters=260, kernel_size=3, strides=1, padding = 'same', activation='relu')(CnnEmbed)
Pool = GlobalMaxPooling1D()(Conv)
C_Flat = Flatten()(Pool)
concat = Concatenate()([Lstm,C_Flat])
Output = Dense(1, activation='sigmoid')(concat)
model1 = Model(x_Input, Output )
model1.compile(loss = 'binary_crossentropy', optimizer='adam')
hist = model1.fit(x_train, y_train, 
                 batch_size=32, 
                 epochs=1,
                 validation_data = (x_test, y_test))



xPool = MaxPooling1D(pool_size=4, strides=1, padding='valid')(xConv)
xFlat = Flatten()(xPool)
xInput = Input(batch_shape = (None, nStep, nFeature))
#filter 30개 kenelsize=8개, 
Conv = Conv1D(filters=30, kernel_size=8, strides=1, padding = 'valid', activation='relu')(xInput)

xOutput = Dense(1, activation='linear')(xFlat)


xOutput = Dense(1, activation='sigmoid')(xLstm)
model = Model(xInput, xOutput)
model.compile(loss='binary_crossentropy', optimizer='adam')
model.summary()
