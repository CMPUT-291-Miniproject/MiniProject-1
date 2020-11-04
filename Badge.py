import sqlite3
class Badge:
	"""
	Tag handles TagScreen's calls to database

	This module provides an interface for TagScreen to interface
	with the database
	"""
	def __init__(self, dbName, post):
		"""
		Creates an instance of Badge

		Parameters:
			dbName:
				A String object containing the name of the
				database
			post:
				A PostQuery object containing information
				about the post being given a badge
		Returns:
				An instance of Badge
		"""
		self.__db__ = sqlite3.connect(dbName)

	def getBadgeNames(self):
		"""
		Grabs badge names from the database and puts them in a 
		List of String objects

		Returns:
			A List of String objects containing badge names
		"""
		badges = []

		cursor = self.__db__.cursor()
		cursor.execute("SELECT bname FROM badges")

		for row in cursor.fetchall():
			badges.append(row[0])
		cursor.close()
		return badges

	def addBadge(self, badgeName, pid):
		"""
		Attempts to add the badge to the post given
		that the adding of the badge does not violate
		the rules of the database

		Parameters:
			badgeName:
				A String object containing the name of the
				badge to be given to the user
			pid:
				A String object containing the posts ID
		"""

		cursor = self.__db__.cursor()
		
		cursor.execute("SELECT poster FROM posts WHERE pid = ?", (pid,))
		uid = cursor.fetchone()[0]

		try:
			cursor.execute("INSERT INTO ubadges VALUES(?, DATE('now'), ?)", (uid, badgeName))
			input("Gave the user the badge. Press enter to continue:")
		except sqlite3.IntegrityError as integError:
			input("Cannot give a user multiple badges in one day! Press enter to continue:")

		self.__db__.commit()

		cursor.close()

if __name__ == "__main__":
	b = Badge("Miniproject_1.db")
	print(b.getBadgeNames())
	b.addBadge("socratic question", )
