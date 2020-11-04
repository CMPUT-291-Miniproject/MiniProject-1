import sqlite3
from Terminal import Terminal
from PostQuery import QuestionQuery
from PostQuery import AnswerQuery

class AcceptedAnswer:
	
	def __init__(self, terminal, apid):
		"""
		Object used to mark a post as accepted. Only privileged users can use this, but that requirement is not reflected in this class.
		
		Parameters:
			terminal: Terminal object. Used to get database name.
			apid: 4 char String. The answer ID.
			
		Returns:
			N/A
		"""
		self.__terminal__ = terminal
		self.__apid__ = apid
		
	
	def acceptAnswer(self):
		"""
		Accepts the answer and reflects the change in the database.
		
		Parameters: Self
		
		Returns: N/A
		"""
		
		#connect to db and grab a cursor
		db = sqlite3.connect(self.__terminal__.getDBName())
		cur = db.cursor()
		
		#grab the question pid
		cur.execute("SELECT qid FROM answers WHERE pid = ?", (self.__apid__,))
		qid = cur.fetchone()
		
		#update theaid in the question to the answer pid
		cur.execute("UPDATE questions SET theaid = '{}' WHERE pid = ?".format(self.__apid__), (qid[0],))
		
		#commit and close the db
		db.commit()
		db.close()
		