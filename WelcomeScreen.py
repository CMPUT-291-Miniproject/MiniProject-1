from os import system, name
import shutil

class WelcomeScreen:
	def __init__(self):
		system('clear')

	def welcomeUser(self):
		screenSize = shutil.get_terminal_size().columns
		print("-----Welcome User-----".center(screenSize))
		print("(Type exit to quit at any time)\n\n\n".center(screenSize))
		
	def checkUserExistence(self):
		while True:
			userInput = input("Are you an existing user? (Type y or n): ").upper()
			if userInput == "Y":
				return True
			elif userInput == "N":
				return False
			elif userInput == "EXIT":
				return None
			else:
				input("Invalid input, press enter to continue: ")
				system('clear')

