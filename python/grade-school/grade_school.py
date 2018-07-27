class School(object):
    def __init__(self):
        self.grade_book = {}

    def add_student(self, name, grade):
        self.grade_book[name] = grade

    def roster(self):
        return sorted(self.grade_book.keys(), key=lambda x: [str(self.grade_book[x]), x[0]])

    def grade(self, grade_number):
        names = [name for name, grade in self.grade_book.items() if grade == grade_number]
        return sorted(names, key=lambda x: x[0])
