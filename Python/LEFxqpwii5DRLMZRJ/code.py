
[[9,10,11,12,13,14,15,16], [18,19,20,21,22]]

def get_sum(n):

    blocks = [] 
    for i in range(1,n):
        res = [] 
        while sum(res) < n:
            res.append(i)
            i += 1
        if sum(res) == n:
            blocks.append(res)
    print(blocks)
    return blocks


get_sum(100)