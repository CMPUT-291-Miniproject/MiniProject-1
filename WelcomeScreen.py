class WelcomeScreen:
	"""
	A Screen which is used to welcome the user.

	This module is used to welcome the user and asks
	the user for their status which is either registered
	or not registered.
	"""
	def __init__(self, terminal):
		self.__terminal__ = terminal
		self.__terminal__.clear()

	def printWelcome(self):
		self.__terminal__.printCenter("--- Welcome User ---")
		self.__terminal__.printCenter("(Type exit to quit at any time)")
		
	def printScreen(self):
		while True:
			self.printWelcome()
			userInput = input("Are you an existing user? (Type y or n): ").upper()
			if userInput == "Y":
				return True
			elif userInput == "N":
				return False
			elif userInput == "EXIT":
				return None
			else:
				input("Invalid input, press enter to continue: ")
				self.__terminal__.clear()


if __name__ == "__main__":
	from Terminal import Terminal
	welcomeScreen = WelcomeScreen(Terminal())
	welcomeScreen.printScreen()
