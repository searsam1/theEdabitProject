
def count(n):
    n = abs(n)
    if n < 10:
        return 1

    s = 0
    while n >= 1:
        s += count(n % 10)
        n //= 10
    return s
    
    
    
    
        

class Test:
    
    @staticmethod
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")

num_vector, res_vector = [
  [0, 318, -92563, 4666, -314890, 654321, 638476, 12345, 1289396, -1232323, 12839393, -231273683],
  [1, 3, 5, 4, 6, 6, 6, 5, 7, 7, 8, 9]
]
for i, n in enumerate(num_vector): Test.assert_equals(count(n), res_vector[i])
