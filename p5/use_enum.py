from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
#@unique装饰器可以帮助我们检查保证没有重复值。
print(Weekday.Mon)
print(Weekday['Tue'])
print(Weekday.Tue.name)
print(Weekday.Tue.value)

print(Weekday(1))
print(Weekday(1).name)
# print(Weekday(7))