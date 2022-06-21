from string_expansion import string_expansion
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(string_expansion("3M2u5b2a1s1h2i1r"),"MMMuubbbbbaashiir")
Test.assert_equals(string_expansion("3Mat"),"MMMaaattt")
Test.assert_equals(string_expansion("3M123u42b12a"),"MMMuuubbaa")
Test.assert_equals(string_expansion("3n6s7f3n"),"nnnssssssfffffffnnn")
Test.assert_equals(string_expansion("0d4n8d2b"),"nnnnddddddddbb")
Test.assert_equals(string_expansion("0c3b1n7m"),"bbbnmmmmmmm")
Test.assert_equals(string_expansion("7m3j4ik2a"),"mmmmmmmjjjiiiikkkkaa")
Test.assert_equals(string_expansion("3A5m3B3Y"),"AAAmmmmmBBBYYY")
Test.assert_equals(string_expansion("5M0L8P1"),"MMMMMPPPPPPPP")
Test.assert_equals(string_expansion("2B"),"BB")
Test.assert_equals(string_expansion("7M1n3K"),"MMMMMMMnKKK")
Test.assert_equals(string_expansion("A4g1b4d"),"Aggggbdddd")
Test.assert_equals(string_expansion("111111"),"")
Test.assert_equals(string_expansion("4d324n2"),"ddddnnnn")
Test.assert_equals(string_expansion("5919nf3u"),"nnnnnnnnnfffffffffuuu")
Test.assert_equals(string_expansion("2n1k523n4i"),"nnknnniiii")
Test.assert_equals(string_expansion("6o23M32d"),"ooooooMMMdd")
Test.assert_equals(string_expansion("1B44n3r"),"Bnnnnrrr")
Test.assert_equals(string_expansion("M21d1r32"),"Mdr")
Test.assert_equals(string_expansion("23M31r2r2"),"MMMrrr")
Test.assert_equals(string_expansion("8494mM25K2A"),"mmmmMMMMKKKKKAA")
Test.assert_equals(string_expansion("4A46D6B3C"),"AAAADDDDDDBBBBBBCCC")
Test.assert_equals(string_expansion("23D42B3A"),"DDDBBAAA")
Test.assert_equals(string_expansion("143D36C1A"),"DDDCCCCCCA")
Test.assert_equals(string_expansion("asdf"),"asdf")
Test.assert_equals(string_expansion("23jbjl1eb"),"jjjbbbjjjllleb")
Test.assert_equals(string_expansion("43ibadsr3"),"iiibbbaaadddsssrrr")
Test.assert_equals(string_expansion("123p9cdbjs"),"pppcccccccccdddddddddbbbbbbbbbjjjjjjjjjsssssssss")
Test.assert_equals(string_expansion("2309ew7eh"),"eeeeeeeeewwwwwwwwweeeeeeehhhhhhh")
Test.assert_equals(string_expansion("312987rfebd"),"rrrrrrrfffffffeeeeeeebbbbbbbddddddd")
Test.assert_equals(string_expansion("126cgec"),"ccccccggggggeeeeeecccccc")
Test.assert_equals(string_expansion("1chwq3rfb"),"chwqrrrfffbbb")
Test.assert_equals(string_expansion("389fg21c"),"fffffffffgggggggggc")
Test.assert_equals(string_expansion("239vbsac"),"vvvvvvvvvbbbbbbbbbsssssssssaaaaaaaaaccccccccc")
Test.assert_equals(string_expansion("davhb327vuc"),"davhbvvvvvvvuuuuuuuccccccc")
Test.assert_equals(string_expansion("cvyb239bved2dv"),"cvybbbbbbbbbbvvvvvvvvveeeeeeeeedddddddddddvv")
Test.assert_equals(string_expansion(""),"")
# Mubashir
