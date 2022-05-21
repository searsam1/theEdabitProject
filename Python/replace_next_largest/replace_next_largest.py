def swap_large(l):
    s = sorted(l)
    print(s)
    d = {k:v for k, v in zip(s, s[1:])}
    print(d)
    
    return [d.get(n, -1) for n in l]
swap_large([5, 7, 3, 2, 8])

