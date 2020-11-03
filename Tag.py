import sqlite3

class Tag:
	"""
	
	"""
	def __init__(self, dbName):
		"""

		"""
		self.__connection__ = sqlite3.connect(dbName)
	
	def addTag(self, pid, tag):
		"""
		"""
		tag = tag.upper()
		cursor = self.__connection__.cursor()
		cursor.execute("SELECT tag FROM tags WHERE pid = ? AND tag LIKE(?)", (pid, "%"+tag+"%"))
		if cursor.fetchone() is None:
			cursor.execute("INSERT INTO tags VALUES (?, ?)", (pid, tag))
			self.__connection__.commit()
		else:
			raise ValueError("Post has already been tagged with " + tag)
