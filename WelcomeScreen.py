class WelcomeScreen:
	"""
	A Screen which is used to welcome the user.

	This module is used to welcome the user and asks
	the user for their status which is either registered
	or not registered.
	"""
	def __init__(self, terminal):
		"""
		Creates an instance of WelcomeScreen, which is the UI interface for welcoming users to the
		program. Gets user input for deciding whether the user needs to register or login
		Parameters:
			Terminal: 
				Terminal object. Used as an interface between this module and the terminal of the OS
		Returns:
			An instance of WelcomeScreen
		"""
		self.__terminal__ = terminal
		self.__terminal__.clear()

	def printTitle(self):
		"""
		Prints main elements of the UI
		"""
		self.__terminal__.printCenter("--- Welcome User ---")
		self.__terminal__.printCenter("(Type exit to quit at any time)")
		
	def printScreen(self):
		"""
		The main loop of the module. Prints the title and get's users input on whether they
		are registering or logging in
		"""
		while True:
			self.printTitle()
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
