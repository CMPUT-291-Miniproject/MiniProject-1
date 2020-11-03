from CheckInput import CheckInput
from PostEdit import PostEdit

class PostEditScreen:
	
	def __init__(self, terminal, post):
		self.__terminal__ = terminal
		self.__post__ = post
		self.__postEdit__ = PostEdit(terminal.getDBName())		
		self.__chkinp__ = CheckInput()		

	def printTitleMain(self):
		self.__terminal__.clear()
		self.__terminal__.printCenter("Editing Post")
		self.__terminal__.printCenter("The title of the post you are editing is " + self.__post__.title)
	
	def printTitleSubTitle(self):
		self.__terminal__.clear()
		self.__terminal__.printCenter("Editing Title")
		self.__terminal__.printCenter("Current Title: " + self.__post__.title)

	def printTitleSubBody(self):	
		self.__terminal__.clear()
		self.__terminal__.printCenter("Editing Body")
		self.__terminal__.printCenter("Current Body: " + self.__post__.body)
	
	def getEditType(self):
		while True:
			self.printTitleMain()
			print("1. Edit Title of Post")
			print("2. Edit Body of Post")
			userInput = input("Select what you would like to edit: ")
			if (userInput == "1" or userInput == "2"):
				return userInput
	
	def printScreen(self):
		editType = self.getEditType()
		if editType == "1":
			self.printTitleSubTitle()
			title = input("Enter new title: ")
			self.__postEdit___.changeTitle(post.title, title)
		if editType == "2":
			self.printTitleSubBody()
			body = input("Enter new body: ")
			self.__postEdit__.changeBody(post.body, body)
		input("Type enter to continue: ")

if __name__ == "__main__":
	from Terminal import Terminal
	from SearchForPostsScreen import SearchForPostsScreen
	from SelectedPostScreen import SelectedPostScreen

	sfps = SearchForPostsScreen(Terminal())
	post = sfps.printScreen()
	sps = SelectedPostScreen(Terminal(), post, True)
	if sps.printScreen() == 4:
		pes = PostEditScreen(Terminal(), post)
		pes.printScreen()
					
