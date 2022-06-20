# function
import math
from logging import raiseExceptions


n1 = 255
n2 = 1000
print(hex(255))
# def a function
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(n2))
# 如果你已经把my_abs()的函数定义保存为abstest.py文件了，
# 那么，可以在该文件的当前目录下启动Python解释器，
# 用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名)

# empty function
def doNothing():
    pass

# check arguments
def my_abs1(x):
    if not isinstance(x,(int,float)):
        raise TypeError('check argument typeaaaaaaa')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs1(1))
# mutiple return acturally is a tuple
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
print(move(30,30,20,20))

# ax2+bx+c=0
def quadratic(a, b, c):
    sqrtnumber = math.sqrt(b**2-4*a*c)
    x1= (-b+sqrtnumber)/(2*a)
    x2= (-b-sqrtnumber)/(2*a)
    return x1, x2
print(quadratic(2,3,1))

# 默认参数

def power(x,n=2):
    begin = x
    while n > 1:
        x = begin * x
        n = n - 1
    return x
print(power(2,10))
# 默认参数必须指向不变对象，不能是list
def add_end(L=[]):
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end())
print(add_end())

# change funtion to that:
def add_end1(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

#可变参数
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
# 但是，调用该函数时，可以传入任意个参数，包括0个参数：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(2))
print(calc(2,3))

# 如果已经有个list
# *nums表示把nums这个list的所有元素作为可变参数传进去。
nums = [1,2,3,4,5]
print(calc(*nums))


#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，
#这些关键字参数在函数内部自动组装为一个dict

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Adam', 45, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
# 两种方法
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)

# 命名关键字参数
def person1(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
person1('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# 如果一个函数在内部调用自身本身，这个函数就是递归函数

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

# 递归容易栈溢出，用尾递归解决
# 事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# # 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)