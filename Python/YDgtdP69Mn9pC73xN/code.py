


def num_grid(arr):
    def bomb(row, col):
        row_len = len(arr[0])
        col_len = len(arr)
        char = arr[row][col]
        if char == "#":
            if row != 0:
                if arr[row - 1][col] != "#":
                    arr[row - 1][col] += "0"

                if col + 1 != col_len:
                    if arr[row - 1][col + 1] != "#":
                        arr[row - 1][col + 1] += "0"
                if col != 0:
                    if arr[row - 1][col - 1] != "#":
                        arr[row - 1][col - 1] += "0"
            
            if row + 1 != row_len:
                if arr[row + 1][col] != "#":
                    arr[row + 1][col] += "0"

                if col + 1 != col_len:
                    if arr[row + 1][col + 1] != "#":
                        arr[row + 1][col + 1] += "0"
                if col != 0:
                    if arr[row + 1][col - 1] != "#":
                        arr[row + 1][col - 1] += "0"

            if col != 0:
                if arr[row][col - 1] != "#":
                    arr[row][col - 1] += "0"

            if col + 1 != col_len:
                if arr[row][col + 1] != "#":
                    arr[row][col + 1] += "0"
            
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            bomb(i,j)
    
    res = [] 
    for i in arr:
        row = list(map(lambda x: str(x.count("0")) if x != "#" else "#", i))
        res.append(row)
    return res
        

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(num_grid([
['-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-']
]), [
['0', '0', '0', '0', '0'],
['0', '1', '1', '1', '0'],
['0', '1', '#', '1', '0'],
['0', '1', '1', '1', '0'],
['0', '0', '0', '0', '0']
])

Test.assert_equals(num_grid([
['-', '-', '-', '-', '#'],
['-', '-', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '-', '-', '-', '-'],
['#', '-', '-', '-', '-']
]), [
['0', '0', '0', '1', '#'],
['0', '1', '1', '2', '1'],
['0', '1', '#', '1', '0'],
['1', '2', '1', '1', '0'],
['#', '1', '0', '0', '0']
])

Test.assert_equals(num_grid([
['-', '-', '-', '#', '#'],
['-', '#', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '#', '#', '-', '-'],
['-', '-', '-', '-', '-']
]), [
['1', '1', '2', '#', '#'],
['1', '#', '3', '3', '2'],
['2', '4', '#', '2', '0'],
['1', '#', '#', '2', '0'],
['1', '2', '2', '1', '0']
])