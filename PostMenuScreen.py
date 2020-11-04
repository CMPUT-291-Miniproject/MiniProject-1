from Menu import Menu

class PostMenuScreen:
	"""
	A screen which allows the user to select
	a post

	This module provides the ui for the postMenu interface
	"""
	def __init__(self, terminal, posts):
		"""
		Creates an instance of PostMenuScreen

		Parameters:
			terminal:
				A Terminal object allowing the module to interface
				with the OS terminal
		Returns:
				An instance of Tag
		"""
		self.__menu__ = Menu(terminal)
		for post in posts:
			self.__menu__.addMenuItem(post)

	def printScreen(self):
		"""
		Prints the menu options of the module
		"""
		self.__menu__.printScreen()

if __name__ == "__main__":
	from Terminal import Terminal
	posts = ["How do I make eggs?", "Hello anyone out there?", "Yes I am Here!", "Just google it 4head"]
	postScreen = PostMenuScreen(Terminal(), posts)
	postScreen.printScreen()
