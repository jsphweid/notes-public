# Exploring a Request with wireshark

I went to [http://laughtears.com](http://laughtears.com) and captured the activity.

[[output.pcapng]]

filter = `ip.addr == 13.226.23.15`

It makes a lot of requests is the first thing I notice. But a lot of this seems to be TCP traffic. The HTTP traffic is the stuff that you'd see in chrome dev tools networking tab. 

![[/Untitled.png]]

Note that the latency between these servers is 11.5 ms. Direct line of sight latency is 1.7ms. That is something that would be interesting to explore.

### First probe

- [ ]  what are all these TCP Acknowledge requests really doing... what are they 'acking'...?
    - Looking at one of the HTTP requests, it appears that the TCP lines are "segments"
        - for example, 1 http frame on there is 810 bytes, but it reassembles into 11,236 bytes, de-chunks to 10,720 bytes, then uncompresses the gzip to 38,347 bytes
            - [ ]  what does the HTTP entry even mean?
            - [ ]  how is it known which chunks fit together in what order?
            

### DNS probe

- [x]  just search "dns" and see the query/response. It's pretty simple because it seems fairly 1:1
    - part of a DNS response might be
    
    ![[/Untitled 1.png]]
    
    Notice how `13.226.23.15`, the address it will later be communicating with is in the byte stream `0D E2 17 0F`
    
    That query takes a whole 45ms! Damn, that's a lot of time
    

### More Info

from [here](https://www.youtube.com/watch?v=7CYpjf19GkA), the "stream index" sort of refers to the conversation that's going on (because there might be multiple)

- [ ]  TODO: get more actual detail on this

SYN - "Synchronize" - request for a connection, THIS IS TCP PROTOCOL

- you send SYN, they send SYN ACK, then you send ACK finally (I guess acknowledging the acknowledgement?)

![[/Untitled 2.png]]

- sends sequence number that segments should start with
    - sequence seems to jump up by number of bytes in *the content* (not the total bytes of the frame)
    - wireshark displays it as 0 and increments from there, neglecting the actual values but preserving the relative values
        
        ![[/Untitled 3.png]]
        
- [x]  what about:
    - [x]  ECN
    - some way that routers and endpoints signal impending congestion and can slow down the flow of packets in advance
    - [x]  CWR
    - "congestion window reduced" - acknowledges "congestion-indication echoing was received"
        - [x]  what does that mean?
        - apparently according to [here](https://osqa-ask.wireshark.org/questions/57120/syn-ecn-cwr-packet-rst-packet/), in the context of a handshake, it's simply exists to inform that the sender is capable of handling such mechanisms
    - 
- [ ]  what happens if you just keep sending SYNs, can you ddos someone this way?
    - [ ]  side: mimic an SYN and send it to a server, see what they send back
    
    [[What is Joseph Working On/first principles/networking megathread/Exploring a Request with wireshark/DNS in C]]
    
    - seems like this can happen in a normal circumstance... like why the hell at some point does the client start sending a bunch SYNs
    
    ![[/Untitled 4.png]]
    

Some of them have multiple TLAs, why...