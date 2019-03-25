import Population as plt
from Individual import target
from helpers import summarize
def main():
	population = plt.population()
	population.initializePopulation()
	while (population.bestScore < len(target)):
		for i in range(population.popSize):
			population.pop[i].getfitness()

			if population.pop[i].fitness > population.bestScore:
				population.bestScore = population.pop[i].fitness
				summarize(population.generation, population.pop[i].getContent(), population.bestScore)
			
		parents = population.pop[:] # New Parents for next Generation
		population.pop =[] # New Parent for next Generation
		population.matingPool1(parents)
		for i in range(population.popSize):
			population.selection()
			population.crossOver()
			population.mutate()
			population.pop.append(population.child)	
	population.generation +=1

if  __name__ == "__main__":
	main()


