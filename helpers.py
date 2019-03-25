from termcolor import colored
from Individual import target

def colorize(value):
	for i in range(len(target)):
		if value[i] == target[i]:
			print(colored(value[i],"green"),end="")
		else:
			print(colored(value[i],"red"),end="")
		
def summarize(gen, phr, fit):
	print(f"Generation #{gen:3}: ",end="")
	colorize(phr)
	print(f"Score: {fit:2}/{len(target)}")
	
	
