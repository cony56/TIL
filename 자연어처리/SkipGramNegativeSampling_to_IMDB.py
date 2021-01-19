# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:14:23 2020

@author: student
"""


from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Embedding, Bidirectional, LSTM
from tensorflow.keras.layers import Dropout
from tensorflow.keras.datasets import imdb
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
from nltk import pos_tag
from nltk.stem import PorterStemmer
import collections

max_features = 6000
max_length = 400

total_data =imdb.load_data(num_words=max_features)
x_data = total_data[0][0]

word2idx = imdb.get_word_index()
idx2word = dict((v+2,k) for k,v in word2idx.items())
idx2word[0]= 'padding'
idx2word[1]='*start*'
idx2word[2]='OOV'
word2idx = dict((v,k) for k,v in idx2word.items())


def decode(sent_list):
    new_words = []
    for i in sent_list:
        # 0 : padding, 1 : 문서 시작, 2 : OOV로 사용함.
        # 실제 word index에서 3을 빼야함.
        # revind에서 i-3을 조회하고, 없으면 '*'로 채우라는 의미.
        new_words.append(revind.get(i-3, '*'))
    comb_words = " ".join(new_words)
    return comb_words

# 문장의 시작은 항상 '*'로 시작할 것임. 중간에 있는 '*'는 OOV일 것임.
decode(x_train[0])



(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)