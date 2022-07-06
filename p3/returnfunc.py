# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(lazy_sum(1, 3, 5, 7, 9))
print(lazy_sum(1, 3, 5, 7, 9)())
print(f)
print(f())
# Closure
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)

if f1==f2:
    print('same')
else:
    print('different')
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(count())
print(f1(),f2(),f3())

# 如果一定要引用循环变量就再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f4, f5, f6 = count1()
print(f4(),f5(),f6())

# nonlocal
def inc():
    x = 0
    def fn():
        # 仅读取x的值:
        return x + 1
    return fn

f = inc()
print(f()) # 1
print(f()) # 1

def inc():
    x = 0
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2