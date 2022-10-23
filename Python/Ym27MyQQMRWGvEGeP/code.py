def is_consecutive(s, n=0):
	# recursive code in here
	if n:
		res = [ int(s[i:i+n]) for i in range(0, len(s), n) ] 
		return res
	all_blocks = [] 
	while n < len(s) // 2:
		all_blocks.append( is_consecutive(s, n + 1) )
		n += 1
	for block in all_blocks:
		res = [] 
		for i in range(1, len(block)):
			if block[i-1] - block[i] in [1, -1]:
				res.append(block[i-1] - block[i])
		if len(set(res)) == 1 and len(res) == len(block) - 1:
			return True 
	return False
		
import string
code = [ string.ascii_lowercase[i:i+5] for i in range(0, 26, 5) ]
print(code)		

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test

actual_param = [
  "121314151617", "123124125", "667666", "23242526", "444445", "1234567", "123412351236",
  "57585960616263", "500001500002500003", "919920921", "12341235123612371238", "326325324323",
  "54321", "56555453", "32332432536", "2324256", "1235", "121316", "12131213", "90090190290",
  "35236237238", "999897959493", "171615141312119", "1716171819181920", "273274273274"
]
expected = [
  True, True, True, True, True, True, True, True, True, True, True, True, True, True,
  False, False, False, False, False, False, False, False, False, False, False
]
for i, z in enumerate(actual_param): Test.assert_equals(is_consecutive(z), expected[i])