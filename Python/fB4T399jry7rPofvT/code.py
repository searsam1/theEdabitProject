def gpa_calculator(student):
    class Student():

        def __init__(self,info):
            self.student_name = info["name"]
            self.semester = info["semester"]
            self.courses = info["courses"]
            self.credit_hours = [d["credit_hours"] for d in self.courses]
            self.grades = [{"A" : 4, "B" : 3, 
                            "C" : 2, "D" : 1, "F" : 0}[d["grade"]]
                            for d in self.courses
                            ]
            self.gpa = sum(map(lambda x : x[0] * x[1], 
            zip(self.grades, self.credit_hours))) / sum(self.credit_hours)
    stud = Student(student)
    return "{0} GPA for {1} is {2}".format(stud.student_name, 
	stud.semester, 
	str(round(stud.gpa,2)).ljust(4,"0")
	)