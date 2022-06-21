# iteration
from collections.abc import Iterable
for ch in 'abcdef':
    print(ch)

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

# 通过collections.abc模块的Iterable类型判断可否迭代
isinstance('abc', Iterable)

#Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身

for i, value in enumerate(['A', 'B', 'C']):
    print(i,value)

for i,j,k in [(1,1,1),(1,2,3),(2,1,1),(4,2,3)]:
    print(i,j,k)

def findMinAndMax(L):
    
    if L ==[]:
        return (None, None)
    else:
        maxnum,minnum = L[0],L[0]
        for number in L:
            if(number > maxnum):
                maxnum = number
            if(number < minnum):
                minnum = number 
        return (minnum,maxnum)
print(findMinAndMax([]))
    