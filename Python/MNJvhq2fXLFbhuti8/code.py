
def almost_palindrome(n):
    str_n = str(n)
    count = 0 

    for c in set(str_n):
        if str_n.count(c) == 1:
            count += 1
    return [None,n][count <= 1]
	
def palindrome_sieve(nums):
    return [i for i in list(map(almost_palindrome,nums)) if i]


