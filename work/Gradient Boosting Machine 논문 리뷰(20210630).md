## Gradient Boosting Machine 논문 리뷰

* Greedy Function Approximation이 GBM의 핵심 원리
* '모형이 반환하는 잔차에 대한 잔차를 줄여나가기 위해 모델을 만든다'가 Greedy Function의 과정임
* 모델들이 직렬로 연결되어 예측 오차를 줄여나가기 때문에 boosting 알고리즘의 한 방법



### 1.0 Function Estimation

* 목표함수를 수식으로 정의함

$$
F^* = \mathop{\arg\min}_{F}E_{y,x}L(y,F(x)) = \mathop{arg min}_{F}E_{x}[E_y(L(y,F(x)))| x]
$$

찾고자하는 F'은 x가 주어졌을 때 y와 F(x)로 이루어진 손실함수(보통 MSE, negative-log likelihood, squared_error 등)에 대해 전 구간의 평균값을 minimize 하는 함수

* x에 대한 함수를 여러 파라미터를 갖는 함수로 확장시킴

$$
F(x;\{ \beta_m, a_m\}^M_{1} = \sum_{m=1}^M\beta_mh(x;a_m))
$$

F 함수는 보통 ML, DL 함수에서 weight와 파라미터 간 곱으로 나타남

### 1.1 Numerical Optimization

* parameterized model을 선택하는 문제(P*모델을 고르는 것)는 곧 파라미터 최적화 문제임

$$
P^* = \mathop{arg min}_P\Phi(P)
$$

* P에 대한 함수는 y와 f* 로 이루어진 손실 함수를 뜻함(P= 파라미터)

$$
\Phi(P) = E_{y,x}L(y,F(x;P))
$$

* F*(x) 함수는 결국 손실함수를 최소화시키는 parameter로 이루어진 함수

$$
F^*(x) = F(x;P^*)
$$
























