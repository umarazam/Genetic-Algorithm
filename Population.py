import Individual 
class population:
	size=10
	ind=[]*size
	def initializePopulation(self):
		for i in range(self.size):
			self.ind.append((Individual.individual()))

	def printPop(self):
		for i in range(self.size):
			print(self.ind[i].genes)

	def calc_MostFit(self):
		minfit=-1
		for i in range(self.size):
			temp=self.ind[i].getfitness()
			if temp > minfit:
				minfit =temp 
				index = i
		return index 
	
	def calc_MinFit(self):
		maxfit=111
		for i in range(self.size):
			temp=self.ind[i].getfitness()
			if temp < maxfit:
				maxfit =temp 
				index = i
		return index 	
	
	def calc_Second_MostFit(self):
		base = self.ind[0].getfitness()
		second_fit=0
		for i in range(1,self.size):
			temp = self.ind[i].getfitness()
			if base < temp:
				second_fit=i
				base = temp	
		return second_fit
