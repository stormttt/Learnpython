# 牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，
# 每个对象都拥有相同的方法，但各自的数据可能不同

class Student(object):
    # pass
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('bart',99)

bart.name = 'bart'
print(bart)
print(bart.name)
print(bart.get_grade())

