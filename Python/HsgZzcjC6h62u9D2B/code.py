def is_magic_square(arr):
	sums = [] 
	for row in arr:
		sums.append(sum(row))
	for col in zip(*arr):
		sums.append(sum(col))
	d_1, d_2 = [],[] 
	for i in range(len(arr)):
		for j in range(len(arr)):
			if i == j:
				d_1.append(arr[i][j])
	sums.append(sum(d_1))
	arr = arr[::-1]
	for i in range(len(arr)):
		for j in range(len(arr)):
			if i == j:
				d_2.append(arr[i][j])
	sums.append(sum(d_2))
	
	return len(set(sums)) == 1
			
	

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(is_magic_square([[2,7,6],[9,5,1],[4,3,8]]), True)
Test.assert_equals(is_magic_square([[2,7,600],[9,5,1],[-94,3,8]]), False)
Test.assert_equals(is_magic_square([[2,7,0.5],[9,555,1],[-9,3,8]]), False)
Test.assert_equals(is_magic_square([[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]), True)
Test.assert_equals(is_magic_square([[7,12,1,14],[2,13,8,11],[16,3,10,5],[9,6,15,4]]), True)
Test.assert_equals(is_magic_square([[7,12,1,14],[2,13,8,11],[16,3,10,5],[9,6,16,5]]), False)
Test.assert_equals(is_magic_square([[1,14,14,4],[11,7,6,9],[8,10,10,5],[13,2,3,15]]), True)
Test.assert_equals(is_magic_square([[1,14,14,4],[11,7,6,9],[8,11,10,5],[13,2,3,15]]), False)
Test.assert_equals(is_magic_square([[1,15,4,14],[10,11,5,8],[7,6,12,9],[16,2,13,3]]), False)