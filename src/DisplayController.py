from abc import ABC, abstractmethod
import os

class DisplayControllerInterface():

	def _init_(self):
		self.maxHight = 20
		self.maxWidth = 20

	def clearScreen(self):
		if os.name == "nt":
			os.system('cls')  # For Windows
		else:
			os.system('clear')  # For Linux/OS X

	def drawSquar(self,side,x,y):
		"""Upper Left Cords """
		for i in range(y):
			print("\n")
		for i in range(side):
			line = ""
			for j in range(x):
				line += " "
			for k in range (side):
				line += "#"
			print(line)







def printLine():
	print("diplay")