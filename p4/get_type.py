import types

print(type('123'))
print(type(123))
print(type(abs))
print('type(abs) =', type(abs))
print('type(123) =', type(123))
print(type(123)==int)

print(type(abs)==types.BuiltinFunctionType)
# isinstance() 也可以用
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir('abc'))
class MyObject(object):
     def __init__(self):
         self.x = 9
     def power(self):
         return self.x * self.x
obj = MyObject()
print(obj.x)
print(hasattr(obj, 'y')) # 有属性'y'吗？
print(setattr(obj, 'y', 19)) # 设置一个属性'y'
print(getattr(obj, 'y')) # 获取属性'y'
print(obj.y)
getattr(obj, 'z') # 获取属性'z'