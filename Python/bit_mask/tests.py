from bit_mask import bit_mask
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

from sys import _getframe
class Tester:
	def __init__(self):
		self.bin = bin
	def __getattribute__(self, name):
		if name == "bin" and _getframe(1).f_code != self.run.__code__:
			raise Test.AssertException("No cheating!")
		return super().__getattribute__(name)
	def run(self):
		# Testing starts here
		for i in range(256):
			rev_bin = self.bin(i)[2:][::-1] + "0"
			for j in range(len(rev_bin)):
				Test.assert_equals(bit_mask(i, j), int(rev_bin[j]), "Testing number %d at index %d" % (i, j))
		# Testing ends here
tester = Tester()
def bin(*args, **kwargs):
	raise Test.AssertException("No cheating!")
__builtins__.bin = bin
tester.run()
