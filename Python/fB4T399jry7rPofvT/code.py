def gpa_calculator(student):
	

TestsConsolefirst = {"name": "Utsab Karkee", "courses": [{"name": "cal1", "credit_hours": 5, "grade": "A"}, {"name": "phy1", "credit_hours": 3, "grade": "A"}, {"name": "eng1", "credit_hours": 3, "grade": "B"}, {

    "name": "pysch1", "credit_hours": 3, "grade": "A"}, {"name": "music1", "credit_hours": 3, "grade": "A"}, {"name": "chem1", "credit_hours": 3, "grade": "A"}], "semester": "Fall 2013"}

second = {"name": "Ansha Mandal", "courses": [{"name": "cal1", "credit_hours": 5, "grade": "A"}, {

    "name": "kin1", "credit_hours": 3, "grade": "A"}], "semester": "Spring 2018"}

third = {"name": "Lila Jha", "courses": [{"name": "cal1", "credit_hours": 5, "grade": "B"}, {"name": "phy1", "credit_hours": 3, "grade": "B"}, {"name": "eng1", "credit_hours": 3, "grade": "B"}, {

    "name": "pysch1", "credit_hours": 3, "grade": "B"}, {"name": "music1", "credit_hours": 3, "grade": "C"}, {"name": "chem1", "credit_hours": 3, "grade": "A"}], "semester": "Summer 2018"}

fourth = {"name": "Rama Basnet", "courses": [{"name": "cal3", "credit_hours": 3, "grade": "B"}, {"name": "dan1", "credit_hours": 3, "grade": "C"}, {"name": "eng3", "credit_hours": 3, "grade": "A"}, {

    "name": "pysch1", "credit_hours": 3, "grade": "A"}, {"name": "music1", "credit_hours": 3, "grade": "A"}], "semester": "Spring 2017"}

fifth = {"name": "Rima Rawal", "courses": [{"name": "cal1", "credit_hours": 5, "grade": "A"}, {

    "name": "kin1", "credit_hours": 3, "grade": "F"}], "semester": "Spring 2018"}



Test.assert_equals(gpa_calculator(first),"Utsab Karkee GPA for Fall 2013 is 3.85")

Test.assert_equals(gpa_calculator(second),"Ansha Mandal GPA for Spring 2018 is 4.00")

Test.assert_equals(gpa_calculator(third),"Lila Jha GPA for Summer 2018 is 3.00")

Test.assert_equals(gpa_calculator(fourth),"Rama Basnet GPA for Spring 2017 is 3.40")

Test.assert_equals(gpa_calculator(fifth),"Rima Rawal GPA for Spring 2018 is 2.50")