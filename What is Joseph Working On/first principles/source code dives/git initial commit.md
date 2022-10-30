# git initial commit

not a lot of files...

trying to run `make` → get error complaining:

```
./cache.h:13:10: fatal error: 'openssl/sha.h' file not found
#include <openssl/sha.h>
         ^~~~~~~~~~~~~~~
```

- [x]  Why doesn't the make specify how to get that somehow? Or maybe it is ignored it git... but then again, did git even have gitignore back then. I'm confused.
    - I think sha-1 used to be more standard but has been deprecated by most players... you can 're-enable' like [this](https://www.anintegratedworld.com/mac-osx-fatal-error-opensslsha-h-file-not-found/)

introduced as a *directory content manager*

- it "tracks" directory contents
    - [ ]  what exactly does it mean to track?
- uses SHA-1 as a hash "mostly to guard against accidental corruption"
    
    

### Two Abstractions

- [ ]  what does it mean by "abstractions" in this context

1. Object Database
    - initial thought: the history as it is stored in the .git folder somewhere? (nowadays)
    - SHA1_FILE_DIRECTORY
    - content-addressable collection of objects (using SHA1)
        - multiple kinds
            - [x]  how are the kinds of objects different
                - **blob** object - binary blob of data, no attributes, "no name associations, no permission", just a blob of data
                    - [ ]  what do name associations and permissions even mean here...?
                - **tree** object - list of permission/name/blob data sorted by name, is "uniquely determined by the set contents"
                    - [ ]  does that mean the hash always points to the same details?
                    - pure data abstraction - "no history, no signatures, no verification of validity except that the contents are protected by the hash itself". You can trust the contents, but you just don't know where it came from
                        - [ ]  what makes that a "pure data abstraction" — maybe that refers to "pure data"?
                    - since tree objects is a sorted list of filename+content, you can create a diff between two trees without having to unpack two trees. just "ignore all the common parts and your diff will look right"
                        - [ ]  what does diff mean here exactly?
                    - since blob is identified by content, you can see renames easily, because the blob stayed the same
                - **changeset** object
                    - defined by
                        - tree object that it results in
                        - parent changesets that led up to that point (zero or more)
                        - comment on what happened
                    - "contents are well-defined and "safe" due to the cryptographically
                    strong signatures at all levels, but there is no reason to believe that
                    the tree is "good" or that the merge information makes sense. The
                    parents do not have to actually have any relationship with the result,
                    for example."
                        - [ ]  not sure what this means
                    - I'm not 100% sure what a changeset *exactly* is yet
                        - seems like a node that has parent node... but it's not a 'commit' or 'merge commit' or anything specifically (maybe it's a superset?)
                    - since the SHA1 is produced from all the contents of its parents, it affixes the history
    - objects may refer to other objects, so you can create hierarchy
    - "objects are deflated with zlib and start off with a tag of their type and size information of the data"
        - [ ]  what does "start off" mean? like it's a part of the file/object name?
            - object inflates to a stream of bytes that form the sequence
                1. ascii tag without space
                    - [ ]  what is an "ascii tag"
                2. space
                3. ascii decimal size
                4. byte\0
                5. binary object data
            - [ ]  would be nice to have an example
    - hash is always of the compressed object, not the original one
2. Current Directory Cache
    - initial thought: some state of changes unstaged/staged (nowadays) stored somewhere in .git folder?
    - ACTUAL: simple binary file that "contains efficient representation of a virtual directory content at some random time" TODO: what is meant by *random* here?
    - simple array that associates names, dates, permissions, content together
    - ordered by name, which are unique at any point in time
    - has no longer term meaning, does not even need to be consistent with the current directory contents
    - can regenerate the full state it caches, not just directory structure but actual data too (through blob object)
        - there is a clear and unambiguous one-way mapping from a current directory cache to a "tree object". at any point in time CDC maps to exactly one tree object
        - has efficient methods for finding inconsistencies between that cached state
    - [ ]  is the CDC a commit?!? or it actually describes it as being a "work in progress" towards a tree commit
    

### playing around with CLI

makes 7 command line tools

1. cat-file
2. commit-tree
3. init-db
    - creates `.dircache` (original .git folder, basically)
4. read-tree
5. show-diff
6. update-cache
    - creates `.dircache/index` although the next time it is ran, I just get seg fault, this is probably because I didn't compile it correctly (it compiled with warnings, after I added two additional compile flags)
7. write-tree