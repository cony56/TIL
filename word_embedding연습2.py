# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 17:15:48 2020

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

L_Input = Input(batch_shape=(None, max_length))
LstmEmbed = Embedding(max_features, 60)(L_Input)
Lstm = Bidirectional(LSTM(64))(LstmEmbed)
L_Flat = Flatten()(Lstm)

C_Input = Input(batch_shape=(None, max_length))
CnnEmbed = Embedding(max_features,60)(C_Input)
Conv = Conv1D(filters=30, kernel_size=8, strides=1, padding = 'valid', activation='relu')(CnnEmbed)
# Pool = GlobalMaxPooling1D(pool_size=4, strides=1, padding='valid')(Conv)
Pool = GlobalMaxPooling1D()(Conv)
C_Flat = Flatten()(Pool)


concat = Concatenate()([C_Flat,L_Flat])
Output = Dense(1, activation='sigmoid')(concat)


model1 = Model([L_Input,C_Input], Output)
model1.compile(loss='binary_crossentropy', optimizer='adam')
print(model1.summary())

hist = model1.fit([x_train, x_train], y_train,
                  batch_size=32,
                  validation_data = ([x_test, x_test], y_test),
                  epochs=1)


# epoch 1 일 때와 epoch 10일 때의 정확도 비교
y_pred = model1.predict([x_test,x_test])
y_pred = np.where(y_pred>0.5,1,0)
model1_acc=accuracy_score(y_test, y_pred)
model1_acc
model1_epoch10=model1_acc.copy()
model1_epoch10





# vocab_dictionary의 단어 수를 비교하려 딕셔너리 단어수가 다른 3개의 데이터를
# 인풋값으로 넣은 lstm 모형들을 넣은 모델을 만들어봤지만 연산속도는 엄청나게 오래 걸리고
# 정확도 개선이 되지 않았음 --> epoch하나 당 20분 걸림

max_f1 = 4000
max_f2 = 8000
max_f3 = 12000
(x_train1, y_train1), (x_test1, y_test1) = imdb.load_data(num_words=max_f1)
(x_train2, y_train2), (x_test2, y_test2) = imdb.load_data(num_words=max_f2)
(x_train3, y_train3), (x_test3, y_test3) = imdb.load_data(num_words=max_f3)
x_train1 = sequence.pad_sequences(x_train, maxlen=max_length)
x_test1 = sequence.pad_sequences(x_test, maxlen=max_length)
x_train2 = sequence.pad_sequences(x_train, maxlen=max_length)
x_test2 = sequence.pad_sequences(x_test, maxlen=max_length)
x_train3 = sequence.pad_sequences(x_train, maxlen=max_length)
x_test3 = sequence.pad_sequences(x_test, maxlen=max_length)

Input1 = Input(batch_shape=(None, max_length))
LstmEmbed1 = Embedding(max_features, 60)(Input1)
Lstm1 = Bidirectional(LSTM(64))(LstmEmbed1)
L_Flat1 = Flatten()(Lstm1)

Input2 = Input(batch_shape=(None, max_length))
LstmEmbed2 = Embedding(max_features, 60)(Input2)
Lstm2 = Bidirectional(LSTM(64))(LstmEmbed2)
L_Flat2 = Flatten()(Lstm2)

Input3 = Input(batch_shape=(None, max_length))
LstmEmbed3 = Embedding(max_features, 60)(Input3)
Lstm3 = Bidirectional(LSTM(64))(LstmEmbed3)
L_Flat3 = Flatten()(Lstm3)

Concat = Concatenate()([L_Flat1, L_Flat2, L_Flat3])
Hid = Dense(750, activation='tanh')(Concat)
Hid = Dropout(0.2)(Hid)
Output2 = Dense(1, activation='sigmoid')(Hid)
Ensemble = Model([Input1,Input2,Input3],Output2)
Ensemble.compile(loss='binary_crossentropy',optimizer='adam')
Ensemble.summary()
hist2 = Ensemble.fit([x_train1, x_train2, x_train3], y_train1,batch_size=32,
                  validation_data = ([x_test1,x_test2,x_test3], y_test1),
                  epochs=3)

y_pred2 = Ensemble.predict([x_test1,x_test2,x_test3])
y_pred2 = np.where(y_pred2>0.5,1,0)
Ensemble_acc=accuracy_score(y_test1, y_pred2)

#confusion matrix 비교

from sklearn.metrics import classification_report, confusion_matrix

confusion_matrix(y_test1, y_pred2)
confusion_matrix(y_test,y_pred)
classification_report(y_test1, y_pred,target_names=['positive','negative'])

confusion_matrix(y_test, y_pred)


#패드, OOV, Start를 추가해 word_index 수정

word2idx = imdb.get_word_index()
idx2word = dict((v,k) for k,v in word2idx.items())
idx2word = dict((v+3,k) for k ,v in word2idx.items())
idx2word[0]='<PAD>'
idx2word[1]='<START>'
idx2word[3] = '<OOV>'

word2idx = dict((k,v) for v,k in idx2word.items())
def decode(review):
	x= [idx2word[s] for s in review]
	return ' '.join(x)
# 워드임베딩 백터에서 단어간 유사도 확인해보기
    
mom = model1.get_weights()[0][word2idx['mother']]
dad = model1.get_weights()[0][word2idx['father']]
cosine_similarity(mom, dad)
