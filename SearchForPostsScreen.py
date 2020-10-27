class SearchForPostsScreen:
	"""
	SearchForPostsScreen provides the ui for
	the search for posts function of the application.

	This module allows the user to interface with the SearchForPosts
	module.
	"""
	def __init__(self, terminal):
		self.__terminal__ = terminal
			
	def printScreen(self):
		self.__terminal__.clear()
		self.__terminal__.printCenter("Search for Posts")
		self.__terminal__.printCenter("Enter terms delimited by commas")
	def getKeyWords(self):
		userInput = input("Enter search term(s): ")
		searchTermList = userInput.split(",")
		for i, string in enumerate(searchTermList):
			searchTermList[i] = string.strip()
		print(searchTermList)
