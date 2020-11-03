from CheckInput import CheckInput
from Badge import Badge

class BadgeScreen:

	def __init__(self, terminal, post):
		self.__terminal__ = terminal
		self.__badge__ = Badge(terminal.getDBName(), post)
		self.__post__ = post
		self.__chkinp__ = CheckInput()
		self.__badges__ = self.__badge__.getBadgeNames()

	def printTitle(self):
		self.__terminal__.clear()
		self.__terminal__.printCenter("Add Badge to Post")
		self.__terminal__.printCenter("Adding a badge to post with title: " + self.__post__.title)
		self.printBadgeNames()
	
	def printBadgeNames(self):
		print("All Badges\n")
		for badge in self.__badges__:
			print(badge)
	
	def printScreen(self):
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
