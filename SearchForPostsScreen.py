class SearchForPostsScreen:
	"""
	SearchForPostsScreen provides the ui for
	the search for posts function of the application.

	This module allows the user to interface with the SearchForPosts
	module.
	"""
	def __init__(self, terminal):
		self.__terminal__ = terminal
			
	def printTitle(self):
		self.__terminal__.clear()
		self.__terminal__.printCenter("Search for Posts")
		self.__terminal__.printCenter("Enter terms delimited by commas")
	def printScreen(self):
		self.printTitle()
		userInput = input("Enter search term(s): ")
		searchTermList = userInput.split(",")
		for i, string in enumerate(searchTermList):
			searchTermList[i] = string.strip()
		return searchTermList

if __name__ == "__main__":
	from Terminal import Terminal
	searchPostScreen = SearchForPostsScreen(Terminal())
	print(searchPostScreen.printScreen())
