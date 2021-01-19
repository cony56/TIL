# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:20:38 2020

@author: student
"""


import nltk
import numpy as np
nltk.download()

textId = nltk.corpus.gutenberg.fileids()

textId
#raw는 string단위로 불러옴
text = nltk.corpus.gutenberg.raw('austen-emma.txt')
len(text)
#words는 word단위로 불러옴
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma)
#sentence는 단어리스트를 문장별로 묶은 형태로 파일을 불러옴
sentence = nltk.corpus.gutenberg.sents('austen-emma.txt')
sentence[2:5]

longestLen = max(len(s) for s in sentence)

longestSent = [s for s in sentence if len(s)==longestLen]
longestSent

import matplotlib.pyplot as plt

''.join(sentence[1])

countWord =[len(n) for n in sentence]
countletter =[len(''.join(n)) for n in sentence]
# histogram만 보고싶을 때는 n, bins, patches로 나눠준다
# 이 때 n은 각 구간의 빈도수, bins는 구간을 나누는 기준점, patches는 그래프를 나타낸다
n, bins ,patches = plt.hist(countWord, bins=50)

n2, bins2 ,patches2 = plt.hist(countletter, bins=50)

countChar = [len(w) for s in sentence for w in s]
np.mean(countChar)
plt.hist(countChar)

textId

#각 소설별로 단어의 알파벳 수에 대한 빈도표 구하기
for i in textId:
    sentence = nltk.corpus.gutenberg.sents(i)
    countChar = [len(w) for s in sentence for w in s]
    print(i)
    plt.hist(countChar)
    plt.show()


from urllib import request
url ='http://www.gutenberg.org/files/1342/1342-0.txt'
response = request.urlopen(url)


#영화대본--webtext에서 불러오기-> 구어체가 많음

from nltk.corpus import webtext
textId = webtext.fileids()
textId
text = webtext.raw('pirates.txt')
print(text[:4000])

word =webtext.words('pirates.txt')

#인터넷의 일반 데이터-채팅

from nltk.corpus import nps_chat

textId = nps_chat.fileids()
print(textId)

text = nps_chat.raw(textId[0])
chatroom = nps_chat.posts(textId[0])
len(nps_chat.posts(textId[1]))


# 브라운 코퍼스 - 브라운 대학교에서 만든 전자문서
from nltk.corpus import brown
textId = brown.fileids()
print(textId)
cat = brown.categories()
cat
news = brown.raw(categories='news')
len(news)

brown.words(fileids=['cg22'])

#장르의 단어분포를 확인할 수 있음
cfd = nltk.ConditionalFreqDist((genre, word) for genre in brown.categories()
                               for word in brown.words(categories=genre))

print(cfd.conditions())
cfd['adventure']

genres = ['news','religion','hobbies','science_fiction','romance','humor']
modals = ['can','could','may','might','must','will']
cfd.tabulate(conditions=genres, samples=modals)


## 영어단어목록

wordlist = nltk.corpus.words.words()
print('단어개수 = ', len(wordlist))

print(wordlist[:30])

puzzleLetters = nltk.FreqDist('egivrvonl')
puzzleLetters
obligatory ='r'
answer =[w for w in wordlist if len(w)>=4 and obligatory in w
         and nltk.FreqDist(w) <= puzzleLetters]
answer

# 사람이름 목록

names = nltk.corpus.names
fileId = names.fileids()
fileId

maleNames = names.words('male.txt')
femaleNames = names.words('female.txt')
names.words(fileId[0])[-1]
names.words(fileId[0])[-1]
cfd = nltk.ConditionalFreqDist( (fileid, name[-1])
                               for fileid in names.fileids()
                                   for name in names.words(fileid))


for fileid in names.fileids():
    for name in names.words(fileid):
        nltk.ConditionalFreqDist(fileid,name[-1])
f = [w for w in cfd]
cfd[f[0]]
cfd[f[1]]
help(nltk.ConditionalFreqDist())


#워드넷

from nltk.corpus import wordnet as wn

wn.synsets('motorcar')
wn.synset('car.n.01').lemma_names()

wn.synset('car.n.01').definition()
wn.synset('car.n.01').examples()

wn.synsets('working')
wn.synset('work.v.02').lemmas()
wn.sysnet('work.v.02').lemma_names()

#문제1

# 지프의 법칙 (Zipf's Law)
# f(w) : 단어 w의 빈도
# rank(w) : 단어 w의 빈도 순위
# f(w) ~ 1/rank(w)
# log(f) = -1 * log(rank) : 기울기가 -1인 직선
import nltk
import numpy as np
from matplotlib import pyplot as plt
text = nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
fdist = nltk.FreqDist(text)
print(fdist)

x = np.arange(1, len(fdist) + 1)
y = sorted(list(fdist.values()), reverse=True)
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.xlim(1, 100)
plt.show()

plt.figure(figsize=(10, 6))
logx = np.log(x)
logy = np.log(y)
plt.plot(logx, logy)
plt.show()

print("기울기 = ", np.polyfit(logx, logy, 1)[0])

#문제2

emma = nltk.corpus.gutenberg.words('austen-emma.txt')

male_count=0
female_count=0
for word in emma:
    if word in names.words('male.txt'):
        male_count+=1
    elif word in names.words('female.txt'):
        female_count+=1
    else:
        pass
male_count, female_count
