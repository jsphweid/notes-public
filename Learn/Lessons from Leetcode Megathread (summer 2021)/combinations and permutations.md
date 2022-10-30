# combinations and permutations

# Combinations

[[a,b],[c,d]] →[ac, ad, bc, bd]

## Ways to do it

### mixed base counting

my first thought was that this seems oddly similar to counting if we think in terms of the indices...

00, 01, 10, 11. The problem is when you have an item in that list that's more or less than 2... it becomes less obvious. It's essentially counting but with mixed bases... In regular base counting you can simply check how many 1000s / 100s / 10s / 1s etc. are in a number (for decimal). But in multiple bases it's a little odd (to me at least right now). If you have a 3 'digit' number whose bases are 2,3,2, you're really asking how many 6's are there, then how many 2's are there, then how many 1's. To get these numbers, you take the max possibilities (2*3*2⇒12) and divide by 2, then 3, then 2 again. Once you are able to count, you can iterate over all 12, produce the number for each (up to 1-2-1) which corresponds to the indices that you can use to get each combination.

# Permutations

abc → abc, acb, bca, bac, cab, cba

## Ways to do it

### first

Aaron had an interesting idea, to start with a letter, say 'a'. then take the next letter and generate more results on each side... so 'ab' and 'ba', then do the same for the rest of the letters, each time using the previous result... so 'ab' becomes 'cab', 'acb', 'abc' and 'ba' becomes 'cba', 'bca', 'bac'