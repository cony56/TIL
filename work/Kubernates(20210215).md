## Docker Compose

* Docker 커맨드, 복잡한 설정을 쉽게 관리하기 위한 도구
* YAML fomat에 Docker 생성, 설정관련된 작업으 작성해 놓은 Script 파일

YAML파일구조 -> json파일과 같고 key:value 형태로 구성됨

* 커맨드의 세부구조 따라 들여쓰기가 되어있음
* Docker compose파일을 통해 여러가지 컨테이너를 쉽게 한번에 관리할 수 있음



** `netstat -ano`

-> 포트번호가 이미 사용중이라고 했을 때 해당포트가 연결된 작업을 확인할 수 있음

```powershell
 프로토콜  로컬 주소              외부 주소              상태            PID
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       1032
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:1536           0.0.0.0:0              LISTENING       452
  TCP    0.0.0.0:1537           0.0.0.0:0              LISTENING       844
  TCP    0.0.0.0:1538           0.0.0.0:0              LISTENING       1576
  TCP    0.0.0.0:1539           0.0.0.0:0              LISTENING       2464
  TCP    0.0.0.0:1540           0.0.0.0:0              LISTENING       2032
  TCP    0.0.0.0:1541           0.0.0.0:0              LISTENING       4060
  TCP    0.0.0.0:3306           0.0.0.0:0              LISTENING       4632
```

작업관리자의 세부정보에서 해당 PID를 찾아 프로세스 종료할 수 있음



* docker-compose.yml의 예시

```dockerfile
version: "3.9"
services:
  my-mysql:
    container_name: mysql_server
    image: mysql:5.7
    volumes: 
      - ../sql_volmount:/var/lib/mysql
    ports:
      - 3306:3306
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: mydb
  
  my-django:
    image: edowon0623/mydjango
    ports:
      - 8000:8000
    depends_on:
      - my-mysql
```



* depends_on : 컨테이너 간 먼저 run해야되는 순서가 있기 때문에 container의 dependency를 지정해 줌



### Kubernates



### Kubernates란?

* 컨테이너(도커와 같은) 운영을 자동화하기 위한 컨테이너 오케스트레이션 도구 
* 많은 수의 컨테이너를 협조적으로 연동시키기 위한 통합 시스템이며 이 컨테이너를 다루기 위한 API 및 명령행 도구가 함께 제공됨