from SearchForPosts import SearchForPosts
from Menu import Menu
from CheckInput import CheckInput

class SearchForPostsScreen:
	POSTPERPAGE = 5
	"""
	SearchForPostsScreen provides the ui for
	the search for posts function of the application.

	This module allows the user to interface with the SearchForPosts
	module.
	"""
	def __init__(self, terminal):
		self.__terminal__ = terminal
		self.__SearchForPosts__ = SearchForPosts(terminal.getDBName())
		self.__menu__ = Menu(terminal)		
		self.__chkinp__ = CheckInput()		

	def printTitleKeyword(self):
		self.__terminal__.clear()
		self.__terminal__.printCenter("Search for Posts")
		self.__terminal__.printCenter("Enter terms delimited by commas")

	def printTitlePostSelect(self):
		self.__terminal__.clear()
		self.__terminal__.printCenter("Posts Matching Keywords")
		self.__terminal__.printCenter("Type the number of the post you would like to select")
		self.__terminal__.printCenter("Type n to go to the next page or p to go to the previous page")
		print("Post Title" + "|" + "Votes" + "|" + "Answers")

	def printScreen(self):
		self.printTitleKeyword()
		userInput = input("Enter search term(s): ")
		searchTermList = userInput.split(",")
		for i, string in enumerate(searchTermList):
			searchTermList[i] = "%" + string.strip() + "%"
		posts = self.__SearchForPosts__.getPosts(searchTermList)
		
		postSelected = False
		index = 0
		maxIndex = len(posts) - 1 
		inputMessage = "Type number next to desired post (n for next) (p for prev): "
		
		while not postSelected:
			manyRemainingPosts = self.getMenu(posts, index)
			self.printTitlePostSelect()
			self.__menu__.printItems()

			if not manyRemainingPosts:
				userInput = input(inputMessage)
				if self.__chkinp__.checkAlphaNumeric(userInput):
					if self.__chkinp__.checkEscape(userInput):
						return None
					isPost = self.__menu__.isNumericalSelection(userInput)
					if isPost:
						selectedPost = posts[index+int(userInput)-1]
						return(selectedPost[0], [1])
					elif isPost is False:
						print("Selection is outside of possible range!")
					elif isPost is None:
						if userInput == "n":
							print("No posts on next page")
						elif userInput == "p" and index - POSTPERPAGE < 0:
							print("No posts on previous page")
						elif userInput == "p" and index - POSTPERPAGE >= 0:
							index -= POSTPERPAGE
						else:
							print("Invalid input!")
				else:
					print("Your input contains a character that is neither a letter or a number!")

			else:
				userInput = input(inputMessage)
				if self.__chkinp__.checkAlphaNumeric(userInput):
					if self.__chkinp__.checkEscape(userInput):
						return None
					isPost = self.__menu__.isNumericalSelection(userInput)
					if isPost:
						selectedPost = posts[index+int(userInput)-1]
						return(selectedPost[0], selectedPost[2])
					elif isPost is False:
						print("Selection is outside of possible range!")
					elif isPost is None:
						if userInput == "n":
							index += POSTPERPAGE
						elif userInput == "p" and index - POSTPERPAGE >= 0:
							index -= POSTPERPAGE
						elif userInput == "p" and index - POSTPERPAGE <= 0:
							print("No posts on previous page")
						else:
							print("Invalid input!")					
				else:
					print("Your input contains a character that is netiher a letter or a number!")
			input("Press enter to continue with action taken: ")

	def getMenu(self, posts, index):
		POSTPERPAGE = 5
		maxIndex = len(posts) - 1 

		self.__menu__.clearMenu()
		if (index + POSTPERPAGE > maxIndex):
			for post in posts[index:]:
				if isinstance(post, QuestionQuery):
					self.__menu__.addMenuItem(str(post.title)+ " | " + str(post.voteCount) + " | " + str(post.answerCount))
				else:
					self.__menu__.addMenuItem(str(post.title) + " | " + str(post.voteCount))
			return False
		else:
			for i in range(index, index+POSTPERPAGE):
				if isinstance(post, QuestionQuery):
					self.__menu__.addMenuItem(str(posts[i].title) + " | " + str(posts[i].voteCount) + " | " + str(posts[i].answerCount))
				else:
					self.__menu__.addMenuItem(str(posts[i].title) + " | " + str(posts[i].voteCount))
			return True
if __name__ == "__main__":
	from Terminal import Terminal
	searchPostScreen = SearchForPostsScreen(Terminal())
	searchPostScreen.printScreen()
