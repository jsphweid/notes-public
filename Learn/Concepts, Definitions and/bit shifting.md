# bit shifting

shift right but not letting things fall over the edge... what is the significance of this sequence?

- it kind of halves
- they are all divisible by 3

1001 (9) → 1100 (12) → 0110 (6) → 0011 (3)

The other way is just the opposite (a pointless statement)

# bit hacks

tricks, sometimes with great speed improvement

### parity check

`x ⇒ x % 2` could be better via `x => x & 1`

it uses fewer instructions