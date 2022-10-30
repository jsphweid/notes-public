# nand...
def nand_fn(left, right):
    return not (left and right)


assert not nand_fn(1, 1)
assert nand_fn(1, 0)
assert nand_fn(0, 1)
assert nand_fn(0, 0)

# but how can we make others using only nand...


def and_fn(left, right):
    return nand_fn(nand_fn(left, right), nand_fn(left, right))


assert and_fn(1, 1)
assert not and_fn(1, 0)
assert not and_fn(0, 1)
assert not and_fn(0, 0)


def or_fn(left, right):
    return nand_fn(nand_fn(left, left), nand_fn(right, right))


assert or_fn(1, 1)
assert or_fn(1, 0)
assert or_fn(0, 1)
assert not or_fn(0, 0)
