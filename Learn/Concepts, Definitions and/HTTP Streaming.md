# HTTP Streaming

Right now, I'm a bit confused on what streaming is.

### initial thoughts

Obviously, at a lower level, all data is transferred over frames/packets that are very small in size (max 1500 bytes or so). Even on the file system, everything is streaming in a way; everything is just a byte stream. So it may be a bit of a misnomer. When you don't "stream a file" it means you don't start processing it until the whole thing is in memory. Streaming really seems to refer to buffering that happens, which allows information to be dealt with before it is fully received.

### learning

[reading this](https://gist.github.com/CMCDragonkai/6bfade6431e9ffb7fe88) for some reason

mentions ["online algorithm"](https://en.wikipedia.org/wiki/Online_algorithm) a term I like because I think it pretty much encapsulates a concept that is familiar to me

also this:

```
The first thing to understand is that HTTP streaming involves streaming 
within a single HTTP transaction. In a larger context, each HTTP transaction 
itself represents an event as part of a larger event stream. This reveals 
to us that the concepts of "streaming" is a context-specific concept, it's 
relative to what we consider the "stream" to be.
```

In other words it's very context dependent since everything is a stream anyways.

HTTP Streaming ≠ Websockets - websockets is a different protocol entirely (but also uses TCP)

involves streaming within a *single* HTTP Transaction

- [ ]  what *exactly* is an HTTP transaction?
    - according to [this](https://www.cs.cmu.edu/~aist/www_paper/transaction.html), which is very old, it seems to contain Connection, Request, Response, Close
    
    is this an example?
    
    ![Untitled](Learn/Concepts,%20Definitions%20and/HTTP%20Streaming/Untitled.png)
    
    - I feel like the concept of transaction vs. connection overlap to the point of it being hard to distinguish
    - 
    

### experiments

I made a small file and served it over http, only buffering 32 bytes at a time.

However, inspecting the wireshark logs, it seems like it's sending more than 32 bytes at a time... but interestingly in numbers divisible by 32... (i.e. 64 or 96)

- [ ]  why is this
- often it *is* 32... is the flask lib that I'm using combining them? or some layer under that?
- interestingly, it's all being received as 1 chunk on the other end... I wonder if I can configure it to be less?
- [this answer on SO](https://stackoverflow.com/a/55035292/4918389) seems to make a bit of sense, basically you can predict what the network is going to do exactly...
    - [ ]  why do you get chunks larger than 1500 if that's the MTU (Maximum Transmission Size)
        - may have something to do with with me running on localhost? not going over ethernet? probably, [see this](https://stackoverflow.com/a/52581065/4918389)
        - even running the same request through insomnia multiple times yields stuff like:
        
        ![Untitled](Learn/Concepts,%20Definitions%20and/HTTP%20Streaming/Untitled%201.png)
        
        ![Untitled](Learn/Concepts,%20Definitions%20and/HTTP%20Streaming/Untitled%202.png)
        
        ![Untitled](Learn/Concepts,%20Definitions%20and/HTTP%20Streaming/Untitled%203.png)
        
- [ ]  I wonder if lower layer protocols do the same?
- [ ]  also, why is there no `Content-Length` or `Transfer-Encoding` header?

### more reading

Reading on in hopes that there is more information...

says "Each chunk starts with its byte length expressed as a hexadecimal number" but that doesn't seem to be the case in wireshark... maybe it's not talking about raw byte information?

It talks a lot about buffering concerns, like how it has to be considered at each stack. And often you don't have control over buffers in between client and server (proxy buffers that your ISP uses, for example).

# Streaming vs. Chunking

what is the difference? My initial impression is that a stream of bytes, a byte is a chunk in a way.. but maybe if the chunk is large than a byte, it's considered chunking and not streaming?