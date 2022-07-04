def tree_photography(trees):

	

TestsConsoleTest.assert_equals(tree_photography([1, 2, 3, 6, 5]), "left")

Test.assert_equals(tree_photography([5, 6, 5, 4]), "right")

Test.assert_equals(tree_photography([1, 3, 1, 6, 5]), "left")

Test.assert_equals(tree_photography([1, 1, 2, 2, 2, 2, 3]), "left")

Test.assert_equals(tree_photography([1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2]), "left")

Test.assert_equals(tree_photography([3, 3, 3, 3, 2]), "right")

Test.assert_equals(tree_photography([4, 3, 2, 3, 3, 3, 1]), "right")

Test.assert_equals(tree_photography([3, 1, 4, 5, 2, 5, 1]), "left")

Test.assert_equals(tree_photography([4, 3, 3, 4, 3, 1, 3]), "right")

Test.assert_equals(tree_photography([5, 1, 2]), "right")

Test.assert_equals(tree_photography([1, 2, 4, 1, 5, 3, 1]), "left")

Test.assert_equals(tree_photography([1, 1, 1, 4, 1, 3, 5]), "left")

Test.assert_equals(tree_photography([3, 1, 4, 1, 5, 9, 2, 6]), "left")