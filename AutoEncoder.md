# AutoEncoder

## 1. 핵심

### 1.1 self supervised learning이다

* 입력층과 출력층의 shape와 값이 동일하다

* encoder는 latent feature의 역할을 한다

* 기존의 feature들을 압축한 값으로 차원축소, 노이즈 제거 등에 사용된다.





## 1. Transposed convolution

* Convolution AutoEncoder에서 Encoding을 통해 축소된 값을 Decode할 때, 즉 입력 데이터의 shape으로 복원시킬 때 필요하다.
* 더 직관적으로 이해하려면 저해상도의 이미지를 고해상도 이미지로 만들기 위한 Upsampling에 사용한다.

### 풀이1



[참고자료](https://zzsza.github.io/data/2018/02/23/introduction-convolution/)

출처: https://zzsza.github.io/data/2018/02/23/introduction-convolution/

아래 그림은 convolution연산이 filter와 input의 행렬곱 연산으로 표현된다.

이 때 filter(혹은 kernel)은 행렬연산을 위해 0을 추가한 sparsed matrix 형태로 변환한다.

![transposed2d_1](C:%5CUsers%5Cstudent%5CDesktop%5CTIL%5Cmarkdown-images%5Ctransposed2d_1.png)



Transposed Convolution2d는 sparsed matrix의 전치행렬에Convolution 출력값을 곱한 값이다. 이러면 Convolution의 입력값과 shape이 동일해진다.  하지만 Sparse Matrix에 0이 많은 것에서 알다시피 정보의 유실이 있다는 단점이 있다.

![transposed2d_2](C:%5CUsers%5Cstudent%5CDesktop%5CTIL%5Cmarkdown-images%5Ctransposed2d_2.png)

### 풀이2



