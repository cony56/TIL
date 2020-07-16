# GAN

## 1. 모델 이해

### 1.1 GAN의 특성

Unsupervised Learning방식으로 이미지, 문서, 음성 데이터를  **생성**하는 알고리즘이다.

이전에 배운 ANN, CNN, RNN이 예측을 위한 알고리즘이라면 GAN의 목적은 "데이터 생성"이다. GAN은 보유중인 데이터와 유사한 데이터를 생성한다는 점에서 앞에서 배운 AutoEncoder와 닮았다. 

* AutoEncoder : 입력(학습 데이터)  --> 모델(딥러닝 모델) --> 출력(학습 데이터)
* GAN :입력(기존데이터, 랜덤데이터) --> 모델(두 개의 딥러닝 모델) --> 출력(Sigmoid)

GAN의 기본원리는 



하지만 출력값에 입력값 자신을 넣어 학습하는 AutoEncoder와 달리 GAN은 Generator와 Discriminator라는 두 개의 신경망을 결합하여 랜덤 데이터가 기존데이터와 닮도록 학습시킨다.

GAN(랜덤 데이터, 학습 데이터) ---> 랜덤값

어떤 뜬금없는 데이터를 넣어도 학습 데이터와 




$$
\min_{G} \max_{D}V(D,G) = E_{x \sim p_{data(x)}}[logD(x)+ E_{z \sim p_{z}}[log(1-D(G(z))]
$$












https://hyunw.kim/blog/2017/10/27/KL_divergence.html

### 1.2 GAN을 왜 쓸까?

* GAN은 



