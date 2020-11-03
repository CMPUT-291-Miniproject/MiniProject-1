import sqlite3 
from collections import namedtuple
class SearchForPosts:
	def __init__(self, dbName):
		self.__db__ = sqlite3.connect(dbName)
	
	def getPosts(self, keywords):
		questions = self.getQuestions(keywords)
		answers = self.getAnswers(keywords)
		postList = questions + answers
		postList.sort(key = lambda x:x[1], reverse=True)

		sortedList = []
		for post in postList:
			sortedList.append(post[0])
		return sortedList
		

	def getQuestions(self, keywords):
		#Each keyword gets its own list
		#resulting in a list of lists
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
		
			
		#query database for each postid within posts appends a tuple with the post information and priority of said post to  
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
			QuestionQuery = namedtuple('QuestionQuery', ['title', 'voteCount', 'answerCount', 'body', 'pid'])
			cursorResult = cursor.fetchone()
			questions.append([QuestionQuery(cursorResult[0],cursorResult[1],cursorResult[2],cursorResult[3],cursorResult[4]), post[1]])
		return questions
		
	def getAnswers(self, keywords):
		#Each keyword gets its own list
		#resulting in a list of lists
		postIDs = []
		posts = []

		answers = []
		
		cursor = self.__db__.cursor()

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
			AnswerQuery = namedtuple('AnswerQuery', ['title', 'voteCount', 'body', 'pid'])
			cursorResult = cursor.fetchone()
			answers.append([AnswerQuery(cursorResult[0],cursorResult[1],cursorResult[2],cursorResult[3]), post[1]])
		return answers
			
			
