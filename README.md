# Installation
## 1.) Install Docker (you're on your own here, there are plenty of guides)
## Install loki log docker driver - $ docker plugin install grafana/loki-docker-driver:2.9.2 --alias loki --grant-all-permissions

# Usage
### $ docker-compose up -d
### $ docker-compose down
### $ docker container stop pg_container grafana && docker container rm pg_container grafana && docker image rm bi-shoc-op-log-sim_postgres:latest && sudo rm -rf postgres/data/ && ### ### $ docker-compose down
### $ docker-compose up -d && docker logs -f pg_container

# Links
## Grafana server - http://localhost:3000/?orgId=1
## Prometheus server (username=admin, password=admin) - http://localhost:9090/
## pgAdmin (username=shoc@shoc.us, password=JustKeepSwimming) - http://localhost:3031/
### -> Add server, in connection tab set (host=pg_container, username=shoc, password=JustKeepSwimming)
## jupyterLab - http://localhost:8889/