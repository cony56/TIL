# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:31:12 2020

@author: student
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import scipy
import math
import pandas as pd
import numpy as np
import collections
from gensim.models import word2vec
from tensorflow.keras import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from tqdm.notebook import tqdm
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Embedding, Bidirectional, LSTM, Dropout
from tensorflow.keras.layers import concatenate
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
TRAIN_CLEAN_DATA = '4-1.train_clean.csv'
DATA_IN_PATH = './dataset/'

# 전처리가 완료된 학습 데이터를 읽어온다.
train_data = pd.read_csv(DATA_IN_PATH + TRAIN_CLEAN_DATA)
reviews = list(train_data['review'])
sentiments = list(train_data['sentiment'])

sentences= []

for review in reviews:
    sentences.append(review)

sentences
tokenizer = preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(sentences)
sequences = tokenizer.texts_to_sequences(sentences)
word_index = tokenizer.word_index
idx2word = {v:k for (k, v) in word_index.items()}

len(word_index.keys())

sentences

total_dict = collections.Counter()
pos_dict = collections.Counter()
neg_dict = collections.Counter()
for i , sentence in enumerate(sentences):
    words = set(sentence.split())
    for word in words:
        total_dict[word]+=1
        if sentiments[i]==0:
            neg_dict[word]+=1
        else:
            pos_dict[word]+=1
pos_dict.most_common(100)
neg_dict.most_common(100)
little=0.0000000000000000001
real_dict={}
for word in total_dict.keys():
    real_dict[word]= (pos_dict[word]/25000)*math.log(2*(pos_dict[word]+little)/total_dict[word])+\
        (neg_dict[word]/25000)*math.log(2*(little+neg_dict[word])/total_dict[word])

dict_common = sorted(real_dict.items(), reverse=True, key= lambda x: x[1])

dic_num = round(len(dict_common)/2)
new_dict = [x[0] for x in dict_common[:dic_num]]

new_dict1 = {v:i for i,v in enumerate(new_dict)}


new_sentences=[]
for sentence in sentences:
    new_sent = []
    sent = ''
    for word in sentence:
        try:
            new_dict1[word]
            wd = word
        except:
            wd = ' '
        sent+=wd
        new_sent.append(sent)
    new_sentences.append("".join(new_sent))
            
# 모델링------------------------------------------------------------------

tokenizer = preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(new_dict1)
new_wordidx = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(sentences)
sequences = np.array(sequences)


max_feature= 37032+1
# Embedding layer
x = sequence.pad_sequences(sequences, maxlen = 130, padding='post')
y = np.array(sentiments)

#TF-IDF 벡터

vectorizer = TfidfVectorizer(min_df = 0.0, analyzer="word", sublinear_tf=True, 
                             ngram_range=(1,2), max_features=1000) 
x2 = vectorizer.fit_transform(new_sentences)

X1_train, X1_test, Y_train, Y_test = train_test_split(x2, y , test_size=0.3, random_state=42)

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, 
                                                    random_state=42)

X1_train.sort_indices()
X1_test.sort_indices()
#최종 모델링
xInput = Input(batch_shape=(None, 130))
xEmbed = Embedding(input_dim=max_feature, output_dim=300,input_length =130)(xInput)
xLstm = Bidirectional(LSTM(64))(xEmbed)
xLstm = Dropout(0.3)(xLstm)

x2Input = Input(batch_shape=(None, 1000))
Concat = concatenate([xLstm,x2Input])
Xhid2 = Dense(200, activation='relu')(Concat)
Xhid2 = Dropout(0.3)(Xhid2)
xOutput = Dense(1, activation='sigmoid')(Concat)
model = Model([xInput,x2Input], xOutput)
model.compile(loss='binary_crossentropy', optimizer='Adam' )
model.summary()
# 학습
hist = model.fit([X_train,X1_train], Y_train, 
                 batch_size=600, 
                 epochs=4, validation_data=([X_test,X1_test],Y_test))


y_hat = model.predict([X_test,X1_test], batch_size=32)
y_hat_class = np.round(y_hat, 0)
y_hat_class.shape = Y_test.shape

print (("Test accuracy:"),(np.round(accuracy_score(Y_test,y_hat_class),3)))
# 0.895
# Epoch 1/5
# 35/35 [==============================] - 46s 1s/step - loss: 0.6141 - val_loss: 0.4604
# Epoch 2/5
# 35/35 [==============================] - 49s 1s/step - loss: 0.3139 - val_loss: 0.2885
# Epoch 3/5
# 35/35 [==============================] - 53s 2s/step - loss: 0.1894 - val_loss: 0.2671
# Epoch 4/5
# 35/35 [==============================] - 54s 2s/step - loss: 0.1252 - val_loss: 0.2856
# Epoch 5/5
# 35/35 [==============================] - 54s 2s/step - loss: 0.0810 - val_loss: 0.3341
# Test accuracy: 0.892
#---------------------------------------------------------------------------

x2.shape



# Doc2 vec

# documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(new_sentences)]
# model = Doc2Vec(vector_size=300, alpha=0.025, min_alpha=0.00025, 
#                 min_count=10, workers=4, dm =1)
# model.build_vocab(documents)
# model.train(documents, total_examples=model.corpus_count, epochs=10)

# RANDOM_SEED = 42
# TEST_SPLIT = 0.2
# X = [model.docvecs[i] for i in range(len(sentences))]
# y = np.array(sentiments)

# X_train, X_eval, y_train, y_eval = train_test_split(X, y, test_size=TEST_SPLIT, 
#                                                     random_state=RANDOM_SEED)


# # Logistic Regression으로 학습 데이터를 학습한다
# lgs = LogisticRegression(class_weight='balanced', solver='newton-cg') 
# lgs.fit(X_train, y_train)

# # 시험 데이터로 학습 성능을 평가한다
# predicted = lgs.predict(X_eval)
# print(predicted[:20])
# print("Accuracy: %f" % lgs.score(X_eval, y_eval))









