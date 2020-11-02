from Menu import Menu
class SelectedPostScreen:
	def __init__(self, terminal, post, privileged):
		self.__terminal__ = terminal
		self.__post__ = post
		self.__menu__ = Menu(terminal)
		self.__privileged__ = privileged
		self.menuSetup()

	def menuSetup(self):
		self.__menu__.addMenuItem("Upvote")
		if self.__post__[1]:		#Post is a question
			self.__menu__.addMenuItem("Post an answer")
		else:
			if (self.__privileged__):
				self.__menu__.addMenuItem("Mark as accepted answer")
		if (self.__privileged__):
			self.__menu__.addMenuItem("Give a badge")
			self.__menu__.addMenuItem("Add a tag")
			self.__menu__.addMenuItem("Edit post")

	def printTitle(self):
		self.__terminal__.clear()
		self.__terminal__.printCenter(self.__post__[0][0])
		if self.__post__[1]:		#Post is a question
			self.__terminal__.printCenter(self.__post__[0][3])
		else:
			self.__terminal__.printCenter(self.__post__[0][2])

	def printScreen(self):
		self.printTitle()
		return self.__menu__.printScreen()

if __name__ == "__main__":
	from Terminal import Terminal
	from SearchForPostsScreen import SearchForPostsScreen
	sps = SearchForPostsScreen(Terminal(), "Miniproject_1.db")
	post = sps.printScreen()
	sps = SelectedPostScreen(Terminal(), post, False)
	print(sps.printScreen())
	sps = SelectedPostScreen(Terminal(), post, True)
	print(sps.printScreen())
