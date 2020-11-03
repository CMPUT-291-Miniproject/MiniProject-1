from Tag import Tag
from CheckInput import CheckInput
from PostQuery import QuestionQuery
from PostQuery import AnswerQuery

class TagScreen:
	def __init__(self, terminal, post):
		self.__chkinp__ = CheckInput()
		self.__terminal__ = terminal
		self.__post__ = post
		self.__tag__ = Tag(terminal.getDBName())
	
	def printTitle(self):
		self.__terminal__.clear()
		self.__terminal__.printCenter("Tag the post")
		self.__terminal__.printCenter("The post you are currently tagging has the title " + self.__post__.title)

	def printScreen(self):
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

		
