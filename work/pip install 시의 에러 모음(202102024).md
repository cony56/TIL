## pip install 시의 에러 모음



1) `pip install scrapy`

문제상황

```powershell
 copying src\twisted\internet\test\_yieldfromtests.py.3only -> build\lib.win32-2.7\twisted\internet\test
    creating build\lib.win32-2.7\twisted\internet\test\fake_CAs
    copying src\twisted\internet\test\fake_CAs\chain.pem -> build\lib.win32-2.7\twisted\internet\test\fake_CAs
    copying src\twisted\internet\test\fake_CAs\not-a-certificate -> build\lib.win32-2.7\twisted\internet\test\fake_CAs
    copying src\twisted\internet\test\fake_CAs\thing1.pem -> build\lib.win32-2.7\twisted\internet\test\fake_CAs
    copying src\twisted\internet\test\fake_CAs\thing2-duplicate.pem -> build\lib.win32-2.7\twisted\internet\test\fake_CAs
    copying src\twisted\internet\test\fake_CAs\thing2.pem -> build\lib.win32-2.7\twisted\internet\test\fake_CAs
    copying src\twisted\mail\test\rfc822.message -> build\lib.win32-2.7\twisted\mail\test
    copying src\twisted\python\test\_deprecatetests.py.3only -> build\lib.win32-2.7\twisted\python\test
    copying src\twisted\words\im\instancemessenger.glade -> build\lib.win32-2.7\twisted\words\im
    copying src\twisted\words\xish\xpathparser.g -> build\lib.win32-2.7\twisted\words\xish
    running build_ext
    building 'twisted.test.raiser' extension
    error: INCLUDE environment variable is empty

    ----------------------------------------
Command "c:\python27\python.exe -u -c "import setuptools, tokenize;__file__='c:\\users\\thomas~1\\appdata\\local\\temp\\pip-build-3oirm6\\Twisted\\setup.py';
f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))"
 install --record c:\users\thomas~1\appdata\local\temp\pip-xvbgd2-record\install-record.txt --single-version-externally-managed --compile" 
failed with error code 1 in c:\users\thomas~1\appdata\local\temp\pip-build-3oirm6\Twisted\
```

twisted 파일을 설치하는데서 문제가 생김

문제원인: twisted 파일이 python 3.8 버전에서 자동으로 안깔림

문제해결:

​	1>https://www.lfd.uci.edu/~gohlke/pythonlibs/ 에 들어가 컴퓨터에 알맞은 twisted.whl 버전을 다운로드함

​	2> `pip install <Twisted-18.7.0-cp35-cp35m-win_amd64.whl>` 와 같이 다운로드 받은 .whl 파일로 twisted 다운로드를 진행함

​	3> 이후 다시 `pip install scrapy`를 진행함

 2) `pip install tensorflow`

````
socket.timeout: The read operation timed out
````

문제원인: 네트워크 커넥션이 불안정해 생기는 오류임

문제 해결: `pip --default-timeout=300 install tensorflow` 로 timeout 시간을 늘려주어 해결