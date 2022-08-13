# Alec Sears
def factorial(n):
    total = n
    while n > 1:
        n -= 1
        total += n
    return total

def ry_seq(n, s=None):
    red, length, total = n * 2 - 1, n * 2 - 1, n * 2 - 1
    while length > 1:
        length -= 2
        total += length * 2
    yellow = total - red
    if n == 0:
        red, yellow, total = 0,0,0
    if s in ["all", "red", "yellow"]:
        return {"all": total, "red" : red, "yellow" : yellow}[s]
    return False
#