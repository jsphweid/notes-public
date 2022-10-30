# Kubernetes

container orchestration tool

I watched [https://www.youtube.com/watch?v=VnvRFRk_51k](https://www.youtube.com/watch?v=VnvRFRk_51k), then [https://www.youtube.com/watch?v=aSrqRSk43lY](https://www.youtube.com/watch?v=aSrqRSk43lY)

cluster

- virtual network - makes all nodes behave as one "machine"
- nodes - has to have at least one main, then worker nodes, this is a cluster?
    - main node - controls critical orchestration processes
        - in production environment, probably have "multiple mains" somehow :thonk
        - contains api to kube cluster (dashboard/rest api/cli)
            - auth
            - kubectl is the cli-based entrypoint
        - controller manager - keeps track of states of other nodes, like which ones need to be repaired/restarted/etc.
        - scheduler - decides when to allocate more containers on which nodes based on workload, resources, etc.
        - etcd - key/value store that contains current state of cluster
            - can be used to recover the entire state
    - worker node(s) - do most of the work
        - each has kubelet process running on it
            - kubelet - process that makes it possible for cluster to talk to each other?
        - has multiple docker containers running... (but probably not necessarily docker
        - pods
            - pod - smallest unit of computation? to think of... wrapper around a container(s)...?
                - you can think of as a server
                - has a single IP address
                - usually only have multiple containers per pod if you need them as part of 1 application...? that's ambiguous
                    - answer: it sounds like it is recommended that a pod containers only 1 container unless you have "helper" containers like sidecars, proxies, bridges, adapters, etc. A good indicator on whether or not to keep it together or separate is to consider how things scale. If they benefit from scaling independently (which most things probably do), then it's best to put it on separate pods
                - if container inside a pod fails, pod will restart it
                - are ephemeral, if one dies, another created with new IP
                - often have **service** sitting in front of it
                    - when pod dies, service stays
                    - permanent IP address
                    - load balancer
                    - at first I thought it was more of a thing that runs on each pod, but it may be a running thing across multiple pods? or at least it makes it appear that way?? Like 5 pods running with the same image grouped as a service have 1 IP?
                        - can even use DNS so you don't have to specify IPs for services talking to each other (runs by default?)
                    - often can have **ingress** sitting in front of that
- deployment - declarative yaml/json template for creating pods
    - you give kubectl a deployment (which goes through the API?) and it stores/manages that (adds it to the main state?)
    - kinds
        - deployment - specifies things like what image to run, how many replicas, etc.
        - service - specifies a wrapper around a group of running deployments? (same selector/image?)
            - can have an external IP?
- config map - stores env vars more or less?
    - don't have to rebuild image
    - attached to the pod
- secret - stores secret env vars more or less (like config map but in b64)?
    - how is this any more secure?
- volumes - attachment that is local or remote storage
    - k8s doesn't manage persistence
- stateful set - stateful apps (dbs, elasticsearch, etc.)
    - helps manage pods that are stateful by "guaranteeing ordering and uniqueness of the pods" (?)
    - manages "sticky identity" for pods (instead of being ephemeral I assume)

Helm charts

- package manager for kub
- sounds similar to terraform modules or cdk constructs...?

pods

containers

services