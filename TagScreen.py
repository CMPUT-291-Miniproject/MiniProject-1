from Tag import Tag
from CheckInput import CheckInput
from PostQuery import QuestionQuery
from PostQuery import AnswerQuery

class TagScreen:
	"""
	A screen which handles adding a tag to a post

	This module is responsible for providing the UI of the screen
	which the user can interface with to add tags to posts
	"""
	def __init__(self, terminal, post):
		"""
		Creates an instance of TagScreen

		Parameters:
			terminal:
				A Terminal object allowing for this module to interface
				with the OS terminal
			post:
				A PostQuery Object which contains information about the post
				who is getting a tag
		Returns:
			An instance of TagScreen
		"""
		self.__chkinp__ = CheckInput()
		self.__terminal__ = terminal
		self.__post__ = post
		self.__tag__ = Tag(terminal.getDBName())
	
	def printTitle(self):
		"""
		Prints text identifying this screen to the user and providing some information
		"""
		self.__terminal__.clear()
		self.__terminal__.printCenter("Tag the post")
		self.__terminal__.printCenter("The post you are currently tagging has the title " + self.__post__.title)

	def printScreen(self):
		"""
		Serves as the main loop of the module. Allowing the user
		to interface with the program by providing a tag
		"""
		self.printTitle()
		invalidInput = True
		
		try:
			while invalidInput:
				userInput = input("Enter tag you would like to add to the post: ")
				if self.__chkinp__.checkEscape(userInput):
					return None
			self.__tag__.addTag(post.pid, userInput)
		except Exception as e:
			print(e)
		else:
			print("Tag successfully added!")
		finally:
			input("Type enter to continue: ")
		

if __name__ == "__main__":
	from Terminal import Terminal
	from SearchForPostsScreen import SearchForPostsScreen
	from SelectedPostScreen import SelectedPostScreen

	sfps = SearchForPostsScreen(Terminal())
	post = sfps.printScreen()
	sps = SelectedPostScreen(Terminal(), post, True)
	if sps.printScreen() == 3:
		t = TagScreen(Terminal(), post)
		t.printScreen()

		
