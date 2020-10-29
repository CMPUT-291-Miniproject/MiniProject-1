import sqlite3

class LoginUser:
	"""
	LoginUser handles LoginScreen's calls to database

	This module provides an interface for LoginScreen to interface
	with the database
	"""
	
	#This will return true or false depending on whether the uid and password check out
	def logIn(dbName, uid, password):
		"""
		Framework for logging into the program. The implemetation for doing so lies in LoginScreen.
		Connects to the database and checks for a uid and password that directly matches the user's input. Literally the same as any login screen, except the passwords aren't encrypted. 
		
		Parameters:
			dbName: String. Name of the database, entered as an arguement on runtime of main.py
			uid: 4 char String. User inputted ID, which is verified with a passwork in this method.
			password: Case Sensitive String. User inputted, which is checked in this method.
			
		Returns: Boolean. True if the login was successful, false otherwise.
		"""
		
		#connect to database
		db = sqlite3.connect(dbName)
		cur = db.cursor()
		
		#check for correct uid and password
		cur.execute("SELECT uid, pwd FROM users WHERE uid = ? AND pwd = ?", (uid, password))
		
		#grabs the first result, if it exists
		check = cur.fetchone()
		
		#If the result exists, return true. return false otherwise.
		if check is None:
			return False
		else:
			return True	
		