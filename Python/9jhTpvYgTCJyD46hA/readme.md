# First Recurrence Index
<br><br>
## Deep Xavier
<br><br>
### """Create a function that identifies the very first item that has recurred in the string argument passed. It returns the identified item with the index where it first appeared and the very next index where it resurfaced ⁠— entirely as an dictionary; or as an empty dictionary if the argument is either None, an empty string, or no recurring item exists.
You can solve this challenge via a recursive approach, alternatively.
A recursive version of this challenge can be found here."""
<br><br>
[9jhTpvYgTCJyD46hA](https://edabit.com/challenge/9jhTpvYgTCJyD46hA)
<br><br>
```recur_index("DXTDXTXDTXD") ➞ {"D": [0, 3]}
// D first appeared at index 0, resurfaced at index 3
// T appeared and resurfaced at indices 3 and 6 but D completed the cycle first

recur_index("YXZXYTUVXWV") ➞ {"X": [1, 3]}

recur_index("YZTTZMNERXE") ➞ {"T": [2, 3]}

recur_index("AREDCBSDERD") ➞ {"D": [3, 7]}

recur_index("") ➞ {}

recur_index(None) ➞ {}
```

<br><br>
