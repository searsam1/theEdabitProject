# Return the Sum of Two Numbers (on the Moon)
<br><br>
## Matt
<br><br>
### """When two numbers are added together, the strange Lunar arithmetic is used on the Moon. The Lunar sum of two numbers is not determined by the sum of their individual digits, but by the highest digit of the two taken into account at each step, in columnar form.
Given two positive integers number1 and number2, implement a function that returns their sum as a new integer.
The given numbers will be always positive integers: no exceptions to handle."""
<br><br>
[NfhWZbpcyydySzXeq](https://edabit.com/challenge/NfhWZbpcyydySzXeq)
<br><br>
```2  4  6  +
3  1  7  =
--------
3  4  7

# 3 > 2 | 4 > 1 | 7 > 6

1  3  4  +
   5  4  =
--------
1  5  4

#  1 > 0 | 5 > 3 | 4 == 4
# Blank spots in the columnar form are equals to 0

   2  0  +
1  4  0  =
-------
1  4  0

# 1 > 0 | 4 > 2 | 0 == 0
```

<br><br>
