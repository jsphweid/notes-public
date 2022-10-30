# zip

doesn’t use extra space unless you sort it or convert it to a list...

```
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     1  812.652 MiB  812.652 MiB           1   @profile
     2                                         def my_func(lst1, lst2):
     3  888.953 MiB   76.301 MiB           1       w = list(lst1)
     4  965.250 MiB   76.297 MiB           1       a = list(lst2)
     5 1042.000 MiB   76.750 MiB           1       sorted(zip(lst1, lst2))

~ - jsphweid@gmail.com $ python -m memory_profiler ~/Desktop/dumb.py
Filename: /Users/joseph.weidinger/Desktop/dumb.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     1  812.613 MiB  812.613 MiB           1   @profile
     2                                         def my_func(lst1, lst2):
     3  888.914 MiB   76.301 MiB           1       w = list(lst1)
     4  965.211 MiB   76.297 MiB           1       a = list(lst2)
     5  965.211 MiB    0.000 MiB           1       zip(lst1, lst2)
```