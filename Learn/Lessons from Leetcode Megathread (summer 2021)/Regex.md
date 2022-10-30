# Regex

watching [https://www.youtube.com/watch?v=rhzKDrUiJVk](https://www.youtube.com/watch?v=rhzKDrUiJVk)

opens with `/` and ends in `/`, flags come afterwards

flags - global (g), case insensitive (i)

- `+` - matches one or more of prev char, i.e. `e+` matches one or more `e`
- `?` - preceding char is optional
- `*` - match 0 or more
- `.` - match anything, (like wildcard?)
- `\` - escape
- `\w` - matches word character
- `\W` - matches **non**-word character (somehow a `_` is a goddamn word character)
- `\s` - matches space
- `\S` - matches **non**-space
- `\w{4,5}` - matches words between 4-5 chars long
- `[pd]imple` matches pimple or dimple
    - "character set"
- `(p|d)imple` matches pimple and dimple BUT
    - "capturing group"
    - [x]  how is this different from a character set
        - capture groups don't simply match text, but they provide some access of it
        - you can also have subgroups...
- `[b-d]ap` matches bap cap dap
- `[^b]ad` matches anything like `cad` or `sad` but **not** `bad`
    - `^` has to be at the beginning and it negates everything in it
- `^` asserts start of line and `$` is end of line like `^hello$`
- `\b` captures boundary between word and non-word
    - [x]  what the hell does that mean?
        - [x]  looks like it maybe can take the place of either $ or ^? like `u\b` can mean something ending with `u`
        - [x]  but it can also mean like spaces/punctuation?
- `$1` vs. `\1` similar in that it refers to capture group 1, but `\1` is used more from within the regex whereas `$1` is for the replace
- `.*` is a very "greedy" modifier — it'll match everything
    - `[Google](https://google.com) - [[test]]`
        - `[Google](https://google.com) - [test]` will be matched if we use `\[.*\]`
        - but putting `\[.*?\]` will make it match `[Google]` and `[test]` as intended
        

### lazy vs. greedy

happens when you have a repetition operator (like `+` or `*`)

# lookaround

kinda like anchors `^` / `$`

zero-length assertions - "zero-length" don't count in group? "assertions" - only "assert" whether a match is possible

NOTE: you're not capturing anything though (even thouggh it looks like a capture group)

### lookahead

negative - pair of parens with `?!` then your match inside `(?!something)`

positive - pair of parens with `?=` then your match `(?=something)`

### lookbehind

negative - pair of parens with `?<!` then match `(?<!something)`

positive - pair of parens with `?<=` then match `(?<=something)`

String manipulation

[[Strings]]

## python

`import re`

`re.findall` - simple groupings

`re.finditer` - like findall except each item contains more info like start/end index

- the match object `.string()` is a ref to the original! not the current matched

`re.match` - tests beginning of string

`[re.search](http://re.search)` - tests throughout a string

## Questions

why doesn't the top row match (1+) - does grouping "use up 1"?

![Untitled](Learn/Lessons%20from%20Leetcode%20Megathread%20(summer%202021)/Regex/Untitled.png)

- [x]  when do you need `r""` in python?
    - always... might even have to do rf"{some_str}"

`\1` - in capture groups, this refers to the "1st" capture group

`((.)\2*)` - this groups chars together... the \2 is because it matches the 2nd capture group (i.e. the inner one)... and don't forget that \2 counts for 1, that's why we use * (to match for 1 or more ultimately)

NOTE: findall with capture groups gets a little hairy, returns a tuple