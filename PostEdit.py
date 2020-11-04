import sqlite3
class PostEdit():
	"""
	PostEdit handles PostEditScreen's calls to database

	This module provides an interface for PostEditScreen to interface
	with the database
	"""

	def __init__(self, dbName):
		"""
		Creates an instance of PostEdit, which is an interface that handles 
		calls to the database from PostEditScreen
		
		Parameters:
			dbName: A String object containing the name of the database to be interfaced with
			
		Returns: An instance of PostEdit
		"""
		self.__db__ = sqlite3.connect(dbName)	

	def changeTitle(self, pid, title):
		"""
		Changes the title of a post in the database

		Parameters:
			pid:
					A String object containing the ID of the post whose title
					is being changed
			title: 
					A String object that contains the new title that post
					will have if this method succeeds
		"""
		cursor = self.__db__.cursor()
		cursor.execute("UPDATE posts SET title = ? WHERE pid = ?", (title, pid))
		self.__db__.commit()
		cursor.close()
		return self.updatePost()

	def changeBody(self, pid, body):
		"""
		Changes the body of a post in the database

		Parameters:
			pid:
					A String object containing the ID of the post whose title
					is being changed
			body: 
					A String object that contains the new body that post
					will have if this method succeeds
		"""
		cursor = self.__db__.cursor()
		cursor.execute("UPDATE posts SET body = ? WHERE pid = ?", (body, pid))
		self.__db__.commit()
		cursor.close()
		return self.updatePost()

	def updatePost(self):
		"""
		Updates post after an edit

		Returns:
			A PostQuery object
		"""
		c = self.__db__.cursor()
		c.execute("SELECT title, body FROM posts WHERE pid = ?", (self.__post__.pid,))
		post = cursor.fetchone()
		self.__post__.title = post[0]
		self.__post__.body = post[1]
		return post

if __name__ == "__main__":
	pid = "6JcK"
	title = "Dancing is incredible!"

	pe = PostEdit("Miniproject_1.db")
	pe.changeTitle(pid, title)
		
	body = "I dance all the time but I was wondering, why do we dance? Does anyone know?"
	pe.changeBody(pid, body)
 
