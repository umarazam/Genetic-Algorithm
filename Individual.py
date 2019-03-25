import random as rn
target=[0,1,0,1,3,4,0,1,6,2,0,5,7]

#target = [999,8999,1990,2010,2019,6666,1818,1976,1111,0,55555,44444,3333,400000,331921]
class individual:
	def __init__(self):
		self.genes=[]
		for i in range(len((target))):
			self.genes.append(((rn.randint(-9,9))))
	
	def getContent(self):
		return (self.genes)

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
				self.genes[i] == ((rn.randint(-9,9)))
