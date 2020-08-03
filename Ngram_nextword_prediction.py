# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:50:46 2020

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

N=3
quads = list(nltk.ngrams(tokens,N))
newl_app = []
for ln in quads:
    newl = " ".join(ln)
    newl_app.append(newl)

newl_app

from sklearn.feature_extraction.text import CountVectorizer