# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素


def _num_iter():
    n = 3
    while True:
        n = n + 2
        yield n

def _check_div(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _num_iter() # 初始序列
    while True:        
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_check_div(n), it) # 构造新序列
for n in primes():
    if n < 10:
        print(n)
    else:
        break
def odd():    
    yield 1
    print('step 1')
    n = 1
    while(n < 10):
        n = n + 1     
        print(n)   
        yield n
        print(f'step {n:d}')
        n = n +1
for a in odd():
    if a < 10:
        print(a)
    else:
        break
    

