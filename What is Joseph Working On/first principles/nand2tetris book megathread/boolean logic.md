# boolean logic

FPGA is like an arduino?

simple boolean functions can have truth tables where literally every possibility is pre-calculated

### canonical forms

it's like rephrasing the formula, or putting it in a form that describes how to get a 1 result

looking at here too: [https://www.youtube.com/watch?v=Gjsfx-o7nnQ](https://www.youtube.com/watch?v=Gjsfx-o7nnQ)

- sum of products
    - make truth table
    - look for result=1
    - for each, put into form, then `or` everything
- product of sums
    - look for result=0
    - for each, put into form, then `and` everything
    

### exercise: make and/or from nand

I figured this out on my own. I think this is all legal...?

[[nand.py]]

![[boolean logic 52aad1b68305476aa8c812a2ed8f7a58 image.jpg]]

Note... notice home much like [[]]%20545245a8c5d241a3a8485ae8e0652027.csv) is in a sense

The only thing I strugged on was the multiplexer because I didn't grasp that you could have a not go to one side and the inverse go to the other...