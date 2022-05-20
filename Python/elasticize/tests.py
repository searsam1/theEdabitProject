from elasticize import elasticize
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(elasticize("ANNA"), "ANNNNA", "Example #1")
Test.assert_equals(elasticize("KAYAK"), "KAAYYYAAK", "Example #2")
Test.assert_equals(elasticize("X"), "X", "Example #3")
Test.assert_equals(elasticize("AA"), "AA")
Test.assert_equals(elasticize("ABC"), "ABBC")
Test.assert_equals(elasticize("BOB"), "BOOB")
Test.assert_equals(elasticize("OTTO"), "OTTTTO")
Test.assert_equals(elasticize("LEVEL"), "LEEVVVEEL")
Test.assert_equals(elasticize("IJKCBA"), "IJJKKKCCCBBA")
Test.assert_equals(elasticize("REDDER"), "REEDDDDDDEER")
Test.assert_equals(elasticize("ROTATOR"), "ROOTTTAAAATTTOOR")
