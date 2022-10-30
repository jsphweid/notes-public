# Network Interface Card (NIC)

Network Interface Card (NIC) - actual hardware device

how NIC works ([https://www.youtube.com/watch?v=QHoW3GEWLD8](https://www.youtube.com/watch?v=QHoW3GEWLD8))

- bits comes in through wire
    - bits are formatted into a frame
    - CRC is calculated and compared with the CRC in frame trailer
        - [x]  what's a freaking CRC?
            - it's just some algorithm that checks the thing for data corruption (like a hash/checksum)
    - from/to mac address is stripped after checking to make sure it's at the correct place
        - I'm guessing this is really useful if connected to a hub, since there's lots of noise that may be irrelevant to any given NIC, but maybe it could happen anyways
        - if in promiscuous mode, then frames with irrelevant MAC addresses ARE KEPT, not discarded
            - [ ]  traffic on a hub should make sense for this, but a switch sends to a specific machine, not all machines. Therefore how does sniffing work when a switch is present?
                - a "managed" switch probably has special settings that allow duplicating of data and can stream them out another physical port (there are more legitimate reasons to monitor traffic than sniffing)
                - with unmanaged switches (probably most switches), you can use ARP spoofing. I don't [understand this](https://landetective.com/products/internet-monitor/manual/traffic-analysis.html) very well but it seems like you're pretending to be the router by responding to general queries that a computer emits when it's trying to make requests outside
    - all that is left is the data and source/dest IP address
        - I'm guessing if the frame has reached the correct MAC, from a hardware (and software) perspective we don't need that information anymore
    - what is left is called a packet
- need to send stuff
    - have a packet
    - add source/dest MAC address
        - [x]  how does the NIC know what those are?
            - [it doesn't?](https://www.quora.com/How-does-a-NIC-knows-the-destination-MAC-address-when-creates-the-MAC-header)
                - so it knows the ultimate IP and it knows the next MAC to get there. If we're talking about the NIC on your computer, it probably means the MAC of your router. The router only knows the MAC of the ISP. That makes somewhat sense
                - MAC is a physical address. IP is a logic address
                - IP is like a mailing address. MAC is like who you are. It takes both to get the message to the correct person. I guess you could just use MAC but it's very inefficient.
                - [x]  How does the router know which place to forward information coming in.
                    - port forwarding forwards arbitrary traffic I think
                    - else, when a request goes out through the router from a computer, the router must keep *some type of info* so it knows where to send it back to
    - add the CRC
    - send it out as bits
- [ ]  what's the basic protocol that drives this?
    
    

So frames are just about the lowest construct. And the frame becomes a packet after the NIC is done with it. This is starting to make sense with the layers...

![[/Untitled.png]]%209f41bfbb3b52441eae0b9b5c5632014e/Untitled.png)