# Lessons from Leetcode Megathread (summer 2021)

# Definitely do over

- [ ]  populating-next-right-pointers-in-each-node (just 1 more clean time)
- [ ]  [matchsticks-to-square](https://leetcode.com/problems/matchsticks-to-square/) - do it again...  (try not to use a lot of memory)
- [ ]  largest-substring-between-two-equal-characters - read the damn problem! jesus
- [ ]  surrounded-regions - major yikes
- [ ]  odd-even-jump - hard but googly
- [ ]  check-array-formation-through-concatenation - no dumb mistakes
- [ ]  gas-station
- [ ]  single-number-ii (uhh, try to get it)
- [ ]  defuse-the-bomb (should be able to nail this first time)
- [ ]  smallest-string-with-swaps - get faster with UF
- [ ]  [https://leetcode.com/problems/next-greater-element-i/](https://leetcode.com/problems/next-greater-element-i/) but do all in series
- [ ]  do a monotonic queue problem
- [ ]  product-of-array-except-self
- [ ]  maximum-repeating-substring (don’t mess up binary search)
- [ ]  minimum-insertions-to-balance-a-parentheses-string
- [ ]  removeDuplicateLetters
- [ ]  copy-list-with-random-pointer
- [ ]  print-immutable-linked-list-in-reverse (try a harder impl)
- [ ]  merge-nodes-in-between-zeros
- [ ]  count-substrings-that-differ-by-one-character (try lee’s)
- [ ]  best-time-to-buy-and-sell-stock-ii try greedy

hard on deck:

- [ ]  regular-expression-matching

# Language specific

### python

1. splitting a string into a list of chars is as easy as `list(string)` do not use `.split("")` as `split` cannot accept an empty string. Another way would be a list comprehension `[char for char in string]` learned [here](https://github.com/jsphweid/chops/blob/main/lc/answers/plus-one/2021.08.23-23.46.03.py) **+1**
2. `set("123abc")` will make `{"1", "2", "3", "a", "b", "c"}`
3. `strip()` removes all whitespace at the beginning and end of the string (it's NOT "trim")
4. best way to reverse string is `[::-1]`, not `"".join(reversed(str))`
    
    [[Python List [[Python List Primer]]
    
5. `str.count("a")`
6. there is no .lowercase() method on a string, it's `.lower()`
7. `"5".isdigit()` does what you think it does 
8. `"a".isalpha()` (also) does what you think it does
9. `"a1".isalnum()` (also) does what you think it does
10. can't concatenate string and num like `"something" + 5`
11. strings don't support index assignment! **+2**
12. `.startswith` is useful (instead of checking .index == 0 and try catching)
    1. safe with empty strings
13. `format` can come in handy, especially when printing out padded binary - 
    - `"{:08b}".format(i)`
        - [ ]  write a more in-depth article on this
14. `pop(0)` pops from the first index (although consider using a deque instead as popleft is O(1))
15. `.insert(0, var)` adds item to beginning of list (unlike `.append()` which is end) (although again, considering using a deque because it's O(1))
16. `map` and other similar functions take in a fn as a first arg and list as a second arg
17. `[5] * 3` creates `[5, 5, 5]`
    1. can't multiply sequence by non-int (`[5] * 3.0`) is not allowed
18. `mylist.index(item)` is handy
19. `.sort()` is ascending by default, you can change this with `reverse=True` argument (same with `sorted()` (since the first arg is the list you want to sort...)
20. flatten a list like `[item for items in lst for item in items]` or just write it out longways if that's too confusing
21. can't do `len(filter(etc.))`
22. `.union()` joins two sets, `.intersection()` gets the common ones
    1. NOTE: `-` `|` `&` `^` do exactly what you think they do
23. `zip` turns n lists into tuples by index, NOTE: shortest list determines length
24. you can destructure a list of n items like `head, *rest = long_list`
25. `bisect` module for easy binary search
    
    [[bisect in [[bisect in python]]
    
26. `bisect.insort` can be used to insert an item in a sorted array easily (arr, num)
27. `float('inf')` exists and is useful, can also use `from math import inf`
28. `d.items()` exists but so does `d.values()` and `d.keys()`
29. `dict.keys()` doesn't exactly return a set (so don't use methods like `.intersection()`
    1. NOTE: `a | b` works but not `a.union(b)` 🤔
30. careful with single line multivariable assignment... `l1, l2 = {}, {}` is right `l1 = l2 = {}` is wrong (l1 and l2 will BOTH point to the *same* dict)
31. `from fractions import Fraction` `Fraction(1,4)+Fraction(1,4)` ⇒ `1/2`
32. dict values aren't scriptable... i.e. `d.values()[0]` isn't a thing (same with keys — probably because it's set-like)
33. `math.log(1000, 10)` yields `2.9999999999999996` ... use `math.log10`
34. `divmod` is simple way of integer dividing + carry, i.e. `divmod(5, 2)` ⇒ `(2, 1)`
    1. quotient and remainder
35. you can leverae secondary sorts by returning a tuple in the sort function
    1. can also use in in max/min to save a secondary value without having to maintain multiple variables
36. `issubset` you can think like `a.issubset(b)` a is subset OF b
37. use `Counter` it's a shortcut to many problem answers, has cool methods like `most_common`
38. `while` `else`
39. `discard` safely removes item from set, whereas `remove` will throw error if not in there

### MORE

1. Counter.elements() → can be converted back to list with list(), omits if some values have moved to 0 since taking count
2. `zip` doesn’t take up more memory unless you wrap it in list() or sorted() or something
3. `defaultdict` takes in a function that returns a value more specifically 
    - `default_factory` - is what it’s called
    - `treeid.default_factory = treeid.__len__` - uses len function to essentially get a unique ID for that unique item
4. `SortedDict` (not OrderedDict) is very useful `from sortedcontainers import SortedDict`
    - `pop()` is used to remove a key (same as normal dict...) or `del d[key]`
    - `peekitem(i)` can easily get `(0)` or `(-1)` i.e. first or last real easily
    - think it works just by keeping a sorted list on keys and doing binary search a lot
5. `math.gcd` exists.. LCM can be gotten from that `abs(a*b) // math.gcd(a, b)`
6. `[[]] * 5` makes `[[], [], [], [], []]`
7. somehow I keep making goofs... iterating over items of dict `d` is `d.items()` 
8. `ord` and `chr`
9. `Counter` has an `update` method to make it easy to count more than one thing
10. in `enumerate` `start` just changes the index start… it’s not an offset

# Mathy stuff

[[Logarithms]]

[[Shoelace [[Shoelace Formula]]

[[combinations and [[combinations and permutations]]

- completing the square (`k**2 + k - 2n ≤ 0` get `k` on one side...)
- 0 and 1 are not prime by definition

[[slope intercept [[slope intercept form]]

- `1//2` is 0 but `-1//2` is -1...

# General

- integer division always "rounds down" (discards decimals)
- need more confidence around recursion
    
    [[Recursion]]
    
- I don't always consider edge cases
- I probably need to be more regimented about "whiteboarding" even if only in sublime
- modulo operator makes a decent hashing function

[[Dynamic [[Dynamic Programming]]

- it's not fair to describe`O(n^2)` as exponential, but squared since that exponent is constant. exponential would be something like `n^m` (you might say quadratic)

[[Regex]]

[[Trie]]

[[Learn/Concepts, Definitions and/Graphs]]

[[0 1 Knapsack [[0 1 Knapsack Problem]]

# Questions

- [x]  when can a recursive function not be used? seems in `maximum-depth-of-binary-tree` that recursive functions can't be used because there are not enough state variables
    - [x]  Jesse P helped me realize this was possible and once I thought about it from a slightly different perspective I was able to solve it
- [ ]  is traversing a binary tree layer by layer starting at the top with a queue an appropriate solution?
    - the problem is we have to enhance the data structure to also store the depth if we need it
- [ ]  threads vs. cores vs. ??
    
    [[cores vs. threads vs. [[cores vs threads vs processes]]
    

## How to improve my flow

- [ ]  incorporate routines in the templates?
- [ ]  specify how I should solve it more (out loud, in my head, on a whiteboard, verbalize everything, by writing everything out in a document)

## Things I really need to work on

- [x]  talking about complexity
    - [x]  bake complexity into the terminal when starting a new problem
- [x]  dynamic programming
    - [x]  watch some more videos about dynamic programming
    - [ ]  there were two big concepts, I only did one (recursion with caching)
- [x]  redoing older problems
    - [x]  develop algorithm on `./lc` that recycles older problems
- [x]  working on some mediums
    - [ ]  mix them into the equation from time to time
- [ ]  learn the efficiencies of sets
- [ ]  how to deal with brute force solutions that I don't understand how to create (for example `distribute-candies`)
- [ ]  graphs
- [ ]  complexity analysis of regular expressions
- [ ]  sometimes I'll get in a really bad funk where I have a series of embarrassing failures that stem from a basic error like overriding a variable or not getting a range/slice right — but I'll keep overlooking it and it's just really bad
- [ ]  understanding [prefix state map](https://liuzhenglaichn.gitbook.io/algorithm/prefix-state-map), encountered in [this problem](https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/1515501/C%2B%2B-Prefix-State-Map-Two-Pointers-Sliding-Window)
- [ ]  if I have the slightest feeling it may not work for all cases, figure out the edge cases it doesn't work for besides just yoloing a submission **+1**
- [ ]  breadth first search with recursion
- [ ]  always talk about the big O but also what each one means
- [ ]  morris preorder solution [https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/)
- [ ]  priority queue
- [ ]  heap data structure
    - binary tree where the parent node is always less than or equal to children?
    - [https://leetcode.com/problems/last-stone-weight/discuss/294956/JavaC%2B%2BPython-Priority-Queue](https://leetcode.com/problems/last-stone-weight/discuss/294956/JavaC%2B%2BPython-Priority-Queue)

[[priority [[priority queue]]

- [ ]  thinking and talking
- [ ]  [https://leetcode.com/problems/height-checker/discuss/300472/Java-0ms-O(n)-solution-no-need-to-sort](https://leetcode.com/problems/height-checker/discuss/300472/Java-0ms-O(n)-solution-no-need-to-sort) how does this work so well?
- [ ]  [disjoint set](https://leetcode.com/problems/regions-cut-by-slashes/discuss/205680/JavaC%2B%2BPython-Split-4-parts-and-Union-Find) - how tf do you solve this, and [this](https://leetcode.com/problems/connecting-cities-with-minimum-cost/solution/)
    
    [[disjoint [[disjoint sets]]
    

[[deque]]

[[zip]]

[[randomizing an array and [[randomizing an array and Fisher-Yates]]

[kth largest element - quick select - O(n) solution](https://leetcode.com/problems/kth-largest-element-in-an-array/discuss?currentPage=1&orderBy=most_votes&query=)

quick select — same as above!

- [ ]  review order of operations (see count-odd-numbers-in-an-interval-range
- [ ]  topological sorts, finding cycles in directed and undirected graphs

## From Clay

- 5 step optimization (cracking the coding interview)

## What I've learned from wasting time on hard problems

- [https://leetcode.com/problems/next-permutation/](https://leetcode.com/problems/next-permutation/) took me around 3-4 hours... but I feel more confident in general after solving it. I can solve anything I put my mind to. In this problem, it was rather easy to see what needed to be done but hard to imagine programming it. I had to ask myself very deeply "How do I know how to do this" and in pondering that was able to find the correct path forward (eventually)

# Reviewing

- [ ]  the practice I needed, easy just in time - [https://youtu.be/CtQCxc8xYeY?t=9021](https://youtu.be/CtQCxc8xYeY?t=9021)
- [ ]  seems like I often start something and just continue without understanding it
    - ignore clues in plain sight

# Video ideas

- [ ]  shortest-path-to-get-food - medium, i did pretty well on it, can explain it easily
    - use whiteboard video a bit
- [ ]  asteroid-collision - medium, got right after an hour though, a few TLE’s, but optimized it too
- [ ]  stepping numbers - decent lessons and I did come up with a good solution by myself, then optimized according to what is in the discussions
- [ ]  number-of-students-doing-homework-at-a-given-time - stupidly easy easy
- [ ]  edit-distance - HARD was able to do by myself, but took like 2 hours
- [ ]  divide chocolate - HARD question but not done - Jason recommended
- [ ]  number-of-matching-subsequences

Video review checklist

- [ ]  voice overs sound different?
- [ ]  voice overs have black and white?
- [ ]  nothing clipping?
- [ ]  beginning and end have good amount of time
- [ ]  music where appropriate?