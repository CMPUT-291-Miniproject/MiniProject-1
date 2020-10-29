import sqlite3
import string
import random

class PostQuestion:
	
	def __init__(self, dbName, uid):
		"""
		Creates an object that can be used to post a question to the forum.
		
		Parameters:
			dbName: String. The name of the database, needed to connect to said database.
			uid: User ID of the poster. Needed for adding question to database. 
			
		Returns: N/A
		"""
		self.__db__ = dbName
		self.__uid__ = uid
		
	def add_question(self, title, body):
		"""
		Adds a question to the database, using a private function __get_pid__ to generate a unique PID.
		
		Parameters:
			Title: String. The title of the question.
			Body: String. The content of the question.
		
		Additional information:
			UID: 4 char string. Unique to each user, created from registerUser.py.
			self.__pid__: 4 char string. Unique to each post and created in __get_pid__.
			
		Returns:
			N/A
		"""
		#pid is handled inside, as well as pdate
		db = sqlite3.connect(self.__db__)
		
		#Gets unique PID for a post
		pid = self.__get_pid__()
		
		"""
		The next statements enter the question into the database as a post, and then enters it as a question.
		After doing so, it commits the additions and closes the database.
		"""
		#db entry visualization               pid   pdate    title body poster
		db.execute("INSERT INTO posts VALUES (?, DATE('now'), ?, ?, ?)", (pid, title, body, self.__uid__))
		#db entry visualization                  pid  theaid
		db.execute("INSERT INTO questions VALUES (?, ?)", (pid, None))
		db.commit()
		db.close()
		
		
	def __get_pid__(self):
		"""
		Generates a unique post ID, which is checked in the database to verify uniqueness.
		
		Parameters: N/A
		
		Returns: 
			pid: 4 character string
		"""
		db = sqlite3.connect(self.__db__)
		cur = db.cursor()
		chars = string.ascii_letters + string.digits
		while True:
			pid = ""
			for i in range(4):
				pid += chars[random.randrange(0, len(chars))]
			
			cur.execute("SELECT pid FROM posts WHERE pid = ?", (pid,))
			
			if cur.fetchone() is None:
				break
		return pid
				
if __name__ == "__main__":
	question = PostQuestion('Miniproject_1.db')
	question.add_question("This is a test.", "I really hope this works.", "Ahbz")
		