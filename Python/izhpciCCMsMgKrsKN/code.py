# This number sequence can start with any positive integer n. 
# s is the sum of the individual digits in n. 
# If s divides into n evenly
#  then the next term of the series is n//s. Otherwise 
# the next term is n*s. 
def s(n):
    return sum(int(i) for i in str(n))

def next_seq(n):
    if n % s(n) == 0:
        next_term = n // s(n)
    else:
        next_term = n * s(n)
    return next_term

def dead_end(res):
    seq = []
    while not res in seq:
        seq.append(res)
        res = next_seq(res)
    return len(seq), seq[-1]

dead_end(1)

# TestsConsoleTest.assert_equals(dead_end(1), (1, 1))

# Test.assert_equals(dead_end(9), (2, 1))

# Test.assert_equals(dead_end(1000), (1, 1000))

# Test.assert_equals(dead_end(999), (3, 370))

# Test.assert_equals(dead_end(38), (12, 174813842944))

# Test.assert_equals(dead_end(93), (9, 217))

# Test.assert_equals(dead_end(11615819), (74, 1354959139828966431926720346323206635520))

# Test.assert_equals(dead_end(100000001), (15, 220258825732))