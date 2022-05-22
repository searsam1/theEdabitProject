from get_sentence_value import get_sentence_value
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(get_sentence_value("abc ABC Abc"), 24)
Test.assert_equals(get_sentence_value("HELLO world"), 176)
Test.assert_equals(get_sentence_value("Edabit is Legendary"), 160)
Test.assert_equals(get_sentence_value("Her seaside sea-shelling business is really booming!"), 488)
Test.assert_equals(get_sentence_value("edabit Edabit EDABIT"), 164)
Test.assert_equals(get_sentence_value("expensive words"), 198)
Test.assert_equals(get_sentence_value("FISH AND CHIPS"), 232)
Test.assert_equals(get_sentence_value("this sentence is like a piece of hay in a needle stack"), 423)
Test.assert_equals(get_sentence_value("CAN YOU STOP SHOUTING?! I CAN'T HEAR MYSELF THINK!!!"), 966)
Test.assert_equals(get_sentence_value("a whisper in the wind..."), 205)
Test.assert_equals(get_sentence_value(",.;[,.;][,.;[,.][,.;,.]["), 0)
Test.assert_equals(get_sentence_value("Isn't it funny how the word BIG is physically smaller than the word small?"), 777)
Test.assert_equals(get_sentence_value("this is a really pricey sentence: ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"), 2503)
Test.assert_equals(get_sentence_value("                    "), 0)
Test.assert_equals(get_sentence_value(""), 0)
Test.assert_equals(get_sentence_value("Oranges and APPLES"), 236)
Test.assert_equals(get_sentence_value("Edabit is LEGENDARY"), 251)
