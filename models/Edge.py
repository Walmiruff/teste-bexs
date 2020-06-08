class Edge():
	def __init__(self,origin,destiny,weight = 0):
		self.origin = origin
		self.destiny = destiny
		self.weight = weight
				
	def getOrigin(self):
		return self.origin
		
	def setOrigin(self,vertice):
		self.origin = vertice
	
	def getDestiny(self):
		return self.destiny
	
	def setDestiny(self,vertice):
		self.destiny = vertice

	def setweight(self,weight):
		self.weight = weight
		
	def	getWeight(self):
		return self.weight

