# Word Chain
<br><br>
## Helen Yu
<br><br>
### """A word-chain is an array of words, where the next word is formed by changing exactly one letter from the previous word. We do not add or subtract letters from words, only change them.
Create a function that returns True if an array is a word-chain and False otherwise.
Each word in a word chain has equal length.
All words will be in lower case."""
<br><br>
[SmM8CSnsTTEF3mhX3](https://edabit.com/challenge/SmM8CSnsTTEF3mhX3)
<br><br>
```is_word_chain(["meal", "seal", "seat", "beat", "beet"]) ➞ True
# Change "m" in "meal" to get "seal", "l" to get "seat", etc.

is_word_chain(["red", "bed", "bet", "bat", "sat"]) ➞ True

is_word_chain(["red", "bat", "cat", "sat"]) ➞ False
# Do not change more than one letter ("red" and "bat").

is_word_chain(["read", "red", "led", "lad", "lady"]) ➞ False
# Do not add or subtract letters.
```

<br><br>
