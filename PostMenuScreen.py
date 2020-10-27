from Menu import Menu

class PostMenuScreen:
	def __init__(self, terminal, posts):
		self.__menu__ = Menu(terminal)
		for post in posts:
			self.__menu__.addMenuItem(post)

	def printScreen(self):
		self.__menu__.printScreen()

if __name__ == "__main__":
	from Terminal import Terminal
	posts = ["How do I make eggs?", "Hello anyone out there?", "Yes I am Here!", "Just google it 4head"]
	postScreen = PostMenuScreen(Terminal(), posts)
	postScreen.printScreen()
