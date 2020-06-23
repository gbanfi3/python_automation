class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (77,81,99,66,55)

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student()
print(student.name)
print(student.grades)
print(student.average())
print(Student.average(student))