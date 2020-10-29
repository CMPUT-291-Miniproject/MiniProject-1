from Terminal import Terminal
from PostQuestion import PostQuestion

class PostQuestionScreen:
	"""
	User interface for generating and posting a question.
	
	Uses the framework from PostQuestion.py to enter the question into the database, and Terminal for extra UI commands.
	"""
	
	def __init__(self, terminal, dbName, uid):
		"""
		Creates an instance of PostQuestionScreen, which is used in Main.py (subject to change)
		
		Parameters:
			terminal: Terminal Object. Instance of the terminal screen used to display information. Essentially used for easily clearing a screen of text.
			dbName: string. File name of the database. Name is subject to change on demo, therefore parsed at runtime as a sommand line arguement.
			uid: User ID of the poster. Needed for adding question to database. 
			
		Additional Init. Variables:
			__body__: PostQuestion Object. Instance of the Question posting framework, used to add questions to the database.
			
		Returns: N/A
		"""
	

	def printScreen(self):
    """
		User interface for adding a question to the database. This method validates all user input before passing it to PostQuestion.py, which actually adds the entry to the database.
		
		Parameters: N/A
		
		Returns: N/A
		"""
		repeat = True
		
		#Main input loop, runs until user input is valid, or they quit out of the menue.
		while repeat:
			self.__terminal__.printCenter("---POSTING QUESTION---")
			self.__terminal__.printCenter("To go back without posting a question, input BACK during any prompt.")
			print('\n')
			
			#get title of post
			title = input("Please enter the title of the question: ")
			if title.lower().strip() == "back":
				return
			
			print('\n')
			
			#Get body of post
			body = input("Please enter the description of the question: ")
			if body.lower().strip() == "back":
				return
				
			#input validation loop. breaks if input is Y or N.
			while True:
				self.__terminal__.clear()
				self.__terminal__.printCenter(title)
				self.__terminal__.printCenter(body)
				print("\n")
				
			
				choice = input("Is this what you want to post? (Y or N):")
				
				#if the user gives the ok to post, break out of all loops and add the post
				if choice.upper() == "Y":
					repeat = False
					break
				#if the user wants to change their post, repeat main loop but break this input loop
				elif choice.upper() == 'N':
					break
				#Any other input repeats the input loop
				else:
					input("Invalid input. Press enter to continue.")
				
			#adds the question to the database and alerts the user that the operation was a success.
			self.__body__.add_question(title, body)
			input("Your question has been posted. Press enter to return back to the main menue.")
			return
					
if __name__ == "__main__":
	
	postQuestionScreen = PostQuestionScreen(Terminal(), 'Miniproject_1.db')
	postQuestionScreen.printScreen()
