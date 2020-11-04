from CheckInput import CheckInput
from Badge import Badge

class BadgeScreen:
	"""
	A screen which handles giving badges to a post/user

	This module is responsible for providing the UI for providing
	a post/user with a badge
	"""
	def __init__(self, terminal, post):
		"""
		Creates an instance of BadgeScreen

		Parameters:
			terminal:
				A Terminal object which allows this module to interface
				with the OS terminal
			post:
				A PostQuery object which contains useful information
				about the post being given a badge
		"""
		self.__terminal__ = terminal
		self.__badge__ = Badge(terminal.getDBName(), post)
		self.__post__ = post
		self.__chkinp__ = CheckInput()
		self.__badges__ = self.__badge__.getBadgeNames()

	def printTitle(self):
		"""
		Prints identifying information telling the user what screen
		they are on and information about the post being given a badge
		as well as information about badges that can be given
		"""
		self.__terminal__.clear()
		self.__terminal__.printCenter("Add Badge to Post")
		self.__terminal__.printCenter("Adding a badge to post with title: " + self.__post__.title)
		self.printBadgeNames()
	
	def printBadgeNames(self):
		"""
		Prints name of badges which can be given
		"""
		print("All Badges\n")
		for badge in self.__badges__:
			print(badge)
	
	def printScreen(self):
		"""
		Provides the main functionality of BadgeScreen. Prints screen information,
		Gathers user input and calls methods to add that badge if possible
		"""
		self.printTitle()
		userInput = input("Enter Name of Badge to Give: ").lower()
		if userInput in self.__badges__:
			self.__badge__.addBadge(userInput, self.__post__.pid)
		else:
			print("Not a type of badge!")
		
if __name__ == "__main__":
	from Terminal import Terminal
	from SearchForPostsScreen import SearchForPostsScreen
	from SelectedPostScreen import SelectedPostScreen

	sfps = SearchForPostsScreen(Terminal())
	post = sfps.printScreen()
	sps = SelectedPostScreen(Terminal(), post, True)
	selection = sps.printScreen()
	
	if selection == 2:
		bs = BadgeScreen(Terminal(), post)
		bs.printScreen()
