
import random
from code import Sudoku



def check(r):
    sudoku = Sudoku(r)
    for i in range(9):
        row = sudoku.get_row(i)
        row = [i for i in row if i != 0]
        if len(set(row)) != len(row):
            return False
        col = sudoku.get_col(i)
        col = [i for i in col if i != 0]
        if len(set(col)) != len(col):
            return False
        sqr = sudoku.get_sqr(i)
        sqr = [i for i in sqr if i != 0]
        if len(set(sqr)) != len(sqr):
            return False
    return True




r = "010020300004001050060000007005400060000100002080092000300005090000700106007000000"
print(check(r))