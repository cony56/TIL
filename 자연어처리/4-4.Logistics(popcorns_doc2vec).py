# Doc2Vec과 Logistic Regression을 이용한 영화리뷰 데이터 분류
# 데이터 : Kaggle의 Bags of Words Meets Bags of Popcorns
# pip install gensim
# ----------------------------------------------------------
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras import preprocessing
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Embedding, Bidirectional, LSTM, Dropout
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
TRAIN_CLEAN_DATA = '4-1.train_clean.csv'
DATA_IN_PATH = './dataset/'

# 전처리가 완료된 학습 데이터를 읽어온다.
train_data = pd.read_csv(DATA_IN_PATH + TRAIN_CLEAN_DATA)
reviews = list(train_data['review'])
sentiments = list(train_data['sentiment'])

sentences = []
for review in reviews:
    sentences.append(review.split())

model_name = '4-1.300features.doc2vec'
model_saved = True

if model_saved:
    model = Doc2Vec.load(DATA_IN_PATH + model_name)
else:
    # gensim 패키지를 이용하여 문장을 vector화 한다 (Doc2Vec)
    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(sentences)]
    model = Doc2Vec(vector_size=300, alpha=0.025, min_alpha=0.00025, 
                    min_count=10, workers=4, dm =1)
    model.build_vocab(documents)
    model.train(documents, total_examples=model.corpus_count, epochs=10)
    model.save(DATA_IN_PATH + model_name)



# model을 확인해 본다.
keys = list(model.wv.vocab.keys())[:20]
print(keys)

# 단어 'stuff'의 vector를 확인한다. 길이 = 300개
model.wv['stuff']

# 단어 유사도를 측정해 본다.
model.wv.similarity("dog", "cat")
model.wv.similarity("dog", "cake")

np.dot(model.wv['dog'], model.wv['cat'])
np.dot(model.wv['dog'], model.wv['cake'])

model.wv.most_similar("dog")

# 첫 번째 문장의 vector (300 개)
model.docvecs[0]

# 새로운 문장의 vector를 추정한다.
new_sentence = model.infer_vector(["system", "response", "cpu", "compute"])

# 학습 데이터와 시험 데이터로 분리한다.
RANDOM_SEED = 42
TEST_SPLIT = 0.2
X = [model.docvecs[i] for i in range(len(sentences))]
y = np.array(sentiments)

X_train, X_eval, y_train, y_eval = train_test_split(X, y, test_size=TEST_SPLIT, 
                                                    random_state=RANDOM_SEED)


# Logistic Regression으로 학습 데이터를 학습한다
lgs = LogisticRegression(class_weight='balanced', solver='newton-cg') 
lgs.fit(X_train, y_train)

# 시험 데이터로 학습 성능을 평가한다
predicted = lgs.predict(X_eval)
print(predicted[:20])
print("Accuracy: %f" % lgs.score(X_eval, y_eval))


# 딥러닝 모델로 doc2vec 분류하기
X_train = np.array(X_train)
X_eval = np.array(X_eval)


Xinput = Input(batch_shape=(None, 300))
Xhid = Dense(500, activation='relu')(Xinput)
Xhid = Dropout(0.2)(Xhid)
Xhid2 = Dense(300, activation='relu')(Xhid)
Xhid2 = Dropout(0.2)(Xhid2)
xOutput = Dense(1, activation='sigmoid')(Xhid2)
model = Model(Xinput, xOutput)
model.compile(loss='binary_crossentropy', optimizer='adam')
hist = model.fit(X_train, y_train, 
                 batch_size=32, 
                 epochs=7,
                 validation_data = (X_eval, y_eval))

yhat = model.predict(X_eval)
y_hat_class = np.round(yhat, 0)
print (("Test accuracy:"),(np.round(accuracy_score(y_eval,y_hat_class),3)))




# Word2 vec 케라스로 해보기


sentences= []

for review in reviews:
    sentences.append(review)


# counter 

sentences
tokenizer = preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(sentences)
sequences = tokenizer.texts_to_sequences(sentences)
word_index = tokenizer.word_index
idx2word = {v:k for (k, v) in word_index.items()}
sequences = np.array(sequences)

max_feature= 74066

x = sequence.pad_sequences(sequences, maxlen = 130, padding='post')
y = np.array(sentiments)

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, 
                                                    random_state=42)

xInput = Input(batch_shape=(None, 130))
xEmbed = Embedding(input_dim=max_feature, output_dim=300,input_length =130)(xInput)
xLstm = Bidirectional(LSTM(64))(xEmbed)
xOutput = Dense(1, activation='sigmoid')(xLstm)
model = Model(xInput, xOutput)
model.compile(loss='binary_crossentropy', optimizer='adam')
model.summary()
# 학습
hist = model.fit(X_train, Y_train, 
                 batch_size=32, 
                 epochs=3,
                 validation_data = (X_test, Y_test))


y_hat = model.predict(x_test, batch_size=32)
y_hat_class = np.round(y_hat, 0)
y_hat_class.shape = y_test.shape

print (("Test accuracy:"),(np.round(accuracy_score(y_test,y_hat_class),3)))




