import Population as plt
def main():
	x = plt.population()
	x.initializePopulation()
	print('Now Function')
	x.printPop()
	print("Most Fit: ")
	print(x.calc_MostFit())
	print("Least Fit: ")
	print(x.calc_MinFit())
	print("Second Most Fit: ")
	print(x.calc_Second_MostFit())
if  __name__ == "__main__":
	main()
