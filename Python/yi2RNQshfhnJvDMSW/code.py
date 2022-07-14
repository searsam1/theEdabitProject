def left(lst):
    res = [] 

    total = 0 
    for i in range(len(lst)):
        total += lst[i]
        res.append( [total] + lst[i+1:] )

    res = res[1:]
    return [lst] + res

def right(lst):
    lst = lst[::-1]
    res = [] 

    total = 0 
    for i in range(len(lst)):
        total += lst[i]
        res.append( ([total] + lst[i+1:])[::-1] )

    res = res[1:]
    return [lst[::-1]] + res

def squish(lst, d):

    return [right, left][d == "left"](lst) if lst else []