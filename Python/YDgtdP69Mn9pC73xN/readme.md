# Minesweeper I — Grid
<br><br>
## Donnamae
<br><br>
### """This challenge is based on the game Minesweeper.
Create a function that takes a grid of # and -, where each hash (#) represents a mine and each dash (-) represents a mine-free spot. Return a list where each dash is replaced by a digit indicating the number of mines immediately adjacent to the spot (horizontally, vertically, and diagonally).
N/A"""
<br><br>
[YDgtdP69Mn9pC73xN](https://edabit.com/challenge/YDgtdP69Mn9pC73xN)
<br><br>
```num_grid([
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"]
]) ➞ [
  ["0", "0", "0", "0", "0"],
  ["0", "1", "1", "1", "0"],
  ["0", "1", "#", "1", "0"],
  ["0", "1", "1", "1", "0"],
  ["0", "0", "0", "0", "0"],
]

num_grid([
  ["-", "-", "-", "-", "#"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["#", "-", "-", "-", "-"]
]) ➞ [
  ["0", "0", "0", "1", "#"],
  ["0", "1", "1", "2", "1"],
  ["0", "1", "#", "1", "0"],
  ["1", "2", "1", "1", "0"],
  ["#", "1", "0", "0", "0"]
]

num_grid([
  ["-", "-", "-", "#", "#"],
  ["-", "#", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "#", "#", "-", "-"],
  ["-", "-", "-", "-", "-"]
]) ➞ [
  ["1", "1", "2", "#", "#"],
  ["1", "#", "3", "3", "2"],
  ["2", "4", "#", "2", "0"],
  ["1", "#", "#", "2", "0"],
  ["1", "2", "2", "1", "0"],
]
```

<br><br>
