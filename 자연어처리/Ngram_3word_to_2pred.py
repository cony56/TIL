# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:31:37 2020

@author: student
"""


from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.models import Model
from sklearn.model_selection import train_test_split
import nltk
import numpy as np
import string
import random

#File reading

with open('./dataset/alice_in_wonderland.txt','r') as content_file:
    content = content_file.read()

content2 = " ".join("".join([" " if ch in string.punctuation else ch for ch in content]).split())

tokens = nltk.word_tokenize(content2)
tokens = [word.lower() for word in tokens if len(word)>=2]

#Select value of N for N grams among wihch N-1 are used to predict
# last N word

N=5
quads = list(nltk.ngrams(tokens,N))
newl_app = []
for ln in quads:
    newl = " ".join(ln)
    newl_app.append(newl)

newl_app

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()

x_trigm = []
y_trigm = []

for l in newl_app:
    x_str = " ".join(l.split()[0:N-2])
    y_str = " ".join(l.split()[N-2:])
    x_trigm.append(x_str)
    y_trigm.append(y_str)
x_trigm.append(x_str)
y_trigm.append(y_str)

x_trigm_check = vectorizer.fit_transform(x_trigm).todense()
y_trigm_check = vectorizer.fit_transform(y_trigm).todense()

# Dictionaries from word to integer and integer to word
dictnry = vectorizer.vocabulary_
rev_dictnry = {v:k for k,v in dictnry.items()}

X = np.array(x_trigm_check)
Y = np.array(y_trigm_check)

Xtrain, Xtest, Ytrain, Ytest, xtrain_tg, xtest_tg = \
    train_test_split(X,Y,x_trigm, test_size=0.3, random_state=42)

print("X Train shape", Xtrain.shape, "Y Train shape", Ytrain.shape)
print("X Test shape", Xtest.shape, "Y Test shape", Ytest.shape)
# Model_Building

BATCH_SIZE = 128
NUM_EPOCHS = 60

input_layer = Input(shape=(Xtrain.shape[1],),name='input')
first_layer = Dense(1000, activation='relu', name='first')(input_layer)
first_dropout = Dropout(0.5, name='firstdout')(first_layer)
second_layer = Dense(800, activation='relu', name='second')(first_dropout)
third_layer = Dense(1000, activation='relu', name='third')(second_layer)
third_dropout = Dropout(0.5,name='thirdout')(third_layer)
fourth_layer = Dense(Ytrain.shape[1], activation='sigmoid', name='fourth')(third_dropout)

model = Model(input_layer, fourth_layer)
model.compile(optimizer = 'adam', loss = 'binary_crossentropy',metrics=['accuracy'])
print(model.summary())

#Model Training
model.fit(Xtrain, Ytrain, batch_size=BATCH_SIZE, epochs=NUM_EPOCHS, verbose=1,
          validation_split=0.2)

#Model Prediction
Y_pred = model.predict(Xtest)
for i, data in enumerate(Y_pred[0]):
    if data!= 0:
        print(i)
# Sample check on Test data
print("Prior bigram words", "|Actual","Predicted",'\n')
for i in range(10):
    print(i, xtest_tg[i],"|",rev_dictnry[np.argmax(Ytest[i])],"|",rev_dictnry[np.argmax(Y_pred[i])])
NUM_DISPLAY = 10
for i in random.sample(range(len(xtest_tg)), NUM_DISPLAY):
    print(i,xtest_tg[i],"|",
          rev_dictnry[np.argmax(Ytest[i])],"|",
          rev_dictnry[np.argmax(Y_pred[i])])