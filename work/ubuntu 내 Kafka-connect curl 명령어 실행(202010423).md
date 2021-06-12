## ubuntu 내 Kafka-connect curl 명령어 실행

kafka 접속

`bin/connect-distributed ./etc/kafka/connect-distributed.properties`



0) 토픽 생성

`bin/kafka-topics.sh --create --bootstrap-server 184.73.31.161:9092 --topic(토픽이름) `

1) 토픽 생성여부 확인

`ubuntu@ip-172-31-55-25:~/kafka_2.12-2.5.0$ bin/kafka-topics.sh --list --bootstrap-server 184.73.31.161:9092`



2) kafka, zookeeper 서버 켜졌는지 확인

`netstat -ntlp | grep 2181` - > zookeeper server

```
tcp6       0      0 :::2181                 :::*                    LISTEN      18742/java     
```

-> Listen 중

`netstat -ntlp | grep 9092` -> kafka server

3) Curl 명령어로 source-connector를 REST-Api Post방식으로 호출함

```
echo '
{
"name":"market_source2",
"config":{
"connector.class":"io.confluent.connect.jdbc.JdbcSourceConnector",
"connection.url":"jdbc:mysql://18.206.167.14:49156/mysql",
"connection.users":"root",
"connection.password":"",
"mode":"incrementing",
"incrementing.column.name":"id",
"table.whitelist":"market_db",
"topic.prefix":"my_",
"tasks.max":"1"
     }
}
' | curl -X POST -d @- http://localhost:8083/connectors --header "content-Type:application/json"
```

*** Connection 에러

```
 "trace": "org.apache.kafka.connect.errors.ConnectException: java.sql.SQLInvalidAuthorizationSpecException: Could not connect to address=(host=172.31.18.246)(port=3306)(type=master) : (conn=26) Access denied for user 'ubuntu'@'172.31.55.25' (using password: NO)\n\tat io.confluent.connect.jdbc.util.CachedConnectionProvider.getConnection(CachedConnectionProvider.java:59)\n\tat io.confluent.connect.jdbc.JdbcSourceConnector.start(JdbcSourceConnector.java:92)\n\tat org.apache.kafka.connect.runtime.WorkerConnector.doStart(WorkerConnector.java:110)\n\tat org.apache.kafka.connect.runtime.WorkerConnector.start(WorkerConnector.java:135)\n\tat org.apache.kafka.connect.runtime.WorkerConnector.transitionTo(WorkerConnector.java:195)\n\tat org.apache.kafka.connect.runtime.Worker.startConnector(Worker.java:259)\n\tat org.apache.kafka.connect.runtime.distributed.DistributedHerder.startConnector(DistributedHerder.java:1229)\n\tat org.apache.kafka.connect.runtime.distributed.DistributedHerder.access$1300(DistributedHerder.jav
```

** 해결방법

AWS 보안그룹에 가서 Inbound규칙에 mysql의 port를 모든 서버에 대해 열어줌



## 404 error

```
{
  "error_code": 404,
  "message": "No status found for connector market_source6"
}
```

```
** 해결방법

echo '      

{
    "name" : "market_source",
    "config" : {
        "connector.class" : "io.confluent.connect.jdbc.JdbcSourceConnector",
        "connection.url" : "jdbc:mysql://172.31.18.246:49156/mysql",
        "connection.user" : "root",
        "connection.password" : "",
        "mode" : "bulk",
        "incrementing.colum.name" : "id",
        "table.whitelist" : "test",
        "topic.prefix" : "my_topic_",
        "tasks.max" : "1",
        "key.converter": "org.apache.kafka.connect.storage.StringConverter",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "db.timezone": "UTC"
    }
}
' | curl -X POST -d @- http://localhost:8083/connectors --header "content-Type:application/json"
```

->  해림님 코드 참조해서 뒤에 key.converter, value.converter, db.timezone 입력하니까 작동함



5) topic에 잘 전송됐는지 확인

`bin/kafka-console-consumer.sh --topic bus_stop --from-beginning --bootstrap-server 184.73.31.161:9092`



6) kafka 목록 확인

`curl http://localhost:8083/connectors | jq`

7) kafka connect status 확인

`curl http://localhost:8083/connectors/(커넥터이름)/status | jq`

8) connector 상태 이상할 시 삭제

`curl -X DELETE -s "http://{ip}:8083/connㅋectors/test-connector"`

### Kafka sink connector

```
echo ' 
{
    "name" : "market_sink",
    "config" : {
        "connector.class" : "io.confluent.connect.jdbc.JdbcSinkConnector",
        "connection.url" : "jdbc:mysql://marketdt.cblvwasqgnme.us-east-1.rds.amazonaws.com:3306/market",
        "connection.user" : "admin",
        "connection.password" : "12345678",
        "auto.create":"true",
        "auto.evolve":"true",
        "delete.enabled":"false",
	"tasks.max":"1",
	"topics":"market_test",
        "db.timezone": "UTC",
"key.deserializer": "org.apache.kafka.common.serialization.StringDeserializer",
"value.deserializer":"org.apache.kafka.common.serialization.StringDeserializer"
    }
}
' | curl -X POST -d @- http://localhost:8083/connectors --header "content-Type:application/json"
```

echo '      

{
    "name" : "market_source",
    "config" : {
        "connector.class" : "io.confluent.connect.jdbc.JdbcSourceConnector",
        "connection.url" : "jdbc:mysql://172.31.18.246:49156/mysql",
        "connection.user" : "root",
        "connection.password" : "",
        "mode" : "bulk",
        "incrementing.colum.name" : "index",
        "table.whitelist" : "test",
        "topic.prefix" : "market_",
        "tasks.max" : "1",
      "key.serializer": "org.apache.kafka.common.serialization.StringSerializer",
"value.serializer":"org.apache.kafka.common.serialization.StringSerializer",
        "db.timezone": "UTC"
    }
}
' | curl -X POST -d @- http://localhost:8083/connectors --header "content-Type:application/json"



## db utf-8 오류

show variables like 'c%';

-> 컬럼 어떤 포맷으로 저장됐는지 확인가능