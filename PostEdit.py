import sqlite3
class PostEdit():
	def __init__(self, dbName):
		self.__db__ = sqlite3.connect(dbName)	

	def changeTitle(self, pid, title):
		cursor = self.__db__.cursor()
		cursor.execute("UPDATE posts SET title = ? WHERE pid = ?", (title, pid))
		self.__db__.commit()
		cursor.close()

	def changeBody(self, pid, body):
		cursor = self.__db__.cursor()
		cursor.execute("UPDATE posts SET body = ? WHERE pid = ?", (body, pid))
		self.__db__.commit()
		cursor.close()

if __name__ == "__main__":
	pid = "6JcK"
	title = "Dancing is incredible!"

	pe = PostEdit("Miniproject_1.db")
	pe.changeTitle(pid, title)
		
	body = "I dance all the time but I was wondering, why do we dance? Does anyone know?"
	pe.changeBody(pid, body)
 
