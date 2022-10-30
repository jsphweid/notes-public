# nodejs/python streams

I'm really trying to understand here what exactly a stream is

- [x]  is this "stream" specific to nodejs?
    - dumb obviously
- [ ]  how is it different from sockets / connections?
    - more than likely a stream can use a socket connection, but maybe it's just a higher level protocol?
    - I think streams are more generic concept. They can be applied to files / file-like objects / i.e. stream of bytes.

# Node

### reading [the official docs](https://nodejs.org/api/stream.html)

seems like a lot of things use streams — possibly without us knowing — like an HTTP request or process.stdout

unless in object mode (maybe more on that later), all streams operate on strings and buffers

Streams are deceptively tricky. I don't know what I imagine in my head at this point, but I think maybe it's that all streams are passthroughs, which is definitely not the case. I just imagine a stream is something you can read from and write to, but that's not the case?

from [here](https://nodejs.dev/learn/nodejs-streams):

Readable Stream

- you can pipe from, but not pipe into BUT you can still somehow "push data into it" - I guess pushing and piping aren't the same thing or even related? that might be where my misunderstanding is

Writable Stream

- stream you can can *pipe* into but not pipe from (you can send data but not receive from it)

Duplex Stream

- you can do both

Transform Stream

- like duplex, but output is transform of its input
    - [ ]  is transform like "transformation"? or map?

# Experiments with buffering files

When buffering files, the size of the buffer matters quite a bit for extremes...

```python
def experiment(buf_size):
  with open("data.txt", "rb") as f:
    buff = io.BufferedReader(f)
    t = time.time()
    num_buffers = 0
    while True:
      b = buff.read(buf_size)
      if not b:
        break
      num_buffers += 1
    print(f"done, with buf_size={buf_size}, read {num_buffers} buffers in {time.time() - t} seconds") # 4.398540019989014

for item in [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]:
  experiment(item)

"""
RESULTS:
done, with buf_size=10, read 107374183 buffers in 21.909841060638428 seconds                  │
done, with buf_size=100, read 10737419 buffers in 2.366001844406128 seconds                   │
done, with buf_size=1000, read 1073742 buffers in 0.7283079624176025 seconds                  │
done, with buf_size=10000, read 107375 buffers in 0.4257369041442871 seconds                  │
done, with buf_size=100000, read 10738 buffers in 0.19373178482055664 seconds                 │
done, with buf_size=1000000, read 1074 buffers in 0.16433310508728027 seconds                 │
done, with buf_size=10000000, read 108 buffers in 0.2177112102508545 seconds                  │
done, with buf_size=100000000, read 11 buffers in 0.478971004486084 seconds                   │
done, with buf_size=1000000000, read 2 buffers in 0.9776909351348877 seconds

NOTE: non-buffering took around 0.6 seconds
"""
```

Really small buffers make it take quite a while longer. But even very large buffers take a while too. This can only mean that while buffers make things go faster there is some overhead to creating them. For really small buffers, this overhead really takes up most of the time. For very large buffers, where the buffer size is almost the same as reading the whole stream into memory, there is almost no benefit but only cost (?vague).

- [x]  learn more about how this happens
    - seems pretty much what I'd expect [explained here](https://stackoverflow.com/a/2821693/4918389)