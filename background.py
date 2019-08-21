from address import address

class me:

	def __init__(self):
		self.firstName = "Yan"
		self.lastName = "Carvalho Borges"
		self.birth = "21/03/1997"
		self.gender = "Male"
		self.address = address('Brasil','Cruzeiro','Rua Maria José Tabaco','170')
		self.occupation = None

	def work(self, area):
		if(self.getAreaKnowledge(area) <= 0.8):
			checkStudy(area)
			study(area)

	def getAreaKnowledge(self, area):
		# This function return how much skill the object has from 0 to 1
		if(area == "data science"):
			return 0.2
		if(area == "web development"):
			return 0.6
		if(area == "API development"):
			return 0.7
		if(area == "front-end"):
			return 0.4
		if(area == "back-end"):
			return 0.8
		if(area == "Machine learning"):
			return 0.3

	def checkStudy(self, area):
		studying = ['Machine learning','Data science','API','Back-end']
		planning = ['Mobile','Front-end','Deep learning','Big data']
		if(area in planning):
			next_topic = planning.index(area)
			studying.append(next_topic)
			planning.remove(planning.index(area))

	def study(self, area):
		whatIKnow = self.startOnlineResearch(area)
		someExperience = self.startCode(whatIKnow)
		self.makeProjects(someExperience)

