def n_sided_shape(n)
	
end

TestsConsoleTest.assert_equals(n_sided_shape(1), "circle")

Test.assert_equals(n_sided_shape(2), "semi-circle")

Test.assert_equals(n_sided_shape(3), "triangle")

Test.assert_equals(n_sided_shape(4), "square")

Test.assert_equals(n_sided_shape(5), "pentagon")

Test.assert_equals(n_sided_shape(6), "hexagon")

Test.assert_equals(n_sided_shape(7), "heptagon")

Test.assert_equals(n_sided_shape(8), "octagon")

Test.assert_equals(n_sided_shape(9), "nonagon")

Test.assert_equals(n_sided_shape(10), "decagon")