class Car():
	model = None
	brand = None
	number_of_wheels = 4

	def __init__(self, b, m):
		self.model = m
		self.brand = b

	def printName(self):
		print(self.model, self.brand)

	@classmethod
	def returnWheelCount(cls):
		return cls.number_of_wheels

	@classmethod
	def setWheelCount(cls, cnt):
		cls.number_of_wheels = cnt

	@staticmethod
	def horn():
		print("Beep Beep!")


my_car = Car("Toyota", "Innova")
Car.setWheelCount(5)
print(Car.returnWheelCount())
print(my_car.returnWheelCount())
my_car.printName()
my_car.horn()
Car.horn()