from Tag import Tag
from CheckInput import CheckInput

class TagScreen:
	def __init__(self, terminal, dbName, post):
		self.__chkinp__ = CheckInput()
		self.__terminal__ = terminal
		self.__post__ = post
		self.__tag__ = Tag(dbName)
	
	def printTitle(self):
		self.__terminal__.clear()
		self.__terminal__.printCenter("Tag the post")
		self.__terminal__.printCenter("The post you are currently tagging has the title " + self.__post__[0][0])

	def printScreen(self):
		self.printTitle()
		invalidInput = True
		error = 0
		while invalidInput:
			userInput = input("Enter tag you would like to add to the post: ")
			if self.__chkinp__.checkEscape(userInput):
				return None
			if self.__chkinp__.checkAlphaNumeric(userInput):
				invalidInput = False
		if post[1]:
			error = self.__tag__.addTag(userInput, post[0][4])
		else:
			error = self.__tag__.addTag(userInput, post[0][3])
		if (error == 1):
			print("An error has occured")
		else:
			print("Tag successfully added")
		input("Type enter to continue: ")
		

if __name__ == "__main__":
	from Terminal import Terminal
	from SearchForPostsScreen import SearchForPostsScreen
	from SelectedPostScreen import SelectedPostScreen

	sfps = SearchForPostsScreen(Terminal(), "Miniproject_1.db")
	post = sfps.printScreen()
	sps = SelectedPostScreen(Terminal(), post, True)
	if sps.printScreen() == 3:
		t = TagScreen(Terminal(), "Miniproject_1.db", post)
		t.printScreen()

		