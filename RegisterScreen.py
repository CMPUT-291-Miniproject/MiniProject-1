from RegisterUser import RegisterUser
from CheckInput import CheckInput

class RegisterScreen:
	"""
	RegisterScreen provides an interface for users
	such that they can register.
	"""
	def __init__(self, terminal, dbName):
		"""
		Creates an instance of RegisterScreen
		
		@parameters
			terminal: A Terminal object that allows this
				  program to interact with the terminal
			dbName: A String object containing the name of the
				database for creation of RegisterUser object
		"""
		self.__terminal__ = terminal
		self.__checkInput__ = CheckInput()
		self.__registerUser__ = RegisterUser(dbName)

	def printScreen(self):
		"""
		Prints title, gathers data, checks data for escape or errors,
		and if there are neither inserts data as a user in the database 
	
		@return
			None: In the case where the user was not registered
			userID: In the case where the user was registered
		"""
		validInput = False
		while not validInput:
			self.__terminal__.clear()
			self.printTitle()

			userID = input("Enter Desired UserID: ")
			if self.__checkInput__.checkEscape(userID) or userID.lower().strip() == 'exit':
				return None			

			name = input("Your Name: ")
			if self.__checkInput__.checkEscape(name) or userID.lower().strip() == 'exit':
				return None

			city = input("Your City: ")
			if self.__checkInput__.checkEscape(city) or userID.lower().strip() == 'exit':
				return None

			password = input("Enter Desired Password: ")
			if self.__checkInput__.checkEscape(password) or userID.lower().strip() == 'exit':
				return None
			
			print("\n\n\n")
			validInput = self.__registerUser__.register(userID, name, city, password)
			input("Press enter to continue: ") 
		
		return userID

	def printTitle(self):
		"""
		Prints title of screen as well as instructions for user
		"""
		self.__terminal__.printCenter("Register")
		self.__terminal__.printCenter("--UserID must contain exactly 4 alphanumeric characters--")
		self.__terminal__.printCenter("--Name must contain only letters--")
		self.__terminal__.printCenter("--City must contain only letters--")
		self.__terminal__.printCenter("--password must contain only alphanumeric characters--")
		self.__terminal__.printCenter("--Press escape or input exit at any time to go back.")

if __name__ == "__main__":
	from Terminal import Terminal
	registerScreen = RegisterScreen(Terminal(), "Miniproject_1.db")
	print(registerScreen.printScreen())
	
	
	
