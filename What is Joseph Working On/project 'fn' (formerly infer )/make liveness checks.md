# make liveness checks

tensorflow serving

- use rest API port to run something like `curl -d '{"instances": [1.0, 2.0, 5.0]}' -X POST [http://fn-serving-service:8501/v1/models/half-plus-two-cpu:predict](http://fn-serving-service:8501/v1/models/half-plus-two-cpu:predict)`

grpc api

- install this grpc health check on the docker image

```docker
RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

RUN GRPC_HEALTH_PROBE_VERSION=v0.3.1 && \
  wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-amd64 && \
  chmod +x /bin/grpc_health_probe
```

gql api

- should be easy to do an http request

- [ ]  read more [here](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
- [ ]  implement stuff