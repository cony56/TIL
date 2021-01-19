# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:51:54 2020

@author: student
"""


import random

def roll_a_die():
    return random.choice(range(1,7))

# 두개의 확률분포를 만듬
# x는 첫 주사위의 값에 대한 확률분포
# Y는 두 주사위 값의 합에 대한 확률분포
def direct_sample():
    d1 = roll_a_die()
    d2 = roll_a_die()
    return d1, d1+d2

#X에 대한 y의 조건부확률과 y에 대한 x의 조건부 확률 함수를 만듬

def random_y_given_x(x):
    return x + roll_a_die()

def random_x_given_y(y):
    if y <= 7:
        return random.randrange(1,y)
    else:
        return random.randrange(y-6, 7)
    
def gibbs_sample(num_iters=100):
    # 초기값은 상관없음
    x, y = 1, 2
    for _ in range(num_iters):
        x = random_x_given_y(y)
        y = random_y_given_x(x)
    
    return x, y


gibbs_sample()
