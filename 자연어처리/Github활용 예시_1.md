# Git

Git은 분산형버전관리시스템(DVCS) 중 하나이다.

`>`를 써서 인용문을 나타내기도 한다

## 0. Git 기초 설정

* windows 환경에서는 `git for windows`로 검색하여 git bash를 설치한다.[다운로드 링크](https://gitforwindows.org/)
* 최초에 컴퓨터에서 git을 사용하는 경우 아래의 설정을 진행한다.

```bash
$ git config --global user.email 이메일주소
$ git config --global user.name 유저네임
#확인을 위해
$ git config --global-1

```

* 이메일주소를 설정할 때, github에 가입된 이메일로 설정을 해야 커밋 이력이 github에 기록된다.

## 1. Git을 통한 버전관리 기본 흐름

### 1.1. Git 저장소 초기화

> 특정 폴더를 git 저장소로 활용하기 위해서 최초에 입력하는 명령어

```bash
$git init
Initialized empty Git repository in C:/Users/student/Desktop/TIL/.git/(master) $
```
* .git 폴더가 숨긴 폴더로 생성되며, git bash에서는 (master)라고 표기된다.
* 반드시 git으로 활용되고 있는 폴더 아래에서 저장소를 선언하지 말자

### 1.2. add

> 커밋 대상 파일들을 추가한다.

add 전 상황
```bash
$ git status

On branch master

No commits yet

# 트랙킹 되지 않는 파일들

# => 새로 생성된 파일이고, git으로 관리 중이지 않는 파일

Untracked files:

	# git add 파일

# 커밋이 될 것들을 포함시키기 위해서 위의 명렁어를 써라~

  (use "git add <file>..." to include in what will be committed)
        markdown-images/
        markdown.md
On branch master

No commits yet
# 커밋후 변경사항들
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   "markdown-images/\353\263\264\353\205\270\353\263\264\353\205\270.jpg"
        new file:   markdown.md
        new file:   "\353\263\264\353\205\270\353\263\264\353\205\270.jpg"

```

add 명령어는 아래와 같이 활용된다.

```bash
$git add . #현재 디렉토리 전부
$git add 파일명.md # 특정 파일
$git add markdown-images/ # 특정 디렉토리
```

### 1.3 commit

```bash
$ git commit -m '커밋메시지'
[master (root-commit) be7a883] Init
 3 files changed, 99 insertions(+)
 create mode 100644 "markdown-images/\353\263\264\353\205\270\353\263\264\353\205\270.jpg"
 create mode 100644 markdown.md
 create mode 100644 "\353\263\264\353\205\270\353\263\264\353\205\270.jpg"

```

#### log

> 커밋 내역들을 확인할 수 있는 명령어

```bash
$ git log
commit be7a883f5301575e3f9f380ffd780289cb79febe (HEAD -> master)
Author: cony56 <taeyup56@hanmail.net>
Date:   Wed Jul 8 14:47:50 2020 +0900

    Init

#최근 n개 이력(1개)
$ git log -1
commit be7a883f5301575e3f9f380ffd780289cb79febe (HEAD -> master)
Author: cony56 <taeyup56@hanmail.net>
Date:   Wed Jul 8 14:47:50 2020 +0900

    Init

# 간략한 표현
$ git log --oneline
be7a883 (HEAD -> master) Init

#최근 n개 이력을 간략하게
$ git log --oneline -1
be7a883 (HEAD -> master) Init

$git status
$ git status
#커밋할 것도, 작업할 것도 없다
On branch master
nothing to commit, working tree clean

```

## 2. 원격 저장소 활용

> 원격 저장소(remote repository)를 제공하는 서비스는 많다.(gitlab, bitbucket)
>
> 그 중에서 github을 기준으로 설명하겠다.

### 2.1. 원격 저장소 등록

> git아, 원격저장소(remote)로 등록해줘(add) origin이라는 이름으로 등록해줘



```bash
$git remote add origin 저장소url
```

* 저장소 확인

```bash
$git remote -v
origin  https://github.com/cony56/TIL.git (fetch)
origin  https://github.com/cony56/TIL.git (push)
```

* 저장소 삭제

origin으로 지정된 저장소를 rm(remove)한다

```bash
$ git remote rm origin
```



### 2.2 push

origin으로 설정된 원격저장소의 master브랜치로 push한다.

``` bash
$git push origin master
#
```



* commit을 안하면 push를 해도 안올라간다/ 즉 파일 전체가 올라가는 게 아니다
* commit을 클릭해보면 각각의 버전마다의 파일정보들이 고스란히 있다



## 주의사항

> 원격저장소와 로컬 저장소의 이력이 다르게 저장되는 경우
>
> Github에서 직접 파일 수정을 하거나,
>
> 협업하는 과정이거나,
>
> 집-강의장 환경으로 왔다갔다하는 상황 등에서 발생하는 오류

## 기술블로그 만들기

kakao.github.io

* 정적파일생성기

-마크다운 파일을 바탕으로 html로 변환시켜줌

Jekyll(지킬)

-예전부터 많이 쓰임

-ruby

Gatsby

-최근에 많이 쓰임

-Js, React, graphql



## 코딩 참조

* programmers
* 백준알고리즘
* swexpertacademy - 삼성 알고리즘 무료강의 있음
* 