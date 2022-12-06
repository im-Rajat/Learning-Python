students = []


class Student:
    school_name = "IIITD"

    def __init__(self, name, student_id=1):
        self.name = name
        self.student_id = student_id
        students.append(self)
        # student = {"name": name, "student_id": student_id}
        # students.append(student)

    def __str__(self):
        return "Student" + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


class HighSchoolStudent(Student):
    school_name = "IIIT Delhi"

    def get_school_name(self):
        return "This is a high School Student"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"


# s1 = HighSchoolStudent("RJ")
# print(s1.get_name_capitalize())

s1 = Student("RJ")
s1.school_name = "IIIII"
print(s1.school_name)
print(Student.school_name)
# print(s1)
#print(Student.school_name)
