# node

a3627c06f8248b8c7a1580f2985f5b566fc12672

not sure if it can be built seeing as how it's 12 years old

when you build, you're building the node binary

uses waf build automation tool, this is opposed to cmake?

deps

- http_parser
    - made by ryan in pure C (but heavily inspired by [this](https://en.wikipedia.org/wiki/Mongrel_(web_server)))
- libeio
- libev
    - high performance [[Event Loop]]
        - so from [this](https://stackoverflow.com/questions/50115031/does-v8-have-an-event-loop) and [that](https://stackoverflow.com/questions/49811043/relationship-between-event-loop-libuv-and-v8-engine) and without reading v8 source, v8 provides a default event loop but allows "embedders" to override it
    - looks like node probably now uses libuv, not libev. It seems they both can solve the same problem but in [very different ways](https://gist.github.com/andreybolonin/2413da76f088e2c5ab04df53f07659ea)
- liboi - "OpenCL Interferometry Library" whatever that means. honestly I have no immediate idea why this would be used in node
- v8