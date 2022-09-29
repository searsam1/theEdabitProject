# Find Repeating
<br><br>
## hhqrk
<br><br>
### """Create a function that accepts a string and groups repeated, consecutive values. The groups should have the following structure:  [[value, first_index, last_index, times_repeated],  ...,  [value, first_index, last_index, times_repeated]].
value: Character being assessed.
first_index: Index of characters first appearance.
last_index: Index of characters last appearance.
times_repeated: Number of consecutive times character repeats.
An empty string should return an empty list: "" ➞ []
Non-repeated values should start and end on the same index."""
<br><br>
[b9sTvowiouGsiaZE3](https://edabit.com/challenge/b9sTvowiouGsiaZE3)
<br><br>
```find_repeating("a") ➞ [["a", 0, 0, 1]]

find_repeating("aabbb") ➞ [["a", 0, 1, 2], ["b", 2, 4, 3]]

find_repeating("1337") ➞ [["1", 0, 0, 1], ["3", 1, 2, 2], ["7", 3, 3, 1]]

find_repeating("aabbbaabbb") ➞ [["a", 0, 1, 2], ["b", 2, 4, 3], ["a", 5, 6, 2], ["b", 7, 9, 3]]
```

<br><br>
