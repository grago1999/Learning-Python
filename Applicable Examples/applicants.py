class applicant(object):

	def __init__(self,name,gpa,classes,sat):
		self.name = name
		self.gpa = gpa
		self.classes = classes
		self.sat = sat

	def getgrade(self,grade):
		self.classes += 1
		self.gpa = (self.gpa*(self.classes-1)+grade)/self.classes

	def takesat(self,sat):
		self.sat = sat

profiles = {}

def add_applicant(name,gpa=0,classes=0,sat=0):
	newapp = applicant(name,gpa,classes,sat)
	id=len(profiles)+1
	profiles[str(id)]=newapp

def display_applicant(id):
	app = profiles[str(id)]
	print "APPLICANT #"+str(id)
	print "Name: ", app.name
	print "GPA: ", app.gpa
	print "Classes: ", app.classes
	print "SAT: ", app.sat

add_applicant("bob")
add_applicant("steve",3.75,4,2050)

