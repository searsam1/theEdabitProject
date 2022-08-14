#
def is_self_describing(num):
    n = str(num)
    if len(str(num)) % 2:
        return False 

    pairs = [] 
    while num > 1:
        pairs.append(num % 100)
        num //= 100
    
    pairs = [tuple(str(i)) for i in pairs]
    
    pairs = all(n.count(tup[1]) == int(tup[0]) 
        for tup in pairs)
    return pairs
#