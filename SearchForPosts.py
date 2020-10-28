import sqlite3 
class SearchForPosts:
	def __init__(self, dbName);
		connection = sqlite3.connect(dbName)
		self.__db__ = connection.cursor()
	def getPosts(keywords):
		self.__db__
