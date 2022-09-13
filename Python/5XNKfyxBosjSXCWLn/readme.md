# The Humble Sequence of the Modest Numbers
<br><br>
## Matt
<br><br>
### """In this challenge, you have to establish if a positive integer is a Modest number, accordingly to the following algorithm:
Divide the number into two left and right partitions.
For each combination of left and right parts, you have to check if a condition is true: the remainder of the number divided by the right part is equal to the left part.
If at least a combination of two parts satisfies the above condition, the number is Modest, otherwise, it's not.
Given an integer num, implement a function that returns True if num is a Modest number, or False if it's not.
In the right part, leading zeros are not considered (see example #1).
Remember to not confuse partitions with permutations or combinations. In the Instructions, "combination" is related to a combination of the left and the right part containing consecutive digits (see example #2, where is reported each combination of possible partitions).
Trivially, every positive integer lower than 10 can't be partitioned into two parts and it's not a Modest number (see example #4)."""
<br><br>
[5XNKfyxBosjSXCWLn](https://edabit.com/challenge/5XNKfyxBosjSXCWLn)
<br><br>
```is_modest(2036) ➞ True

Combination 1:
Left = 2 | Right = 036 = 36 (Leading zeros are not considered)
Number (2036) % Right (36) =  20 != Left (2)

Combination 2:
Left = 20 | Right = 36
Number (2036) % Right (36) = 20 = Left (20)

# At least a combination satisfies the condition
# It's a Modest number
```

<br><br>
