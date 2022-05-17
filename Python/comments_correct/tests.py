from comments_correct import comments_correct
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(comments_correct("//////"), True)
Test.assert_equals(comments_correct("/**//**////**/"), True)
Test.assert_equals(comments_correct("/**//**//**//**/"), True)
Test.assert_equals(comments_correct("///**///"), True)
Test.assert_equals(comments_correct("/**//////**//**////**/////"), True)
Test.assert_equals(comments_correct("//"), True)
Test.assert_equals(comments_correct("/**/"), True)
Test.assert_equals(comments_correct("///*/**/"), False)
Test.assert_equals(comments_correct("//*/**/"), False)
Test.assert_equals(comments_correct("/////"), False)
Test.assert_equals(comments_correct("///"), False)
Test.assert_equals(comments_correct("/**///**/"), False)
Test.assert_equals(comments_correct("/**/////**/"), False)
