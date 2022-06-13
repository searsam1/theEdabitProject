from award_prizes import award_prizes
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(award_prizes({
	'Joshua' : 45,
	'Alex' : 39,
	'Eric' : 43
}), {
	'Joshua' : 'Gold',
	'Alex' : 'Bronze',
	'Eric' : 'Silver'
})

Test.assert_equals(award_prizes({
	'Person A' : 1,
	'Person B' : 2,
	'Person C' : 3,
	'Person D' : 4,
	'Person E' : 102
}), {
	'Person A' : 'Participation',
	'Person B' : 'Participation',
	'Person C' : 'Bronze',
	'Person D' : 'Silver',
	'Person E' : 'Gold'
})

Test.assert_equals(award_prizes({
	'Mario' : 99,
	'Luigi' : 100,
	'Yoshi' : 299,
	'Toad' : 2
}), {
	'Mario' : 'Bronze',
	'Luigi' : 'Silver',
	'Yoshi' : 'Gold',
	'Toad' : 'Participation'
})
