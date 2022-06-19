# if
age = input()
# input is str change it to int
age = int(age)
if age >= 18:
    print(f'your age is {age}, you are an adult')
elif age >=6:
    print(f'your age is {age}, you are a teenager')
else:
    print(f'your age is {age}, you are a child')