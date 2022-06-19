# list and tuple

classmates = ['Michael', 'Bob', 'Tracy']
# -1 and 1
print(classmates[0])
print(classmates[-1])
classmates.append('test')
print(classmates[-1])
# insert elements
classmates.insert(1, 'Jack')
# delete the last element
classmates.pop()
# delete element
classmates.pop(1)
# change element
classmates[1] = 'Sarah'
# len get the length
print(len(classmates))

# tuple cant be changed after initial cant insert and append
# more safe then list

t = (1,2,3)
print(t[1])

# tuple have a list, list can be "changed"
t = (1,2,[3,4])
print(t[2][0],t[2][1])
t[2][0] = 7
t[2][1] = 8
print(t[2][0],t[2][1])

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])