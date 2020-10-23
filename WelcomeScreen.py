from os import system, name
class WelcomeScreen:
	def __init__(self):
		system('cls')

	def welcomeUser(self):
		print("--Welcome User---")
		
	def checkUserExistence(self):
		while True:
			print("Are you an existing user? (Type y or n)")
			userInput = input().upper();
			if userInput == "Y":
				return True
			elif userInput == "N":
				return False
			else:
				print("Invalid Input, please type either y or n")
				print("Press Enter key to continue")
				input()
				system('cls')

