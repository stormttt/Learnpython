# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'test1'
s.age = 123
print(s.name)
print(s.age)
# error
s.score = 22