# Python List Primer

list indexing works like you'd expect:

```python
[1, 2, 3][0]   # 1
[1, 2, 3][1]   # 2
[1, 2, 3][11]  # throws exception
```

but it can also do cool things like

```python
[1, 2, 3, 4, 5][-1]   # 5
[1, 2, 3, 4, 5][-2]   # 4
[1, 2, 3, 4, 5][-22]  # throws exception
```

you can also get slices of a list

```python
[1, 2, 3, 4, 5][0:2]   # [1, 2]
[1, 2, 3, 4, 5][2:4]   # [3, 4]
[1, 2, 3, 4, 5][1:-1]  # [2, 3, 4]
[1, 2, 3, 4, 5][1:]    # [2, 3, 4, 5]
[1, 2, 3, 4, 5][:2]    # [1, 2]
[1, 2, 3, 4, 5][:-1]   # [1, 2, 3, 4]
[1, 2, 3, 4, 5][:0]    # []
```

you can also add parity

```python
["a", "b", "c", "d", "e", "f"][0:4:2]     # ["a", "c"]
["a", "b", "c", "d", "e", "f"][:4:2]      # ["a", "c"]
["a", "b", "c", "d", "e", "f"][0::2]      # ["a", "c", "e"]
["a", "b", "c", "d", "e", "f"][::2]       # ["a", "c", "e"]
["a", "b", "c", "d", "e", "f"][::-2]      # ["f", "d", "b"]
["a", "b", "c", "d", "e", "f"][::-1]      # ["f", "e", "d", "c", "b", "a"]
["a", "b", "c", "d", "e", "f"][-2:-6:-2]  # ["e", "c"]
["a", "b", "c", "d", "e", "f"][-2:-7:-2]  # ["e", "c", "a"]
["a", "b", "c", "d", "e", "f"][-2:-9:-2]  # ["e", "c", "a"]
["a", "b", "c", "d", "e", "f"][-1:2:-1]   # ["f", "e", "d"]
```

It gets a little weird with negative steps but you just have to remember the format:

[start_index_inclusive, end_index_exclusive, step]

For example: `"abcdefghij"[2::-1]`starts at index 2 inclusive, goes to end by -1 steps (so end is beginning). This yields `"cba"`. If we made it `[2:0:-1]` we'd get "cb" because 0 index stop is exclusive.