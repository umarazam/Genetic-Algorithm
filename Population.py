import Individual 
class population:
	size=10
	ind=[]*size
	def initializePopulation(self):
		for i in range(self.size):
			self.ind.append((Individual.individual()))
			self.ind[i].getfitness()

	def printPop(self):
		for i in range(self.size):
			print(self.ind[i].genes)

	def calc_MostFit(self):
		minfit=-1
		for i in range(self.size):
			temp=self.ind[i].fitness
			if temp > minfit:
				minfit =temp 
				index = i
		return index 
	
	def calc_MinFit(self):
		maxfit=111
		for i in range(self.size):
			temp=self.ind[i].fitness
			if temp < maxfit:
				maxfit =temp 
				index = i
		return index 	
	
	def calc_Second_MostFit(self):
		base_index=second_fitIndex=0
		base = self.ind[base_index].fitness
		for i in range(1,self.size):
			temp = self.ind[i].fitness
			if base < temp:
				second_fitIndex =base_index
				base= temp	
				base_index=i
			elif base > temp and self.ind[second_fitIndex].fitness < temp:
				second_fitIndex=i
			elif base_index==second_fitIndex:
				second_fitIndex=i

		return second_fitIndex
# If the least value comes after the base or max value than no true value
