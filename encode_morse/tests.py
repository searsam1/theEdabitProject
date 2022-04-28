from encode_morse import encode_morse
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")
		
Test.assert_equals(encode_morse("EDABBIT CHALLENGE"), ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. .", "Test 1")
Test.assert_equals(encode_morse("HELP ME !"), ".... . .-.. .--.   -- .   -.-.--", "Test 2")
Test.assert_equals(encode_morse("CHALLENGE"), "-.-. .... .- .-.. .-.. . -. --. .", "Test 3")
Test.assert_equals(encode_morse("1 APPLE AND 5 CHERRY, 7 SANDWICHES, 2 TABLES, 9 INVITED GUYS ! THAT'S SO COOL..."), ".----   .- .--. .--. .-.. .   .- -. -..   .....   -.-. .... . .-. .-. -.-- --..--   --...   ... .- -. -.. .-- .. -.-. .... . ... --..--   ..---   - .- -... .-.. . ... --..--   ----.   .. -. ...- .. - . -..   --. ..- -.-- ...   -.-.--   - .... .- - .----. ...   ... ---   -.-. --- --- .-.. .-.-.- .-.-.- .-.-.-", "Test 4")
Test.assert_equals(encode_morse("did you got my mail ?"), "-.. .. -..   -.-- --- ..-   --. --- -   -- -.--   -- .- .. .-..   ..--..", "Test 5")
Test.assert_equals(encode_morse("TWO THInGS TO KNOW : i FORGeT THeM :C"), "- .-- ---   - .... .. -. --. ...   - ---   -.- -. --- .--   ---...   ..   ..-. --- .-. --. . -   - .... . --   ---... -.-.", "Test 6")
