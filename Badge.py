import sqlite3
class Badge:
	def __init__(self, dbName, post):
		self.__db__ = sqlite3.connect(dbName)

	def getBadgeNames(self):
		badges = []

		cursor = self.__db__.cursor()
		cursor.execute("SELECT bname FROM badges")

		for row in cursor.fetchall():
			badges.append(row[0])
		cursor.close()
		return badges

	def addBadge(self, badgeName, pid):
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
