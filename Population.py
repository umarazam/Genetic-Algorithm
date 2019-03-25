from Individual import individual
from Individual import target
import random as rn
class population:
	popSize=500
	generation=1
	bestScore=0
	def initializePopulation(self):
		self.pop=[]
		for i in range(self.popSize):
			self.pop.append(individual())

	def printPop(self):
		for p in self.pop:
			print(p.getContent())

	def matingPool1(self,parents):
		self.matingPool=[]
		for i in range(self.popSize):
			for j in range(parents[i].getfitness()):
				self.matingPool.append(parents[i])
		return self.matingPool

	def selection(self):
		self.x = rn.choice(range(len(self.matingPool)))
		self.y = rn.choice(range(len(self.matingPool)))

	def crossOver(self):
		self.child = self.matingPool[self.x].crossOver(self.matingPool[self.y])

	def mutate(self):
		self.child.mutate()

