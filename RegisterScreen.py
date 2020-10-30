from RegisterUser import RegisterUser
from CheckInput import CheckInput

class RegisterScreen:

	def __init__(self, terminal, dbName):
		self.__terminal__ = terminal
		self.__checkInput__ = CheckInput()
		self.__registerUser__ = RegisterUser(dbName)

	def printScreen(self):
		validInput = False
		while not validInput:
			self.__terminal__.clear()
			self.printTitle()

			userID = input("Enter Desired UserID: ")
			if self.__checkInput__.checkEscape(userID):
				return None			

			name = input("Your Name: ")
			if self.__checkInput__.checkEscape(name):
				return None

			city = input("Your City: ")
			if self.__checkInput__.checkEscape(city):
				return None

			password = input("Enter Desired Password: ")
			if self.__checkInput__.checkEscape(password):
				return None
			
			print("\n\n\n")
			validInput = self.__registerUser__.register(userID, name, city, password)
			input("Press enter to continue: ") 
		
		return userID

	def printTitle(self):
		self.__terminal__.printCenter("Register")
		self.__terminal__.printCenter("--UserID must contain exactly 4 alphanumeric characters--")
		self.__terminal__.printCenter("--Name must contain only letters--")
		self.__terminal__.printCenter("--City must contain only letters--")
		self.__terminal__.printCenter("--password must contain only alphanumeric characters--")

if __name__ == "__main__":
	from Terminal import Terminal
	registerScreen = RegisterScreen(Terminal(), "Miniproject_1.db")
	print(registerScreen.printScreen())
	
	
	
