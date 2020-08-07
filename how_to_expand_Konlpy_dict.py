# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:53:54 2020

@author: student
"""


import konlpy
## 사전등록하는 법
## 1. KONLPY가 있는 폴더를 찾아 간다
## 2. KONLPY 폴더내의 JAVA폴더내에 작업용 폴더를 하나 만든다.
## 3. CMD 창을 연다.
## 4. CMD에 "cd 작업용 폴더의 경로" (cd는 change directory)입력 (그러면 콘솔 명이 바뀐다. 그상태에서 dir입력시 그 디렉토리에있는 파일을 확인할 수 있다.)
## 5. jar xvf ../open-korean-text-2.1.0.jar 을 입력 (..은 한단께이전 디렉토리를 의미) (이 문구로 이전 폴더의 특정파일을 작업 폴더로 풀어서 옮겨온다.)
## 6. 그후 작업용 폴더를 보면 org폴더가 있다. 이폴더에 들어가자
## 7. org -> openkoreantext -> processor -> util 의 순서대로 폴더 들어가기
## 8. 최종 도착지인 util폴더내에 사전들이 들어있다.(품사별 폴더)
## 9. 원하는 품사 별 폴더를 들어가서 그 품사 폴더내의 알맞은 txt파일내에 추가할 단어를 입력하고 저장한다.
## 10. 최초 작업폴더로 돌아간다.
## 11. CMD창에 "jar cvf open-korean-text-2.1.0.jar *" 입력 (이전 5단계에서 풀은파일을 다시 묶어준다.)
## 12. 위단계를 수행하면 작업폴더에 open-korean-text2.10.jar 파일이 생성된다.

from konlpy.tag import Okt

text = '레오나르도 디카프리오는 삼성에 갔다'

okt = Okt()
print(okt.morphs(text))
