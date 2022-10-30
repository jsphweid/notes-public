# dumb question, text/binary web

Status: random thoughts

it's all binary information under the covers, right? Then why can't you use gRPC easily with the web

- I think the reason is that you need fine-grained control to really take advantage of it, and the browser just doesn't have APIs that give you that closeness. See [this](https://grpc.io/blog/state-of-grpc-web/)
    - for example, you can't access the frames