import sqlite3

class Tag:
	"""
	Tag handles TagScreen's calls to database

	This module provides an interface for TagScreen to interface
	with the database
	"""
	def __init__(self, dbName):
		"""
		Creates an instance of Tag

		Parameters:
			dbName:
				A String object containing the name of the
				database
		Returns:
				An instance of Tag
		"""
		self.__connection__ = sqlite3.connect(dbName)
	
	def addTag(self, pid, tag):
		"""
		Adds a tag to the specified post

		Parameters:
			pid:
				A String object containing the ID of the post
				to be tagged
			tag:
				A String object containing the tag with which post
				will be tagged
		"""
		tag = tag.upper()
		cursor = self.__connection__.cursor()
		cursor.execute("SELECT tag FROM tags WHERE pid = ? AND tag LIKE(?)", (pid, "%"+tag+"%"))
		if cursor.fetchone() is None:
			cursor.execute("INSERT INTO tags VALUES (?, ?)", (pid, tag))
			self.__connection__.commit()
		else:
			raise ValueError("Post has already been tagged with " + tag)
