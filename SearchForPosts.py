import sqlite3 
from PostQuery import QuestionQuery
from PostQuery import AnswerQuery

class SearchForPosts:
	"""
	Handles database queries for SearchForPostsScreen

	This module handles calls to the database and parses the
	data returned for easier handling
	"""
	def __init__(self, dbName):
		"""
		Creates an instance of SearchForPosts

		parameters:
			dbName:
				A String object containing the name of the
				database
		Returns:
			An instance of SearchForPosts
		"""
		self.__db__ = sqlite3.connect(dbName)
	
	def getPosts(self, keywords):
		"""
		Calls various methods to get a list of questions and answers
		which contain the keyword in some form and the priority that said post
		should recieve it then sorts the posts returned by priority before returning a List
		of PostQueries
		
		Parameters:
			keywords:
				A List of String objects containing keywords provided by the user
		Returns:
			A sorted List of PostQuery objects
		"""
		questions = self.getQuestions(keywords)
		answers = self.getAnswers(keywords)
		postList = questions + answers
		postList.sort(key = lambda x:x[1], reverse=True)

		sortedList = []
		for post in postList:
			sortedList.append(post[0])
		return sortedList
		

	def getQuestions(self, keywords):
		"""
		Queries the database to get post IDs of any questions
		containing any of the keywords in some form

		Parameters:
			keywords:
				A List of String objects containing keywords provided by the
				user
		Returns:
			A List of QuestionQuery objects which contain at least one keyword
		"""
		postIDs = []
		posts = []

		questions = []
		cursor = self.__db__.cursor()
		
		#For each word in keywords grab any question that contains that keyword 
		for word in keywords:
			cursor.execute('''
				SELECT DISTINCT p.pid 
				FROM posts p, questions q
				LEFT OUTER JOIN
				(
					SELECT pid, tag
					FROM tags
				) AS t ON p.pid = t.pid
				WHERE (p.pid = q.pid)  
				AND (p.title LIKE (?) OR p.body LIKE (?) OR (p.pid = t.pid AND t.tag LIKE (?)))''', (word,word,word))
			matchedPosts = (cursor.fetchall())
			for pid in matchedPosts:
				postIDs.append(pid[0])
		
		#For each postID returned from the previous query orgainize the data in a more useable manner
		for postID in postIDs:
			found = False
			if len(posts) > 0:
				for post in posts:
					if post[0] == postID:
						found = True
				if not found:
					posts.append([postID, postIDs.count(postID)])
			else:
				posts.append([postID, postIDs.count(postID)])		
		
			
		#For each Post ID query the database and return information about that post which is a question
		for post in posts:
			cursor.execute('''SELECT DISTINCT p.title, voteCount, answerCount, p.body, p.pid 
					FROM posts p, 
					(
						SELECT p.pid, COUNT(a.pid) AS answerCount 
						FROM posts p, questions q 
						LEFT OUTER JOIN answers a ON q.pid = a.qid AND p.pid = q.pid
						GROUP BY p.pid
					) AS a,
					(
						SELECT p.pid AS pid, COUNT(v.pid) AS voteCount 
						FROM posts p, questions q 
						LEFT OUTER JOIN votes v ON p.pid = v.pid 
						WHERE p.pid = q.pid GROUP BY p.pid
					) as v
					WHERE v.pid = p.pid AND p.pid = a.pid AND p.pid LIKE (?)''', (str(post[0]),))
			cursorResult = cursor.fetchone()
			questions.append([QuestionQuery(cursorResult[0],cursorResult[1],cursorResult[2],cursorResult[3],cursorResult[4]), post[1]])
		return questions
		
	def getAnswers(self, keywords):
		"""
		Queries the database to get post IDs of any answers
		containing any of the keywords in some form

		Parameters:
			keywords:
				A List of String objects containing keywords provided by the
				user
		Returns:
			A List of AnswerQuery objects which contain at least one keyword
		"""
		postIDs = []
		posts = []

		answers = []
		
		cursor = self.__db__.cursor()
		#For each keyword find the post ID of any answers containing said word
		for word in keywords:
			cursor.execute('''
				SELECT DISTINCT p.pid
				FROM posts p, answers a
				LEFT OUTER JOIN
				(
					SELECT pid, tag
					FROM tags 
				) AS t ON p.pid = t.pid
				WHERE p.pid = a.pid
				AND (p.title LIKE (?) OR p.body LIKE (?) OR (p.pid = t.pid AND t.tag LIKE (?)))''', (word,word,word))
			matchedPosts = cursor.fetchall()
			for pid in matchedPosts:
				postIDs.append(pid[0])
		#For each post ID returned by the previous query orgainize that data in a more useful manner
		for postID in postIDs:
                        found = False
                        if len(posts) > 0:
                                for post in posts:
                                        if post[0] == postID:
                                                found = True
                                if not found:
                                        posts.append([postID, postIDs.count(postID)])
                        else:
                                posts.append([postID, postIDs.count(postID)])
        #For each Post ID query the database and return information about that answer post
		for post in posts:
			cursor.execute('''
				SELECT DISTINCT p.title, voteCount, p.body, p.pid
				FROM posts p, answers a,
				(
					SELECT p.pid AS pid, COUNT(v.pid) AS voteCount 
					FROM posts p, answers a 
					LEFT OUTER JOIN votes v ON p.pid = v.pid 
					WHERE p.pid = a.pid GROUP BY p.pid
				) as v
				WHERE v.pid = p.pid AND p.pid = a.pid AND p.pid like (?)''', (str(post[0]),))
			
			cursorResult = cursor.fetchone()
			answers.append([AnswerQuery(cursorResult[0],cursorResult[1],cursorResult[2],cursorResult[3]), post[1]])
		return answers
			
			
