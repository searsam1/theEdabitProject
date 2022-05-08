from gen_tiles import gen_tiles
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(sorted(gen_tiles()), ['ba tiao', 'ba tiao', 'ba tiao', 'ba tiao', 'ba tong', 'ba tong', 'ba tong', 'ba tong', 'ba wan', 'ba wan', 'ba wan', 'ba wan', 'bing gan', 'bing gan', 'bing gan', 'bing gan', 'er tiao', 'er tiao', 'er tiao', 'er tiao', 'er wan', 'er wan', 'er wan', 'er wan', 'ji', 'ji', 'ji', 'ji', 'jiu tiao', 'jiu tiao', 'jiu tiao', 'jiu tiao', 'jiu tong', 'jiu tong', 'jiu tong', 'jiu tong', 'jiu wan', 'jiu wan', 'jiu wan', 'jiu wan', 'liu tiao', 'liu tiao', 'liu tiao', 'liu tiao', 'liu tong', 'liu tong', 'liu tong', 'liu tong', 'liu wan', 'liu wan', 'liu wan', 'liu wan', 'qi tiao', 'qi tiao', 'qi tiao', 'qi tiao', 'qi tong', 'qi tong', 'qi tong', 'qi tong', 'qi wan', 'qi wan', 'qi wan', 'qi wan', 'san tiao', 'san tiao', 'san tiao', 'san tiao', 'san tong', 'san tong', 'san tong', 'san tong', 'san wan', 'san wan', 'san wan', 'san wan', 'si tiao', 'si tiao', 'si tiao', 'si tiao', 'si tong', 'si tong', 'si tong', 'si tong', 'si wan', 'si wan', 'si wan', 'si wan', 'wu tiao', 'wu tiao', 'wu tiao', 'wu tiao', 'wu tong', 'wu tong', 'wu tong', 'wu tong', 'wu wan', 'wu wan', 'wu wan', 'wu wan', 'yan jing', 'yan jing', 'yan jing', 'yan jing', 'yi wan', 'yi wan', 'yi wan', 'yi wan'])
