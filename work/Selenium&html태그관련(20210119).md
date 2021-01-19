## 기본적인 리눅스 명령어

* 버전 충돌없이 해당 프로젝트 내에서 필요한 버전만 받기 위해 가상환경을 만듦

1) `conda info --envs` - conda 환경보기

2) `conda list` : conda 내의 라이브러리 리스트 확인

3) `conda create --name (가상환경 이름)`

4) `conda remove --name (가상환경이름) --all`: 가상환경 지우기

5) `conda activate (가상환경이름)  : 가상환경 활성화하기/ Anaconda Prompt에서 실행하기

-> Prompt 내 (base) 에서 (가상환경)으로 바뀜

6) `code (이름).py`



Selenium

- 웹 애플맄이션 테스트 프레임워크
- 웹 사이트에서 버튼 클릭과 같은 이벤트 가능



driver = webdriver.Chrome(path) : 지정한 path로 webdriver 실행

driver.get("url링크")

driver.title() : 웹페이지 위쪽에 나와있는 제목



제어할 수 있는 필드

"https://www.google.com/search?ei=5zkGYNGkMNqnoAS3x6zwCQ

&q=python : (검색어)

&oq=django

&gs_lcp=CgZwc3ktYWIQAzIHCAAQsQMQQzIECAAQQzIECAAQQzIICAAQsQMQgwEyAggAMgIIADICCAAyAggAMgIIADICCAA6BQgAELEDOgQIABAKOgYIABAKECo6CggAELEDEIMBEAo6BwgAELEDEApQ-4QBWI-RAWDQlAFoAXABeACAAY4FiAGvE5IBCTItMi4xLjIuMZgBAKABAaoBB2d3cy13aXrAAQE

&sclient=psy-ab

&ved=0ahUKEwiRtMSI8KbuAhXaE4gKHbcjC54Q4dUDCA0

&uact=5"



-> 이렇게 webdriver 링크를 보면 &뒤에 제어할 수 있는 element 이름이 나옴



```python
search_box = driver.find_element_by_name("q")

search_box.send_keys('cloud computing')

search_box.submit()
```

->  해당 element를 넣어주고 send_key에 검색어를 입력한 후, submit() 해주면 검색키를 제어할 수 있음



```python
#제어할 Keys 관련된 method
from selenium.webdriver.common.keys import Keys

elem_email = driver.find_element_by_id('email')
elem_email.send_keys(['[페이스북 아이디]'])
elem_pass =driver.find_element_by_id('pass')
elem_pass.send_keys(['[페이스북 비밀번호]'])
elemm_pass.send_keys(Keys.RETURN)
```



Xpath: Xml 파일의 위치값을 말함

Ex) //*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[5]/div[2]/div[1]/button

-> anchor tag의 위치를 찾을 수 있음

```python
profile_a = driver.find_element_by_xpath('a태그로 되어있는 정보')

print("Profile A =>", profile_a.get_attribute('href'))


```

* <a> 태그의 속성

1) href: 연결할 주소를 지정함

2) target: 링크를 클릭할 때 창을 어떻게 열지 설정함

3) title: 해당 링크에 마우스 커서를 올릴 때 도움말 설명을 설정함



### 이왕 html 나온 김에 다른 태그도 찾아보자

* 
  div  태그의 속성

-웹 페이지의 레이아웃을 구성하고 싶을 때 div를 통해 영역을 설정함

-줄 바꿈을 할 수 있고 사각형 박스로 구역을 정함( div가 추가될 때 마다 다음 줄에 박스가 생김)

-박스 외각에 라인이 그려짐 -> width, height 등 박스의 크기를 조정할 수 있음

-div의 margin은 모든 방향으로 적용이 되고 위 아래의 div와 겹치는 margin은 상쇄됨

* span 태그의 속성

-영역을 설정하는 것에선 동일하지만 그 형식이 조금 다름(줄 단위로 영역 설정)

-span tag 추가 시 다음 줄이 아닌 옆으로 배열 됨

-inline 속성을 가지기 때문에 크기 지정이 불가능 함

-span은 margin이 양옆 방향으로 적용되고 왼, 오른쪽의 다른 span과 margin이 겹치지 않음



