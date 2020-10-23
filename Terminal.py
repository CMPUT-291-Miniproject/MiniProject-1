from os import system
import shutil

class Terminal:
	
	def __init__(self):
		self.__screenSize__ = shutil.get_terminal_size().columns
	
	def clear(self):
		system("clear")
	
	def printCenter(self, string):
		print(string.center(self.__screenSize__))		
		 
