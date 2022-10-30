# Recursion

I'm trying to understand recursion in my own head. Recursion means "a function whose definition includes itself" or something like that makes total sense EXCEPT it's not necessarily immediately helpful when trying to solve something.

Ideally I need some way to have actionable steps that get me a concrete way to solve these problems.

Seems like all (successful) recursive functions *must* have a way to terminate, then a way to progress.

```python
def traverseLinkedList(head: Node) -> None:
    if not head:  # terminate
        return None
    return traverseLinkedList(head.next)  # progress
```

But you can do more than that, even with the example above. Maybe we wanted to disconnect every node in a linked list. This would surely work then...?

```python
def splitLinkedList(head: Node) -> None:
    if not head:
        return None
    next_head = head.next
    head.next = None
    return splitLinkedList(next_head)
```