# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 09:47:56 2020

@author: student
"""


import nltk

text = 'Take me into your loving heart. Kiss me under the light of thousand stars'
token = nltk.word_tokenize(text)
token
nltk.pos_tag(token)

from nltk.corpus import brown
brown_news_tagged = brown.tagged_words(categories='news',tagset='universal')
tag_fd = nltk.FreqDist(tag for (word,tag) in brown_news_tagged)
tag_fd.most_common(12)


#품사 태깅
#p55
import nltk
import matplotlib.pyplot as plt

# Transition probability 찾기
tagged_words = []
all_tags=[]
#nltk.corpus.brown.tagged_sents(tagset='universal')[0]

for sent in nltk.corpus.brown.tagged_sents(tagset='universal'):
    tagged_words.append(("START","START"))
    all_tags.append("START")
    for (word, tag) in sent:
        all_tags.append(tag)
        tagged_words.append( (tag,word))
    tagged_words.append( ("END",'END'))
    all_tags.append("END")

cfd_tags = nltk.ConditionalFreqDist(nltk.bigrams(all_tags))
cpd_tags = nltk.ConditionalProbDist(cfd_tags, nltk.MLEProbDist)

print("Count('DET','NOUN') =", cfd_tags['DET']['NOUN'])
print("P('NOUN | 'DET') =", cpd_tags['DET'].prob('NOUN'))

#Emission probability 찾기
cfd_tagwords = nltk.ConditionalFreqDist(tagged_words)

cpd_tagwords = nltk.ConditionalProbDist(cfd_tagwords, nltk.MLEProbDist)

print("Count('DET','the') =", cfd_tagwords['DET']['the'])
print("P('the'|'DET')=", cpd_tagwords['DET'].prob('the'))


#p56

#명사 앞에 많이 오는 품사를 확인함
brown_news_tagged
word_tag_pairs = nltk.bigrams(brown_news_tagged)
bigram = [(a,b) for (a,b) in word_tag_pairs]

noun_preceders = [a[1] for (a,b) in bigram  if b[1]=='NOUN' ]
noun_preceders

fdist = nltk.FreqDist(noun_preceders)
[tag for (tag,_) in fdist.most_common()]

[]
































