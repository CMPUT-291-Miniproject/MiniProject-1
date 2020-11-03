from CheckInput import CheckInput
from PostEdit import PostEdit
from PostQuery import QuestionQuery
from PostQuery import AnswerQuery

class PostEditScreen:
	"""
	A screen which handles editing posts

	This module is responsible for providing the UI and main functionality
	of the post edit screen
	"""
	def __init__(self, terminal, post):
		"""
		Creates an instance of PostEditScreen

		Parameters:
			terminal:
				A Terminal object which allows this module to interface
				with the OS terminal
			post:
				A PostQuery Object which contains information
				about the post being edited
		"""
		self.__terminal__ = terminal
		self.__post__ = post
		self.__postEdit__ = PostEdit(terminal.getDBName())		
		self.__chkinp__ = CheckInput()		

	def printTitleMain(self):
		"""
		Prints identifying information telling the user what screen
		they are on and information about the post being edited
		"""
		self.__terminal__.clear()
		self.__terminal__.printCenter("Editing Post")
		self.__terminal__.printCenter("The title of the post you are editing is " + self.__post__.title)
		self.__terminal__.printCenter("The body of the post you are editing is " + self.__post__.body)
	
	def printTitleSubTitle(self):
		"""
		Prints identifying information telling the user what
		subscreen they are on and information about the title
		being edited
		"""
		self.__terminal__.clear()
		self.__terminal__.printCenter("Editing Title")
		self.__terminal__.printCenter("Current Title: " + self.__post__.title)

	def printTitleSubBody(self):	
		"""
		Prints identifying information telling the user what
		subscreen they are on and information about the body
		being edited
		"""
		self.__terminal__.clear()
		self.__terminal__.printCenter("Editing Body")
		self.__terminal__.printCenter("Current Body: " + self.__post__.body)
	
	def getEditType(self):
		"""
		Gets userInput on which aspect of the post they would like to edit
			Returns:
				The input of the user which will either be '1' or '2'
		"""
		while True:
			self.printTitleMain()
			print("1. Edit Title of Post")
			print("2. Edit Body of Post")
			userInput = input("Select what you would like to edit: ")
			if (userInput == "1" or userInput == "2"):
				return userInput
			elif (self.__chkinp__.isEscape(userInput)):
				return None
	
	def printScreen(self):
		"""
		The main loop of the module. Prints the title, subtitle and uses the
		user input to call various methods

		Returns:
			None if user exits
		"""
		editType = self.getEditType()
		if editType == "1":
			self.printTitleSubTitle()
			title = input("Enter new title: ")
			self.__postEdit__.changeTitle(post.pid, title)
		elif editType == "2":
			self.printTitleSubBody()
			body = input("Enter new body: ")
			self.__postEdit__.changeBody(post.pid, body)
		elif editType is None:
			return None
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
					
