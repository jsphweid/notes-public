# investigate the best way to run BE

Status: Completed

- maybe use one of my rigs at home?
    - if gaming machine, maybe the docker container can be run on windows and play games at the same time on monday evenings
- run tensorflow serving on a cloud GPU
    - gonna be expensive probably
    - how much?
- run tensorflow serving on a t2 micro for now
    - less expensive, less performant... but at least mirrors what I'd eventually want to do (separate container for models)

probably shouldn't do this until we know if we're keeping graphql or not

Probably should run these in a k8s cluster for now. It's probably not worth make adjustments for serverless. Plus if we wanted to run at edge some day, k8s probably the way to go as it simply keeps everything together. Although edge makes less sense if we have to involve s3 for example (for outputs).