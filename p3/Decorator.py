import functools


def now():
    print('2022-3-25')
f = now
# 函数对象有一个__name__属性
print(now.__name__)
print(f.__name__)

#现在，假设我们要增强now()函数的功能，
# 比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

#本质上，decorator就是一个返回函数的高阶函数

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 把@log放到now()函数的定义处，相当于执行了语句：
# now = log(now)

@log
def now():
    print('2015-3-25')
now()

# 如果decorator本身需要传入参数，
# 那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本
# 三层嵌套
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print(f'{text} {func.__name__}:')
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2015-3-25')
now()
# 把@log放到now()函数的定义处，相当于执行了语句：
# now = log('execute')(now)

# @functools.wraps(func) 把函数名字从wrapper 变成正确的now
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator