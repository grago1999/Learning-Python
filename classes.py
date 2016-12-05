#December 1, 2016 -- Methods

#Create a class with the "class" keyword

class Dog:
	def __init__(self,arg1,arg2):
		self.breed = arg1
		self.pose = arg2

	#methods are functions associated with classes
	def roll_over(self):
		self.pose = "Upside down"
	
	def bark(self):
		print "BARK"

	def changepose(self, newpose):
		self.pose = newpose

Jonathan = Dog("pug","rightside up")
Jonathan.bark()
Jonathan.roll_over()

Jonathan.pose = "absef"
print Jonathan.pose


class Cat:
	def __init__(self,name,color,hobbies):
		self.name = name
		self.color = color
		self.age = 3
		self.hobbies = hobbies

	def changeage(self, newage):
		self.age = newage

	def getname(self):
		return self.name

	def listhobbies(self):
		for hobby in hobbies:
			print hobby


Tina = Cat("Tina","calico",["rowing","ping pong"])

Tina.changeage(16)
print "my cat's name is " + Tina.getname()

Bobert = Cat("Bobert","purple",)
cats = [Tina, Bobert]

mycatsfavoritefoods = {"tuna": Tina, "salmon":Bobert}