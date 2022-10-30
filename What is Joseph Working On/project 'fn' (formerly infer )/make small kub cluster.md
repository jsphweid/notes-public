# make small kub cluster

Status: Completed

consists of 

- tensorflow-serving
- python grpc api
- graphql api

on chicken:

1. terminal 1
    - `minikube start`
    - `minikube dashboard`
2. terminal 2
    - `kubectl proxy &`

on macbook

1. terminal 1
    - `ssh -L 30000:127.0.0.1:8001 jsphweid@chicken`
        - uses port forwarding... basically, it listens to macbook [localhost](http://localhost) 30000 to connect to `127.0.0.1:8001` via `jsphweid@chicken`
            - this [https://stackoverflow.com/a/47585628/4918389](https://stackoverflow.com/a/47585628/4918389) didn't seem to help, but from [this video](https://www.youtube.com/watch?v=N8f5zv9UUMI) I learned the other similar technique
- [ ]  ~~configure automatic updates~~ probably not a good idea for now
- [ ]  ~~use minikube for now entirely~~
- [x]  turn graphql service into docker container
- [x]  host publicly on dockerhub
- [x]  boot up in cluster as pod via a deployment (same on that we were using?)
- [x]  turn python service into a docker container
- [x]  host publicly on dockerhub
- [x]  test that it can talk to the tf-serving container
- [x]  need to wrap everything in services...?

- [ ]  ~~establish health checks~~