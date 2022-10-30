# Subnet Mask

it's a bitmask that can be applied to any ip on the network

bitmask → (`0xFF && 01100011` or whatever)

### but why?

increases speed

- how?
    - reduces broadcast-oriented traffic
        - I guess because if you have 100 computer all broadcasting to each other, but then divide them onto 4 logical subnets, then each machine may only waste the broadcast time with 25 others
    - other benefits like "subnetting enables you to ensure that information remains in the subnetted network or broadcast domain" which is also good, but I don't know what it means

reduces congestion

- seems to be related to the above, broadcast packets don't go to every outlet in a switch — I guess that means the switch is aware of the subnet of each port

security

- somewhat obvious, but if you are splitting your network up, it means that certain machines won't be able to talk to other machines (on a different network). this control equates to security

### it's all about dividing network/host

an ipv4 address is 4 bytes

class A - first byte determines the network (sub network?)

class B - first to second byte determines the network

class C - first to third byte determine the network

It's kind of like phone numbers and area codes... maybe back in the day, vienna was 3037 → 6229, but then we require 422-3037 → 422-6229, then 573-422-3037 → 573-422-6229, etc.

If you have two vastly different IPs, say `10.1.1.1` and `10.2.3.4` they may or may not be on the same subnet depending on what the mask is

- if the mask is `255.0.0.0`, they are on the same subnet
- if the mask is `255.255.0.0` or `255.255.255.0`, they are NOT on the same subnet

### Physical Hardware requirements

- a switch cannot 'route' things to other subnets... you need a router for that. According to [this](https://www.quora.com/Why-do-two-computers-connected-to-the-same-switch-with-an-IP-and-Subnet-192-168-0-1-16-and-192-168-1-1-8-ping-each-other-while-being-on-different-networks) a switch routes based on hardware MAC address. Machines use ARP ()

### differences with VLAN

Hmm.. my first impression was that they are the same because a subnetwork is basically a LAN within a LAN, which is what VLAN would almost mean

### common display

you can either see it like `255.255.255.0` which is common on windows it seems or like `0xffffff00`, which I've seen on mac

I guess you can have `255.255.254.0` why not

If machines are on different networks, then the router has to make special forwarding decisions

- [x]  does the internet use a subnet mask? is that a silly question?
    - I'm guessing it operates differently as doing things like broadcast would be so incredibly expensive. maybe like each bit in an ip network is part of the mask 🤔 except last? idk lol
    - the internet is a bunch of connected networks while a subnet is within a singular network
- [ ]  it has routing tables