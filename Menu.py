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

		self.__terminal__.clear()

	def addMenuItem(self, string):
		self.__menuItems__.append(string)
		self.__length__ += 1
	
	
	def clearMenu(self):
		self.__menuItems__ = []
		self.__length__ = 0

	def printItems(self):
		for i, menuItem in enumerate(self.__menuItems__):
			print(str(i+1) + ". " + self.__menuItems__[i])
		print("\n")
	
	def isNumericalSelection(self, userInput):
		try:
			userInput = int(userInput)
			if userInput <= self.__length__ and userInput >= 1:
				return True
			else:
				return False
		except Exception:
			return None
	
	def printScreen(self):
		while True:
			self.printItems()
			userInput = input("Type the number of the item you would like to select: ")
			try:
				userInput = int(userInput) - 1
				if (userInput <= self.__length__ - 1 and userInput >= 0):
					return userInput
				else:
					input("Invalid selection, press enter to continue: ")
			except Exception:
				try:
					if userInput.upper() == "EXIT":
						return None
				except Exception:
					input("Invalid input, press enter to continue: ") 
			self.__terminal__.clear()

if __name__ == "__main__":
	from Terminal import Terminal
	menu = Menu(Terminal())
	menu.addMenuItem("Just")
	menu.addMenuItem("A")
	menu.addMenuItem("Test")
	print(menu.printScreen())
