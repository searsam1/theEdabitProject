def count_d(sentence)
	
    return sentence.count("d") + sentence.count("D")
end

TestsConsoleTest.assert_equals(count_d("My friend Dylan got distracted at school"), 4)

Test.assert_equals(count_d("Debris was scattered all over the place."), 2)

Test.assert_equals(count_d("The rodents hibernated in their den."), 3)