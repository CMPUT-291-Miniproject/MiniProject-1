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
		self.__db__ = sqlite3.connect(dbName)
		self.__checkInput__ = CheckInput()

	def register(self, userID, name, city, password):
		if (not self.checkInput(userID, name, city, password)):
			return False 
		cursor = self.__db__.cursor()
		
		cursor.execute("SELECT uid FROM users WHERE uid = ?", (userID,))
		item = cursor.fetchone()

		if (item == None):
			cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?, date("now"))', (userID, name, password, city))
			self.__db__.commit()
			print("User successfully registered!")
			return True
		else:
			print("User already exists with that user ID. please select another user ID!")
			return False
	
	def checkInput(self, userID, name, city, password):
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
		userIDLength = 4
		returnValue = True
	
		if not self.__checkInput__.checkLength(userID, userIDLength):
			print("User ID is not proper length. Ensure User ID is exactly 4 characters!")
			returnValue = False
	
		if not self.__checkInput__.checkAlphaNumeric(userID):
			print("User ID is not Alphanumeric. Ensure User ID only contains letters and numbers!")
			returnValue = False
			
		return returnValue

	def checkName(self, name):
		if not self.__checkInput__.checkAlpha(name):
			print("Name contains characters other than letters. Ensure name only contains letters!")
			return False
		return True

	def checkCity(self, city):
		if not self.__checkInput__.checkAlpha(city):
			print("City contains characters other than letters. Ensure city only contains letters!")
			return False
		return True
	
	def checkPassword(self, password):
		if not self.__checkInput__.checkAlphaNumeric(password):
			print("Password contains characters that are not alphanumeric. Ensure password only contains alphanumeric characters")
			return False
		return True			
