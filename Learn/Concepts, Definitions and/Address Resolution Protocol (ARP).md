# Address Resolution Protocol (ARP)

Resolves IP addresses to MAC address

Only exists in IPv6

Remember that the frame deals with MAC addresses. When you're talking to another computer through ping, for example, the frame already has the MAC of the destination. If you're pinging another locally computer, the dest is already the other computer's MAC address. If you try pinging something outside the network, the MAC address is the gateway/router. Obviously you don't know what the MAC is of the destination device. You probably don't even care — you're probably not interested in a specific machine anyways. That's the part of the frame that constantly gets dropped and replaced.

But again, for LANs, MAC addresses are relevant

- [ ]  Why have MAC addresses and IP address
    - according to [this answer](https://networkengineering.stackexchange.com/a/3334) you could get rid of MACs, for example, but you'd be left tied to the IP (specifically probably IPv4) protocol
        - [ ]  not really a satisfying answer though

It's broadcast... stores in a cache

- indicated by ff:ff:ff:ff:ff:ff
- dynamic entries are flushed periodically
- static - user-create association (TODO: do this)
    - do this to prevent lots of broadcast
    

examples

![[Ideas/Code Ideas/Untitled]]%2080d259e71a9248cc9a9754af8c996ba1/Untitled.png)