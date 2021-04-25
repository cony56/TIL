### Docker container error troubleShoot

오류내용:

```
error during connect: This error may indicate that the docker daemon is not running.: Get http://%2F%2F.%2Fpipe%2Fdocker_engine/v1.24/containers/json: open //./pipe/docker_engine: The system cannot find the file specified.
```



1) `C:\Program Files\Docker\Docker` - 해당 디렉토리로 이동

2) `.\DockerCli.exe - SwitchDaemon`- 명령어 실행

-> 윈도우 환경에서 Docker 업데이트 이후 리눅스 컨테이너를 쓰는 세팅이 바뀌어서 그럼

-> 다시 리눅스 세팅으로 맞춰줘서 정상작동함