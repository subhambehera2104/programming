class Vehicle:

	def __init__(self):
		pass

	def start(self):
		print("Vehicle started\n")
	
	def stop(self):
	
		print("Vehicle stop\n")
	
	def info(self):
		print("vehicle info\n")
	


class Bike(Vehicle): # inheritance
	def __init__(self):
		self.wheels=2
		print("inside bike constructor\n")

	def start(self):
		print("Bike started\n")
	
	def stop(self):
		print("Bike stop\n")
	

	def info(self):
		print(f"Bike info wheels {self.wheels}\n")
	
class Car(Vehicle): # inheritance
	def __init__(self):
		self.wheels=4
		print("inside Car constructor\n")

	def start(self):
		print("Car started\n")
	
	def stop(self):
		print("Car stop\n")
	
#main
v = Vehicle() #creating object of a class
v.start()
v.info()
v.stop()


b = Bike()
b.start()
b.info()
b.stop()


c = Car()
c.start()
c.info()
c.stop()


v1 = Bike()
#b1 = Vehicle(); not allowed creating a child object from parent

