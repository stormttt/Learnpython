# 列表元素可以按照某种算法推算出来,一边循环一边计算的机制，称为生成器：generator。

# 把一个列表生成式的[]改成()，就创建了一个generator

from pickle import TRUE


L = [x * x for x in range(10)]
print(L[1])
g = (x * x for x in range(10))
# generator保存的是算法，
# 每次调用next(g)，就计算出g的下一个元素的值，
# 直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
print(next(g))
print(next(g))

# g 是可以迭代的
for n in g:
    print(n)
# normal function
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        # a, b = b, a + b
        # 相当于 t = (b, a + b) # t是一个tuple
        # a = t[0] b = t[1]
        a, b = b, a + b
        n = n + 1
    return 'done'
# generator function
# 要把fib函数变成generator函数，只需要把print(b)改为yield b就可以了
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # a, b = b, a + b
        # 相当于 t = (b, a + b) # t是一个tuple
        # a = t[0] b = t[1]
        a, b = b, a + b
        n = n + 1
    return 'done'
# 调用generator 函数将返回一个generator
# 可以用next 也可以用for loop 调用
for n in fib1(6):
    print(n)

# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value
g = fib1(6)
while TRUE:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

L = [1]
L1 =[1] + L +[1]
print(L1)



