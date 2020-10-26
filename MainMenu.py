from Menu import Menu

class MainMenu():
	"""
	A screen which allows the user to select
	an action they would like to perform.

	This module provides the ui for the main interface
	as well as handling the selection of an action within
	the program
	"""
	def __init__(self, terminal):
		self.__menu__ = Menu(terminal)
	
		self.__menu__.addMenuItem("Post a question")
		self.__menu__.addMenuItem("Search for posts")
		self.__menu__.addMenuItem("Post action - Answer")
		self.__menu__.addMenuItem("Post action - Vote")

		self.__menu__.getUserSelection()		
