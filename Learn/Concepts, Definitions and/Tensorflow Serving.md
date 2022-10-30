# Tensorflow Serving

grpc - high level `classify` and `regress` are higher level abstractions than `predict`, but `predict` can be more performant for large requests somehow

aws ideas:

docker containers, one gpu, one cpu, definitely should be in the same AZ if not [clustered placement group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) if possible

batching - [more [[]] - two ways

- batching requests (sending multiple per request)
- single requests but allowing tf to batch under the hood
    - probably need very high requests per second for this to be worth

[[Tensorflow Serving source code dive]]