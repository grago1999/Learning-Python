class college(object):
	def __init__(self,name,gpa,classes,sat):
		self.name = name
		self.gpa = gpa
		self.classes = classes
		self.sat = sat

college_list = {}

def add_college(name,gpa=0,classes=0,sat=0):
	newapp = college(name,gpa,classes,sat)
	id=len(college_list)+1
	college_list[str(id)]=newapp

def display_college(id):
	app = college_list[str(id)]
	print "College #"+str(id)
	print "Name: ", app.name
	print "GPA: ", app.gpa
	print "Classes: ", app.classes
	print "SAT: ", app.sat

add_college("Harvard", 3.9,6,2300)
add_college("Princeton",3.6,4,1900)