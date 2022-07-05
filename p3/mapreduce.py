# 变量可以指向函数，函数的参数能接收变量
# 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x*x

l = map(f,[1,2,3,4])
# pyhton3 中map返回一个list的object 不能直接输出，python2中直接返回list
print(list(l))

l1=[1,2,3,4]
print(l1)