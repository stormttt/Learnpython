# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
#跟普通函数一样，lambda 也支持 无参数、默认参数 和可变参数

#无参数：lambda :100  #传入一个固定值或者其他值

#默认参数： 
lambda a,b=20,c=30 :a+b+c

#可变参数： 
fn=lambda *a:list(a) 
print(fn(1,2,3)) #输出[1,2,3]

#可变参数：
fn=lambda **kws: kws
print(fn(l1=1,l2=2,l3=3)) #输出{'l1': 1, 'l2': 2, 'l3': 3}