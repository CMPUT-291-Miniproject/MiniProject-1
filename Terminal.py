from os import system
import shutil
import sys

class Terminal:
	"""
	Terminal serves as an interface to interact with the OS terminal.

	Terminal is a module which other modules can use to perform actions
	on the operating systems terminal.
	"""	
	def __init__(self):
		self.__screenSize__ = shutil.get_terminal_size().columns
	
	def clear(self):
		system("clear")
	
	def printCenter(self, string):
		print(string.center(self.__screenSize__))		
	
	def getDBName(self):
		return sys.argv[1]		
