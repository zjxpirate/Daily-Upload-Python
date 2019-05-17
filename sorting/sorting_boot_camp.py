

# 1. sorting boot camp

class Student(object):
    def __init__(self, name, grade_point_average):
        self.name = name
        self.grade_point_average = grade_point_average

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return repr((self.name, self.grade_point_average))



students = [
    Student('A', 4.0),
    Student('C', 3.0),
    Student('B', 2.0),
    Student('D', 3.2)
]



# sort according to __lt__ defined in Student. students remained unchanged.
students_sort_by_name = sorted(students)
print(students_sort_by_name)

# sort students in-place by grade_point-average.
students.sort(key=lambda student: student.grade_point_average)
print(students)


