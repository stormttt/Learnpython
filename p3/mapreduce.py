# 变量可以指向函数，函数的参数能接收变量
# 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
from functools import reduce


def f(x):
    return x*x

l = map(f,[1,2,3,4])
# pyhton3 中map返回一个list的object 不能直接输出，python2中直接返回list
print(list(l))

l1=[1,2,3,4]
print(l1)

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

L1 = ['adam', 'LISA', 'barT']
def normalize(name):
    name = name[:1].upper()+ name[1:].lower() 
    return name
L2 = list(map(normalize, L1))
print(L2)

# def prod(L):
#     def fn(x,y):
#         return x*y
#     return reduce(fn,L)
def prod(L):
    return reduce(lambda x ,y:x*y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
a,b = 1,2
print(2)

def str2float(s):
    num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    if s.find('.') == -1:
        return  reduce(lambda x,y:10*x+y,map(lambda x:num_dict[x],s))
    elif s.find('.') == 0:
        s1,s2 = s.split('.')
        lengthofs2 = len(s2)
        return reduce(lambda x,y:10*x+y,map(lambda x:num_dict[x],s2))/ (10**lengthofs2)
    s1,s2 = s.split('.')
    lengthofs2 = len(s2)
    print(lengthofs2)
    return  reduce(lambda x,y:10*x+y,map(lambda x:num_dict[x],s1))+reduce(lambda x,y:10*x+y,map(lambda x:num_dict[x],s2))/ (10**lengthofs2)

print(str2float('1'))