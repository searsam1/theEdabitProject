def return_only_integer(arr)
	
end

TestsConsoleTest.assert_equals(return_only_integer([9, 2, "space", "car", "lion", 16]), [9, 2, 16])

Test.assert_equals(return_only_integer(["hello", 81, "basketball", 123, "fox"]), [81, 123])

Test.assert_equals(return_only_integer([10, "121", 56, 20, "car", 3, "lion"]), [10, 56, 20, 3])

Test.assert_equals(return_only_integer(["String", true, 3.3, 1]), [1])