# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:34:48 2020

@author: student
"""
import numpy as np


doc=['gold silver truck',
     'Shipment of gold damaged in a fire',
     'Delivery of silver arrived in a silver truck',
     'Shipment of gold arrived in a truck']

doc1 = doc[0].split()
doc2 = doc[1].split()
doc3 = doc[2].split()
doc4 = doc[3].split()
voc_list = list(set(doc1+doc2+doc3))
voc_list

def tf(doc, voc_list):
    tf_value={}
    for i in voc_list:
        tf_value[i]=0
        for j in doc:
            if i == j:
                tf_value[i]+=1
    return tf_value


tf_1 = tf(doc1, voc_list)
tf_2 = tf(doc2, voc_list)
tf_3 = tf(doc3, voc_list)
tf_4 = tf(doc4, voc_list)


tf_list=[tf_1,tf_2,tf_3,tf_4]
def idf(tf_list):
    df_value={}
    for i in tf_list[0]:
        df_value[i]=0
    for dic in tf_list:
        for key in dic:
            df_value[key]+=dic[key]
    for key in df_value:
        df_value[key]= np.log(len(tf_list)/df_value[key])
    return df_value
        
idf=idf(tf_list)

for i, j in enumerate(tf_1):
    print(i,j)

def tf_idf(tf, idf):
    tf_idf={}
    idf_value = np.array(list(idf.values()))
    tf_value = np.array(list(tf.values()))
    tf_idf_val = tf_value*idf_value
    for idx, key in enumerate(tf):
        tf_idf[key]= tf_idf_val[idx]
    return tf_idf

tf_idf1 = tf_idf(tf_1,idf)
tf_idf2 = tf_idf(tf_2,idf)  
tf_idf3 = tf_idf(tf_3,idf)    
tf_idf4 = tf_idf(tf_4,idf)

def dots(a,b):
    a_value = np.array(list(a.values()))
    b_value = np.array(list(b.values()))
    result = np.dot(a_value,b_value)
    return result

dots(tf_idf1,tf_idf2), dots(tf_idf1,tf_idf3), dots(tf_idf1,tf_idf4)
