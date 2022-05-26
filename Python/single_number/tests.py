from single_number import single_number
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

from time import perf_counter
from random import randint, shuffle
tic = perf_counter()

Test.assert_equals(single_number([2, 2, 3, 2]), 3)
Test.assert_equals(single_number([0, 1, 0, 1, 0, 1, 99]), 99)
Test.assert_equals(single_number([-1, 2, -4, 20, -1, 2, -4, -4, 2, -1]), 20)

t_function = 0
for _ in range(200):
    set_nums = {randint(-10000, 10000) for _ in range(randint(100, 1000))}
    expected = set_nums.pop()
    lst = sum([[x] * 3 for x in set_nums], [])
    shuffle(lst)
    lst.append(expected)
    shuffle(lst)
    tic_f = perf_counter()
    Test.assert_equals(single_number(lst), expected)
    t_function += perf_counter() - tic_f

print('t_function = {:.3f}'.format(t_function))
print('       t_total = {:.3f}'.format(perf_counter() - tic))
