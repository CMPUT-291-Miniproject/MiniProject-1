from SearchForPosts import SearchForPosts
from Menu import Menu
from CheckInput import CheckInput
from PostQuery import QuestionQuery
from PostQuery import AnswerQuery

POSTPERPAGE = 5

class SearchForPostsScreen:
	"""
	A screen which handles searching for posts and the processes
	associated with it.

	This module is responsible for providing the UI of the post
	search screen
	"""
	def __init__(self, terminal):
		"""
		Creates an instance of SearchForPostsScreen

		Parameters:
			terminal:
				A Terminal object which allows this module to interface
				with the OS terminal
		Returns:
			An instance of SearchForPostsScreen
		"""
		self.__terminal__ = terminal
		self.__SearchForPosts__ = SearchForPosts(terminal.getDBName())
		self.__menu__ = Menu(terminal)		
		self.__chkinp__ = CheckInput()		

	def printTitleKeyword(self):
		"""
		Prints identifying information telling the user what screen
		they are on and information about how to give keywords
		"""
		self.__terminal__.clear()
		self.__terminal__.printCenter("Search for Posts")
		self.__terminal__.printCenter("Enter terms delimited by commas")

	def printTitlePostSelect(self):
		"""
		Prints identifying information telling the user what screen
		they are on and how to navigate search results
		"""
		self.__terminal__.clear()
		self.__terminal__.printCenter("Posts Matching Keywords")
		self.__terminal__.printCenter("Type the number of the post you would like to select")
		self.__terminal__.printCenter("Type n to go to the next page or p to go to the previous page")
		print("Post Title" + "|" + "Votes" + "|" + "Answers")

	def printScreen(self):
		"""
		The main loop of the module. Prints the title, gets the keywords, displays
		posts gotten through keywords five at a time. Takes user input
		to go from page to page and allows the user to exit or select a post

		Returns:
			None:
				if user exits
			post:
				A PostQuery object containing information about the selected
				post
		"""
		self.printTitleKeyword()
		posts = self.__SearchForPosts__.getPosts(self.getParsedKeywords())
		
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
						return(selectedPost)
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
						return(selectedPost)
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

	def getParsedKeywords(self):
		"""
		Gets input from user and parses it
		into a list of terms that can be used to query the database

		Returns:
			A List of strings that can be used to query the database
		"""
		userInput = input("Enter search term(s): ")
		searchTermList = userInput.split(",")
		for i, string in enumerate(searchTermList):
			searchTermList[i] = "%" + string.strip() + "%"
		return searchTermList


	def getMenu(self, posts, index):
		"""
		Manipulates this modules menu so that only five items
		are displayed at any given time

		Parameters:
			posts:
				A List of PostQuery Objects which contain one of many keywords
			index:
				An Integer that serves as a pointer to the point which we
				are at in posts
		"""
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
				if isinstance(posts[i], QuestionQuery):
					self.__menu__.addMenuItem(str(posts[i].title) + " | " + str(posts[i].voteCount) + " | " + str(posts[i].answerCount))
				else:
					self.__menu__.addMenuItem(str(posts[i].title) + " | " + str(posts[i].voteCount))
			return True
			
if __name__ == "__main__":
	from Terminal import Terminal
	searchPostScreen = SearchForPostsScreen(Terminal())
	searchPostScreen.printScreen()
