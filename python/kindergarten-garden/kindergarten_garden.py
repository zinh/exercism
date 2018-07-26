class Garden(object):
    m = {'R': 'Radishes', 'C': 'Clover', 'G': 'Grass', 'V': 'Violets'}

    def __init__(self, diagram, students = None):
        self.lines = [self.divide_str(line, 2) for line in diagram.split('\n')]
        self.students = sorted(students, key=lambda x: x[0]) if students else students

    def plants(self, student):
        i = self.students.index(student) if self.students else ord(student[0]) - 65
        return self.map_flower("".join([line[i] for line in self.lines]))

    def divide_str(self, txt, str_len):
        return [txt[i:i+str_len] for i in range(0, len(txt), str_len)]

    def map_flower(self, flowers):
        return [self.m[flower] for flower in flowers]
