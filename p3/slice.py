# advancedfeature

# append a list
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

# slice

print(L[:10]) # first 10
print(L[-10:]) # last 10
print(L[10:20]) # 11-20
print(L[:10:2]) # first 10 step = 2
print(L[-10::2]) # last 10 step = 2

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格
def trim(s):
    #check if s is empty
    if(s ==''):
        s = 'empty str'
        return s
    while s[:1]==' ':# 切片第一个元素，如果等于空格
        s=s[1:]      #则s等于第二个元素到最后一个元素（循环到第一个元素不等于空格退出）
    while s[-1:]==' ':# 切片最后一个个元素，如果等于空格
        s=s[:-1]      #则s等于第一个元素到倒数第二个元素（循环到第最后一个元素不等于空格退出）
    if(s ==''):
        s = 'all is space'
    return s          #输出循环之后的s