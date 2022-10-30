# Modulus

it gets the remainder, but the applications are much wider than this

a primitive application is checking odd/even (`i % 2 == 0` means even for example, although this can be more efficiently done by checking the last bit)

other ideas on this: when you add two int32s and expect the result to be int32, there is a certain max num that can result... it's as if bits are being left off, you can implement this limit like `big_num % (2^32)`

- or with smaller numbers you can demonstrate this. For example `2+3=5` but say we have only 0-8 `2+3=5%8` still works. but if we do `4+5=9%8` we start to run over