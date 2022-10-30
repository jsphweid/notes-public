# gRPC

various tips and tricks from [here](https://www.youtube.com/watch?v=Z_yD7YPL2oE&list=WL)

deadlines - allow request to be given up on, can be propagated to all systems involved so they all give up at the same time

- [ ]  how exactly does that work?

errors - can be a part of the response, but usually recommended to be separate (like a graphQL error?)

protobufs are default encoding

- it's necessary to encode something when you have data in memory and you want to share it