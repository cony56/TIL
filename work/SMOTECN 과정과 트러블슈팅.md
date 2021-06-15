### SMOTECN 과정과 트러블슈팅



### SMOTE-CN이란?

Smote sampling을 할 때 기존의 수치형 변수와 다르게 범주형 변수도 결합하여 샘플링을 할 수 있는 방법론

`from imblearn.over_sampling import SMOTENC`

- 이거 하나만 바꿔주면 될 줄 알았는데 생각보다 해야할 게 많았음



1. Cat 변수는 One-hot, Label Encoder를 적용하지 않은 채로 가져와야 함

-> 기존 개발자가 만든 코드에서 One-hot, Label Encoder를 고치는 과정에서 encoding 방식을 배움

Train, Test의 변수명과 비율을 그대로 유지한 상태로 코드를 고치다 보니 어려웠음

-> 특히 