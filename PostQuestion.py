import sqlite3
import string
import random

class PostQuestion:
	
	def __init__(self, dbName):
		self.__db__ = dbName
		
	def add_question(self, title, body, poster):
		#pid is handled inside, as well as pdate
		db = sqlite3.connect(self.__db__)
		
		pid = self.__get_pid__()
		
		#db entry visualization               pid   pdate    title body poster
		db.execute("INSERT INTO posts VALUES (?, DATE('now'), ?, ?, ?)", (pid, title, body, poster))
		#db entry visualization                  pid  theaid
		db.execute("INSERT INTO questions VALUES (?, ?)", (pid, None))
		db.commit()
		db.close()
		
		
	def __get_pid__(self):
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
			
		
		
		
		
		
		
	'''
	def __check_uid__(self):
		db = sqlite3.connect(self.__dbName__)
		cursor = db.cursor()
		#finish later
		
	def add_user(self, uid, name, pwd, city):
	#users(uid, name, pwd, city, crdate)
		db = sqlite3.connect(self.__dbName__)
		db.execute("INSERT INTO users VALUES(?, ?, ?, ?, DATE('now')", (uid, name, pwd, city))
		'''
		