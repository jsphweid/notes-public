# networking megathread

Status: In progress

### practical

- [ ]  mainly I want to understand on streaming works at a high level
- [ ]  how to best build and API around bigger data files

But honestly going low level here for a bit would be helpful. I think it'd be helpful to build a networking interface in verilog

Maybe build a webserver from scratch in C?

0mq - C sockets - raw sockets?

## what geohot recomments

from [[here]]

build "TCP stack" in C

- [x]  what does this mean?
    - I think the "stack" is just the layers
    - stack in that you pop off one layer at a time to uncover what you want (like a stack data structure)

### NOTE: At this point, I don't really know how to start learning about this. I need a good entry point. Otherwise I'm just wasting time because nothing I'm reading is really sticking...

Start with the [[Network Interface Card [[(NIC)]]]] 

## Sockets

what are sockets?

When I hear socket, I think "socket ratchet" although I have no idea what socket even means.

After googling, this picture contains sockets and ratchets

![[/Untitled.png]]

Sockets are the 'female' things.

A network "socket is one endpoint of a two-way communication link between two programs running on the network."

- [ ]  how the hell does this relate to the above picture?

Sockets are bound to a port number.

So it seems like everything, even a simple http request uses sockets. It opens up a socket connection between two points and does the communication back and forth.

I've watched videos on this in the past (http1 vs. http2) but it never really clicked how it affects each layer. I think I'm getting closer...

## HTTP

