
def is_prime(n):
    if n == 1:
        return False
    return all(n % i != 0 for i in range(2, n))




def sexy_triplets(low, high):
    def sex(n):
        
        triple1 = n
        triple2 = triple1 + 6
        triple3 = triple2 + 6

        if is_prime(triple1) and is_prime(triple2) and is_prime(triple3) and not is_prime(triple3 + 6):
            
            return [triple1, triple2, triple3]
    
    res = []
    for i in range(low, high-11):
        if sex(i):
            res.append(sex(i))
    return res

res = sexy_triplets(64,88)
print(res)




