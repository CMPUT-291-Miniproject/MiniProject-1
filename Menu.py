class Menu:
	"""
	Menu is a way for the user to interface with the program.

	Menu is a module which displays items that are numbered and get's user
	input on which option they would like to select from said items

	"""
	def __init__(self, terminal):
		self.__terminal__ = terminal
		self.__menuItems__ = []
		self.__length__ = 0

	def addMenuItem(self, string):
		self.__menuItems__.append(string)
		self.__length__ += 1
	
	def printScreen(self):
		self.__terminal__.clear()

		for i, menuItem in enumerate(self.__menuItems__):
			print(str(i+1) + ". " + self.__menuItems__[i])
		print("\n")
	
	def getUserSelection(self):
		while True:
			self.printScreen()
			try:
				userInput = int(input("Type the number next to the selection you would like to make: ")) - 1
				if (userInput <= self.__length__ - 1 and userInput >= 0):
					print(self.__menuItems__[userInput])
					return userInput
				else:
					input("Invalid selection, press enter to continue: ")
			except Exception:
				input("Invalid input, press enter to continue: ") 
			self.__terminal__.clear()
