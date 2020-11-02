from CheckInput import CheckInput
import sqlite3
from datetime import datetime

class RegisterUser:
	"""
	RegisterUser allows RegisterUserScreen to interface with the database.

	This module provides an interface for RegisterUserScreen and the
	database to interact
	"""
	def __init__(self, dbName):
		"""
		Creates an instance of RegisterUser

		@params
			dbName: A string containing the name of the
				database containing application data
		"""
		self.__db__ = sqlite3.connect(dbName)
		self.__checkInput__ = CheckInput()

	def register(self, userID, name, city, password):
		"""
		Checks if input is valid and if it is
		inserts data as a user in the database
		
		@params
			userID: A String object that will become the uid if valid
			name: A String object that will become the name of the user if valid
			city: A String object that will become the name of the city which
		      	      the user resides in if valid
			password: A String object that will become the users password
				  if valid

		@return
			Boolean representing whether the user was registered or not 
		"""
		if (not self.checkInput(userID, name, city, password)):
			return False 
		
		cursor = self.__db__.cursor()
		cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?, date("now"))', (userID, name, password, city))
		self.__db__.commit()
		print("User successfully registered!")
		return True
	
	def checkInput(self, userID, name, city, password):
		"""
		Calls various methods to check the validity of input

		@params
			userID: A String object that will become the uid if valid
			name: A String object that will become the name of the user if valid
			city: A String object that will become the name of the city which
		     	      the user resides in if valid
			password: A string object that will become the users password
			          if valid

		@return
			Boolean representing whether the inputs are valid or not
		"""
		returnValue = True
		if not self.checkUserID(userID):
			returnValue = False
		if not self.checkName(name):
			returnValue = False
		if not self.checkCity(city):
			returnValue = False
		if not self.checkPassword(password):
			returnValue = False
		return returnValue
	
	def checkUserID(self, userID):
		"""
		Checks if the userID is the correct length,
		type and whether a user exists with this userID.
		Prints an error message describing the problem on failure

		@params
			userID: A String object that will become the uid if valid
		
		@return
			Boolean representing whether the userID is valid
		"""
		cursor = self.__db__.cursor()
		cursor.execute("SELECT uid FROM users WHERE uid = ?", (userID,))
		item = cursor.fetchone()
		
		userIDLength = 4
		returnValue = True
	
		if not self.__checkInput__.checkLength(userID, userIDLength):
			print("User ID is not proper length. Ensure User ID is exactly 4 characters!")
			returnValue = False
	
		if not self.__checkInput__.checkAlphaNumeric(userID):
			print("User ID is not Alphanumeric. Ensure User ID only contains letters and numbers!")
			returnValue = False
		
		if not item == None:
			print("User already exists with that user ID. Please select another user ID!")
			returnValue = False

		return returnValue

	def checkName(self, name):
		"""
		Checks if the name is of the correct type.
		Prints an error message describing the problem
		on failure.

		@params
			name: A String object that will become the name of the user if valid

		@return
			Boolean representing whether the name is valid 
		"""
		if not self.__checkInput__.checkAlpha(name):
			print("Name contains characters other than letters. Ensure name only contains letters!")
			return False
		return True

	def checkCity(self, city):
		"""
		Checks if the city is of the correct type,
		Prints an error message describing the problem
		on failure.
	
		@params
			city: A String object that will become the city the user
			      resides in if valid

		@return
			Boolean representing whether the city is valid
		"""
		if not self.__checkInput__.checkAlpha(city):
			print("City contains characters other than letters. Ensure city only contains letters!")
			return False
		return True
	
	def checkPassword(self, password):
		"""
		Checks if the password is of the correct type.
		Prints an error message describing the problem
		on failure.
	
		@params
			password: A String object that will become the password
				  of user if valid
	
		@return
			Boolean representing whether the password is valid
		"""
		if not self.__checkInput__.checkAlphaNumeric(password):
			print("Password contains characters that are not alphanumeric. Ensure password only contains alphanumeric characters")
			return False
		return True			
