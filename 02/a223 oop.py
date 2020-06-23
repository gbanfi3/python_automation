class Student:
    def __init__(self, name, gr):
        self.name = name
        self.grades = gr

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student('alfréd', (12,34,55,66,55))
print(student.name)
print(student.grades)
print(student.average())
print(Student.average(student))