
def factors(n):
    factors_list = [i for i in range(2,n) if not n % i]
    return factors_list

def semiprime(n):
    length = len(factors(n))
    if length == 1:
        return "Semiprime"
    elif length == 2 and all(len(factors(i)) == 0 for i in factors(n)):
        return "Squarefree Semiprime"
    return "Neither"