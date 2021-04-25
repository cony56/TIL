# Service Discovery



## Consul

Consul 경로접속

`consul agent -dev -ui -datacenter zone1 -node host1 -config-dir ./consul.d/`



* 가변 IP정보를 이용할 때

`set TAX_SVC_URL=http://127.0.0.1:15002`

## Dig

Dig 경로접속

`dig @127.0.0.1 -p 8600 order.service.consul SRV`