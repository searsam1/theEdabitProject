from babbage import babbage
from time import perf_counter
import unittest

class Test(unittest.TestCase):
	
	checks = []

	def assert_equals(a,b,message=None,checks=checks):
		checks.append(["Fail","Pass"][a==b])

s = perf_counter()
Test.assert_equals(babbage(481), 59)
Test.assert_equals(babbage(7009), 497)
Test.assert_equals(babbage(990025), 995)
Test.assert_equals(babbage(327369), 57213)
Test.assert_equals(babbage(269696), "Babbage was incorrect!")
Test.assert_equals(babbage(33765625), 28875)
Test.assert_equals(babbage(314062500), 36250)
e = perf_counter()

print("{:.2} Seconds to complete".format(e-s))