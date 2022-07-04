#---------##---------##---------##---------#
def is_factorial(n):    
    n2 = 1
    count = 0 
    while n2 < n:
        count += 1
        n2 *= count
    return [n2, count]
#---------##---------##---------##---------#
def is_exact(n):
    res = is_factorial(n)
    if res[0] == n:
        return res
    return "Not exact!"
#---------##---------##---------##---------#