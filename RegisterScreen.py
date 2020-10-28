from RegisterUser import RegisterUser

class RegisterScreen:

	def __init__(self, terminal):
		self.__terminal__ = terminal
		self.__registerUser__ = RegisterUser()
		
		self.__terminal__.clear()

	def printScreen(self):
		self.printTitle()
		userID = input("Enter Desired UserID: ")
		name = input("Your Name: ")
		city = input("Your City: ")
		password = input("Enter Desired Password: ")

	def printTitle(self):
		self.__terminal__.printCenter("Register")

if __name__ == "__main__":
	from Terminal import Terminal
	registerScreen = RegisterScreen(Terminal())
	registerScreen.printScreen()
	
	
	
