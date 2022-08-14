# Digital Egomania: the Self-Describing Numbers
<br><br>
## Matt
<br><br>
### """In this challenge, you have to establish if a given number is self-describing. To be self-describing, a positive number must have an even quantity of digits, because it has to be split into separated pairs of adjacent digits x and y, and each pair can be interpreted as a declaration: among the digits of the number, there are x instances of the digit equal to y.
If we take as an example the self-describing number 10123331, we can see how it has an even quantity of digits and it can be split into four pairs:
[1, 0] ➞ This pair declares that among the digits of the number there is 1 instance of 0
[1, 2] ➞ This pair declares that among the digits of the number there is 1 instance of 2
[3, 3] ➞ This pair declares that among the digits of the number there are 3 instances of 3
[3, 1] ➞ This pair declares that among the digits of the number there are 3 instances of 1
If every "declaration" represented by the pairs is true (as in the above example), then the number is self-describing.
Given a non-negative integer num, implement a function that returns True if num is a self-describing number, or False if it's not.
Pairs can be repeated (see example #2), but they have to be true in any case.
Remember to consider the totality of the digits of the number, when checking if a pair represents a true declaration (see example #3).
You can expect always valid non-negative integers as input."""
<br><br>
[czGN5qceLFWba2j6F](https://edabit.com/challenge/czGN5qceLFWba2j6F)
<br><br>
```is_self_describing(10123331) ➞ True
# See the Instructions

is_self_describing(224444) ➞ True
# Pair [2, 2] is True (two times 2 into num)
# Pair [4, 4] is True (four times 4 into num)
# Pair [4, 4] is True (same as previous)

is_self_describing(2211) ➞ False
# Pair [2, 2] is True (two times 2 into num)
# Pair [1, 1] is False! It declares: one time 1 into num...
# ...but 2211 has two instances of 1 among its digits

is_self_describing(333) ➞ False
# Odd quantity of digits, it can't be splitted
```

<br><br>
