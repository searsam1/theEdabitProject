

def f(arr):
    count = 0
    for element in arr:
        count += 1
        if isinstance(element, list):
            count += f(element)
    return count
x = f([[[[[[[[[]]]]]]]]])
print(x)