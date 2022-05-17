from validate_relationships import validate_relationships
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")
"5>-1<0==0<-5>5==5"
Test.assert_equals(validate_relationships("5>-1<0=0<-5>5=5"), False)
Test.assert_equals(validate_relationships("-15<-10<=0=0<5"), True)
Test.assert_equals(validate_relationships("0=807<1000<=1000>9990<-3605<=20"), False)
Test.assert_equals(validate_relationships("3<=3<11>-109"), True)
Test.assert_equals(validate_relationships("44>-33>=1>-13"), False)
Test.assert_equals(validate_relationships("10>2=22>9>3"), False)
Test.assert_equals(validate_relationships("44>0<13>=-2<-1=-1"), True)
Test.assert_equals(validate_relationships("3>=-1"), True)
Test.assert_equals(validate_relationships("9<=9<-1"), False)
Test.assert_equals(validate_relationships("0<9<=9>-1"), True)
Test.assert_equals(validate_relationships("44>=0<13>-2<-1=1"), False)
Test.assert_equals(validate_relationships("-39<=5=5<=9>-1"), True)
Test.assert_equals(validate_relationships("55>7>=7>=1"), True)
Test.assert_equals(validate_relationships("3<19>-19>5>=-19"), False)
