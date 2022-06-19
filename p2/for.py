# for loop
fruits = ["apple", "orange", "kiwi"]
  
# Creating an iterator object 
# from that iterable i.e fruits
iter_obj = iter(fruits)
  
# Infinite while loop
while True:
  try:
    # getting the next item
    fruit = next(iter_obj)
    print(fruit)
  except StopIteration:
  
    # if StopIteration is raised, 
    # break from loop
    break

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(f'name is {name}')

numbers = range(5)
sum = 0
for x in numbers:
    sum = sum + x
print(sum)

# while loop
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for l in L:
    print(f'str is {l}')

# break
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# continue skip current loop to next

n = 0
while n <= 10:
    n = n + 1
    if n % 2 == 0: # 当为偶数时，条件满足，执行continue语句
        continue # continue语句会结束当前循环
    print(n)
    n = n + 1
print('END')
