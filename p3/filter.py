# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现的
from typing import Iterator

print(isinstance((x for x in range(10)), Iterator))