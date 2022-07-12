# 既能检查参数，又可以用类似属性这样简单的方式来访问类的变量

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

class House:
	def __init__(self, *price):
		self.__price = price

	@property
	def price(self):
		return self._price
	
	@price.setter
	def price(self, new_price):
		if new_price > 0 and isinstance(new_price, float):
			self._price = new_price
		else:
			print("Please enter a valid price")

	@price.deleter
	def price(self):
		del self._price

h = House()
h.price = 1000.0
print(h.price)
h.price = 2.3
# del h.price
print(h.price)