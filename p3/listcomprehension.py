# list comprehension
# for x in range(1, 11):
#     newlist.append(x*x)
# write in list compre way
newlist = [x * x for x in range(1, 11)]

# doule loop
newlist1 = [m+n for m in 'ABC' for n in 'XYZ']

print(newlist1[1])
print('m' + 'n',newlist1[2])
# 列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
newlist2 = [key1 +'='+ value for key1,value in d.items()]

print(newlist2[0])

# 在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else

newlist3 = [x for x in range(1, 11) if x % 2 == 0]
newlist4 = [x if x % 2 == 0 else -x for x in range(1, 11)]

# lianxi
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]
print(L2[2])