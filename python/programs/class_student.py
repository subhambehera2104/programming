
class Student:
	def __init__(self, name1,  roll1,  mobile1):
		self.name=name1
		self.roll=roll1
		self.mobile=mobile1

	def display(self):
		print(f"name {self.name} \n roll {self.roll} \n mobile {self.mobile} \n")
# main
s1=Student("xyz", "123", "1234567890")
s1.display()
name =input("Enter Student name ") 
roll= input("Enter Student roll ")
mobile=input("Enter Student mobile number ")

s2=Student(name, roll, mobile)	
s2.display()
	
 