- [ ]  was watching [this](https://www.youtube.com/watch?v=eesqK59rhGA) and was confused by the "connection is aborted after request is sent" or whatever (around 4:00)

## Thoughts on networking stack

I just had a thought that if you build your way up the stack to something like an http connection, you're relying on everything under the application layer to be a certain way. Such that if you decided to reinvent an application layer __, you can just change the thing on top but it still leverages everything else under it. 

### At this point...

I'm a little bit all over here. I think I have a good picture slowly forming but the lines are blurred. I find myself coming back to questions like:

- [x]  What are the alternatives to IP
    - IPX/SPX/etc. stuff we don't ever hear about basically
- [x]  Does every http connection use a socket
    - [x]  is an http connection built on a socket connection? In other words, does an http connection just a socket connection with more details on its nature/lifecycle?
        - [this](https://stackoverflow.com/questions/15108139/difference-between-socket-programming-and-http-programming) seems to answer some of these questions. It seems to indicate that 'yes' sockets are used in http — they are lower level, provided in OS part of the stack (not application layer). Although the stack thing doesn't completely resonate with me yet. The stack seems to make sense for people who already understand these things, but the whole nature of networking is not answered with the analogy, in my opinion.

### Websockets and WebRTC

websockets are built on TCP but WebRTC can do udp or tcp it seems (although it's p2p)

### Python lib

see [Socket Server page](https://github.com/python/cpython/blob/main/Lib/socketserver.py) for cpython. more confirmation of my understanding that TCP/UDP servers are built on socket servers

### TCP vs. UDP

TCP - SSH/HTTP/etc.

UDP - often Game servers / [DNS](https://stackoverflow.com/a/40063433/4918389) / VoIP

### Connections

What are connections?

What about connectionless communication?

- "messages can be sent to another point without prior arrangement" - [here](https://en.wikipedia.org/wiki/Connectionless_communication)
- IP is actually connectionless — the "conversation" is built on protocols higher

In Python lib for socketstream, SOCK_STREAM=TCP/connection whereas SOCK_DGRAM=UDP/connectionless

- this seems to be what [others](https://docs.oracle.com/cd/E19455-01/806-1017/sockets-4/index.html) represent it as, [also](https://stackoverflow.com/a/10810040/4918389)

### Need to go deeper

I see that UDP/TCP servers are built on top of these socket servers

- [ ]  where are the formalized connections taking place in the config for these socket servers (for TCP, for example)
- [ ]  what are these socket servers built on?
    - `sys/socket.h` in POSIX systems (mac/linux/etc.)
        - exists as part of C POSIX Library (which is a superset of C standard lib)
        - [this is the linux implementation (pretty sure)](https://github.com/torvalds/linux/blob/master/net/socket.c)
            - [ ]  where is the `socket` function actually defined in that file though... C is confusing
        - `socket()` "creates an endpoint for communication and returns a file descriptor that refers to that endpoint"
            - [ ]  what is an "endpoint" for communication?
            - [x]  what is a file descriptor
                - handle for a file/socket (remember in UNIX-land, everything is a file)
                - have non-negative int values typically (negative means "no value" or some errors)
                - see [[ Everything is a file  - UNIX]] for more details...
                - it's probably just 'something the OS keeps track of'
    - probably "files"
- `int sockfd = socket(domain, type, protocol)`
    - sockfd → file descriptor returned from the syscall
    - domain - "communication domain" - protocol family which will be used for communication (defined in sys/socket.h)
        - common ones are like `AF_INET6` (i.e. IPv6 protocol)
    - type - "communication type" - specifies the "semantics"
        - probably `SOCK_STREAM` (TCP) or `SOCK_DGRAM` (UDP)
    - protocol - "Protocol value for Internet Protocol(IP), which is 0"
        - [ ]  on a surface level, wouldn't we need domain to be IP for this definition to make sense... maybe there is a better definition
    - [ ]  how does all this stuff work under the hood? *all this stuff seems implemented in the OS and you just kind of connect things together... but it begs the question... how is it implemented in the OS —* for example, you can see [here](https://man7.org/linux/man-pages/man7/ipv6.7.html) that linux implements IPv6
- binding - i.e., hooking it up to something
    - usually bound to address and port
    - also called "assigning a name" to the socket
    - typically a local address is used for SOCK_STREAM to receive connections
        - [ ]  I know that's most of the usage, but what else could you do with this thing...?
    - in C, you [don't even use](https://stackoverflow.com/a/22951328/4918389) `sockaddr` , what kind of weird BS is this... you have to create a `sockaddr_in` and [rebind it](https://stackoverflow.com/a/49456508/4918389) to a `sockaddr`
- listening - `int listen(int sockfd, int backlog);` marks socket as passive socket, i.e. one that will wait for new connection requests using accept
    - sockfd, the sockfd in question (obviously must be a valid socket)
    - backlog - "max length of queue of pending connections sockfd may grow"
        - [x]  how *exactly* does that work? like what does the number include because it's slightly ambiguous from that definition...
            - is the number the max number of connections?
            - or maybe the maximum number in a queue....?
            - or queue + connections, so if there are 5 connected, and 4 queued, and the max is 9, then a new attempted connection would be outright rejected instead of going in the queue
            - So [this answer](https://stackoverflow.com/questions/10002868/what-value-of-backlog-should-i-use) seems to indicate that it's just the size of the queue, which honestly is a literal interpretation of the definition, so 👏 linux docs
        - this is where `ECONNREFUSED` comes from!??! wow
- accept - waits until an item is available to pull off the queue
    - [ ]  how does it wait
    - first arg points to the place in the file where the item can be read
        - [ ]  is that right?
- [x]  what is `char buffer[1024] = {0};`
    - zeros out the contents of buffer... if you do not do this, you will have random bytes in your buffer... sometimes it actually makes sense
- [x]  why `htons`
    - network byte order may be different from what's used on the host
    - arm/x86 use little-endian, but networking is big endian, so things have to be converted...

### trying to understand sockets/files/etc. from a different angle

it seems that when you create a socket, it returns a file descriptor.

that file descriptor is locatable (on linux) under `/proc/{pid}/fd/{fd}`

![[/Untitled 1.png]]

so NOTE: **if you're in another process, it won't be able to find that file descriptor**

every time you `accept` it opens up a new socket! for example, if you run 3 different processes connecting to the socket and sending messages, it looks like this afterwards

![[/Untitled 2.png]]

# Where I'm at and what I'd like to understand

### Where I'm at

so bytes come in to the NIC and the OS does a fair amount of management in this layer. If you have a socket and it's bound to the NIC somehow (port/address?), then connections can be made on that socket, each of which generates another file descriptor (in addition to the base file descriptor). The file descriptors are just handles to the stream of bytes that come in.

### What I need still

- [ ]  how does the OS interact with the NIC?
- [ ]  how do stream of bytes come in to the NIC — how organized are they? how do you know when one starts/ends? are they intermixed?
- [x]  how do socket connections different from other connections (like HTTP connections)? I assume HTTP connections are built on top of socket connections, there is just more protocol to follow?
    - assumption is basically correct
- [x]  what's the lifecycle of socket connections
    - the original socket listens for new connections. Once a connection is accepted, a new socket/file descriptor is made. It stays open until the server closes it. The original one is passive. The others are active.
- [ ]  how does `domain` `type` `protocol` arguments affect behavior?
- [ ]  I wish you could see /proc/pid/fd/3 live in action to see what goes on inside those things.... like are they just buffers of memory that temporarily store data until you read it?
- [ ]  what happens when you call these functions like `socket` `accept` etc. like what is their implementation

interesting perspective here [https://stackoverflow.com/a/24877210/4918389](https://stackoverflow.com/a/24877210/4918389)

- server accepts connections in a loop, but actual handling is done in another thread or by some async means
    - [ ]  need to learn more about async in c or threads

# Packet Switching

packet is a small chunk of data

it's send across the network via many routers and switches

# QUIC

The web, over UDP

Many firewalls don't seem to have tools for analyzing QUIC traffic (maybe because they are designed around TCP?). So some people don't like it.

Exploring [this python lib](https://github.com/aiortc/aioquic), but there are pieces of a real https missing. I ran it 

[[Exploring a Request with wireshark]]

# ACK