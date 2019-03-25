import random as rn
target=[1,1,0,1,1,0,0,1,1,1,0,0,0,1,0,1]
class individual:
	def __init__(self):
		self.genes=[]
		for i in range(len((target))):
			self.genes.append(abs((rn.randint(0,5000))%2))
	
	def getContent(self):
		return ''.join(str(self.genes))

	def getfitness(self):
		self.fitness=0
		for i in range(len(self.genes)): 
			if self.genes[i] == target[i]:
				self.fitness +=1
		return self.fitness	
	def crossOver(self,patner):
		self.child = individual()
		for i in range(len((self.genes))):
			if rn.random() < 0.5:
				self.child.genes[i] = self.genes[i]
			else:
				self.child.genes[i] = patner.genes[i]
		return self.child

	def mutate(self): # Mutate it 
		for i in range(len(self.genes)):
			if rn.random() < 0.01: # In real this parameter changes alot
				self.genes[i] == abs((rn.randint(0,5000)%2))
