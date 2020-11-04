from Menu import Menu
from PostQuery import QuestionQuery
from PostQuery import AnswerQuery
class SelectedPostScreen:
	"""
	A screen which handles options that can be taken
	on a selected post

	This module is responsible for providing the UI
	for taking actions on a post
	"""
	def __init__(self, terminal, post, privileged):
		"""
		Creates an instance of SelectedPostScreen

		Parameters:
			terminal:
				A Terminal object which allows this module to interface
				with the OS terminal
			post:
				A PostQuery object containing information about the post
				that was selected
			privileged:
				A Boolean object representing whether the current
				user is privileged or not
		Returns:
			An instance of SelectedPostScreen
		"""
		self.__terminal__ = terminal
		self.__post__ = post
		self.__menu__ = Menu(terminal)
		self.__privileged__ = privileged
		self.menuSetup()

	def menuSetup(self):
		"""
		Sets up a menu detailing various options that can be
		taken on a selected post. Adds options depending on
		whether the post is a question or an answer and 
		whether the user is privileged
		"""
		self.__menu__.addMenuItem("Upvote")
		if isinstance(self.__post__, QuestionQuery):
			self.__menu__.addMenuItem("Post an answer")
		else:
			if (self.__privileged__):
				self.__menu__.addMenuItem("Mark as accepted answer")
		if (self.__privileged__):
			self.__menu__.addMenuItem("Give a badge")
			self.__menu__.addMenuItem("Add a tag")
			self.__menu__.addMenuItem("Edit post")

	def printTitle(self):
		"""
		Prints identifying information about the current screen
		post title and post body
		"""
		self.__terminal__.clear()
		self.__terminal__.printCenter(self.__post__.title)
		self.__terminal__.printCenter(self.__post__.body)

	def printScreen(self):
		"""
		Provides the main functionality for SelectedPostScreen
		printing the information about the screen and calls a 
		method which displays possible options and gather user input

		Returns:
			A String object which is numerical representing the
			option selected from the menu
		"""
		self.printTitle()
		return self.__menu__.printScreen()

if __name__ == "__main__":
	from Terminal import Terminal
	from SearchForPostsScreen import SearchForPostsScreen
	sps = SearchForPostsScreen(Terminal())
	post = sps.printScreen()
	sps = SelectedPostScreen(Terminal(), post, False)
	print(sps.printScreen())
	sps = SelectedPostScreen(Terminal(), post, True)
	print(sps.printScreen())
