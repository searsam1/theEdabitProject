# Squishing a List
<br><br>
## Helen Yu
<br><br>
### """Write a function that squishes a list from the left or the right.
Squishing from the left is to successively sum the first two elements of a list (shortening the list in the process).
Squishing from the right is to successively sum the last two elements of a list.
Include the original list as the first element in either squish.
Return an empty list if the input is an empty list."""
<br><br>
[yi2RNQshfhnJvDMSW](https://edabit.com/challenge/yi2RNQshfhnJvDMSW)
<br><br>
```squish([1, 2, 3, 4, 5], "left") 
➞ [[1, 2, 3, 4, 5], [3, 3, 4, 5], [6, 4, 5], [10, 5], [15]]

squish([1, 2, 3, 4, 5], "right")
➞ [[1, 2, 3, 4, 5], [1, 2, 3, 9], [1, 2, 12], [1, 14], [15]]

squish([1, 0, 2, -3], "left")
➞ [[1, 0, 2, -3], [1, 2, -3], [3, -3], [0]]

squish([1, 0, 2, -3], "right")
➞ [[1, 0, 2, -3], [1, 0, -1], [1, -1], [0]]
```

<br><br>
