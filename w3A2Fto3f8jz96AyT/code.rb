def license(me, agents, others)
	
end

TestsConsoleTest.assert_equals(license("Zebediah", 1, "Bob Jim Becky Pat"), 100)

Test.assert_equals(license("Eric", 2, "Adam Caroline Rebecca Frank"), 40)

Test.assert_equals(license("Aaron", 3, "Jane Max Olivia Sam"), 20)

Test.assert_equals(license("Zebediah", 4, "Bob Jim Becky Pat"), 40)

Test.assert_equals(license("Zebediah", 5, "Bob Jim Becky Pat"), 20)