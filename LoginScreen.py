from LoginUser import LoginUser
class LoginScreen:
	"""
	A screen which handles logging in and the processes
	associated within it.

	This module is responsible for providing the UI of the log in
	screen as well as handleing calls to the database to authenticate
	users. 
	"""
	
	def __init__(self, terminal):
		self.__terminal__ = terminal
		self.__terminal__.clear()
			
	def printTitle(self):
		self.__terminal__.printCenter("Login Screen")
	
	def printScreen(self):
		self.printTitle()
		uid = input("Enter UserID: ")
		password = input("Enter Password: ")

if __name__ == "__main__":
	from Terminal import Terminal
	loginScreen = LoginScreen(Terminal())
	loginScreen.printScreen()
