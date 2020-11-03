import sqlite3
class Vote:
		
	def __init__(self, dbName):
		"""
		Class to interact with votes.
		
		Parameters:
			dbName: String. Name of database.
			
		Returns:
			N/A
		"""
		self.__dbName__ = dbName
		
	def check_vote(self, pid, uid):
		"""
		Checks to see if a user has already voted on a post.
		
		Parameters:
			pid: 4 char String. The ID of the post to check for votes on
			uid: 4 char String. The ID of the user to for a vote.
		
		Returns:
			Boolean. True if the user has voted on that post already, false if they have not.
		"""
		
		#connect to database
		db = sqlite3.connect(self.__dbName__)
		cur = db.cursor()
		
		#grab potential vote, then close the db
		cur.execute("SELECT uid FROM votes WHERE uid = ? AND pid = ?", (uid, pid))
		result = cur.fetchone()
		db.close()
		
		#If there isn't a vote from the user on this post, return False
		if result is None:
			return False
		#if there is a vote from the user on the post, return True
		else:
			return True
			
			
	def vote(self, pid, uid):
		"""
		Allows the user to vote on a post. check_vote should be used before using this method to check for duplicate vote.
		
		Parameters:
			pid: 4 char String. The ID of the post to check for votes on
			uid: 4 char String. The ID of the user to for a vote.
			
		Returns:
			N/A
		"""
		db = sqlite3.connect(self.__dbName__)
		cur = db.cursor()
		vno = self.vote_count(pid) + 1
		
		cur.execute("INSERT INTO votes VALUES (?, ?, DATE('now'), ?)", (pid, vno, uid))
		db.commit()
		
		db.close()
		
	def vote_count(self, pid):
		"""
		Getter for total number of votes on a post.
		
		Parameters:
			pid: 4 char String. The ID of the post to check for votes on
			
		Returns:
			Int. The number of votes.
		"""
		db = sqlite3.connect(self.__dbName__)
		cur = db.cursor()
		
		cur.execute("SELECT COUNT(pid) FROM votes WHERE pid = ?", (pid,))
		
		return cur.fetchone()[0]
		

if __name__ == "__main__":
	vota = Vote('Miniproject_1.db')
	print(vota.vote_count("DrH1"))
	"""
	if vota.check_vote('ouI5', 'qxgy'):
		vota.vote('ouI5', 'qxgy')
	else:
		print("NOPE")"""
		