'Object Oriented Programming'
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('bart',99)
lisa = Student('lisa',98)

bart.print_score()