import sqlite3

class Tag:
	def __init__(self, dbName):
		self.__connection__ = sqlite3.connect(dbName)
	
	def addTag(self, pid, tag):
		cursor = self.__connection__.cursor()
		cursor.execute("INSERT INTO tags VALUES (?, ?)", (tag, pid))
		self.__connection__.commit()
		return 0

