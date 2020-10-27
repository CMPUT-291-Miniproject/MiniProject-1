from Menu import Menu

class PostMenuScreen:
	def __init__(self, terminal, posts):
		self.__menu__ = Menu(terminal)
		for post in posts:
			self.__menu__.addMenuItem(post)

	def printScreen(self):
		self.__menu__.printScreen()
