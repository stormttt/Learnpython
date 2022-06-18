# practice 

# ord() and chr()

print(ord('A')) 
print(chr(66)) 
# bytes type and unicode
# str to bytes
a = 'ABC'.encode('ascii')
b = 'ABC'.encode('utf-8')
print(a,b)
# new line 
print(a, b, sep='\n')

#bytes to str
c = b'ABC'.decode('ascii')
print(c)

# len() calculate numbers of bytes or characters
d = len(b'ABC')
e = len('ABC')
print(d,e,sep='\n')

# %s %d %f ...

print('%2d-%02d'%(3,1))
print('%.2f' % 3.1415926)
print('Hi, %s, you have $%d and %d.' % ('Michael', 1000000,d))

#format() and f-string
r = 2
s = 3 * r ** 2 
print(f'The area of a circle with radius {r} is {s:.2f}')
print('The area of a circle with radius {0} is {1:.3f}'.format(r,s))

#lianxi
s1=72
s2=85
grade=(s2-s1)/s1*100
print('小明的分数提升了{0:.2f}%.'.format(grade))
print(f'小明的分数提升了{grade:.2f}%.')
# sometimes need use %% replace % in str
print('小明的分数提升了%.2f%%.' % grade)