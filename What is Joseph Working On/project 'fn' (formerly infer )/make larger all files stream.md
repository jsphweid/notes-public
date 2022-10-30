# make larger/all files stream

- implement streaming in fn
    - need to stream at every layer probably
    - [ ]  put max message size down really small everywhere (smaller than default) so it forces us to adjust wherever necessary
        - [ ]  tensorflow-serving ↔  grpc ↔  graphql (if still exists)
- [ ]  remove max message size...?