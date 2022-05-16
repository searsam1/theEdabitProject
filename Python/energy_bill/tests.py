from energy_bill import energy_bill
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(energy_bill("2020,01,01", "2020,04,01", 1000, 2000, 0.188, 0.243), "$220.62")
Test.assert_equals(energy_bill("1987,11,01", "1989,02,21", 874, 6253, 0.061, 0.124), "$406.76")
Test.assert_equals(energy_bill("2011,09,02", "2012,09,05", 3297, 4721, 0.151, 0.176), "$293.97")
Test.assert_equals(energy_bill("1970,01,01", "2020,11,22",   0, 22456, 0.0213, 0.1671), "$3763.59")
Test.assert_equals(energy_bill("1980,06,15", "1980,12,25", 7650, 9912, 0.0534, 0.054), "$137.77")
Test.assert_equals(energy_bill("2010,01,01", "2020,01,01", 2000, 2000, 0.171, 0.213), "$816.77")
Test.assert_equals(energy_bill("2010,01,01", "2020,01,01", 2785, 12874, 0.128, 0.148), "$1923.48")
Test.assert_equals(energy_bill("2017,03,01", "2017,06,01", 6348, 7559, 0.142, 0.20), "$199.88")
Test.assert_equals(energy_bill("1984,04,19", "1991,04,10", 2000, 1000, 0.61, 0.074), "Invalid meter readings")
Test.assert_equals(energy_bill("2020,01,01", "2019,01,01", 1000, 2000, 0.171, 0.243), "Invalid date")
# Author: ben3297
