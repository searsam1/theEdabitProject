from itertools import combinations

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_pair_list(num):
    arr = [i for i in range(2,num) if is_prime(i)]
    
    new_arr = [] 
    for i in arr:
        if i * 2 == num:
            new_arr.append(i), new_arr.append(i)
        else:
            new_arr.append(i)
    arr = new_arr

    p = list(combinations(arr, 2))
    
    res = ["{0}+{1}".format(tup[0], tup[1]) 
        for tup in p if sum(tup) == num]
    return res

res = prime_pair_list(10)
print(res)