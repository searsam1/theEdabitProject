float median(std::vector<int> arr) {
	
}

TestsConsoleDescribe(get_median_tests)

{

	// Even number of integers

	It(even_number_of_integers_1){Assert::That(median({342, 98, 5456, 32, 786, 432, 890, 321}), Equals(387));}

	It(even_number_of_integers_2){Assert::That(median({32786, 7837, 83736, 83736, 10383, 738393}), Equals(58261));}

	It(even_number_of_integers_3){Assert::That(median({0, 0, 0, 0}), Equals(0));}

	It(even_number_of_integers_4){Assert::That(median({238, 432, 897, 710}), Equals(571));}

	// Odd number of integers

	It(odd_number_of_integers_1){Assert::That(median({20, 40, 20, 30, 50, 60, 70, 0, 20}), Equals(30));}

	It(odd_number_of_integers_2){Assert::That(median({32, 5, 78, 32, 4, 5, 3}), Equals(5));}

	It(odd_number_of_integers_3){Assert::That(median({7685, 83736, 38376, 73638, 7337}), Equals(38376));}

	// Should work with a float median

	It(should_work_with_a_float_median){Assert::That(median({1, 0, 1, 0, 0, 0, 1, 1}), Equals(0.5));}

	// Should work with negative values

	It(should_work_with_negative_values_1){Assert::That(median({-20, 40, 30, -2, 40, -13}), Equals(14));}

	It(should_work_with_negative_values_2){Assert::That(median({-30, -42, -60, -10, -30, -50}), Equals(-36));}

};