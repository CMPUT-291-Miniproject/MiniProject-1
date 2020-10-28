from Terminal import Terminal
from PostQuestion import PostQuestion

class PostQuestionScreen:
  
	def __init__(self, terminal, dbName):
			self.__terminal__ = terminal
			self.__terminal__.clear()
			self.__body__ = PostQuestion(dbName)
	
	def printScreen(self):
		repeat = True
		
		while repeat:
			self.__terminal__.printCenter("---POSTING QUESTION---")
			self.__terminal__.printCenter("To go back without posting a question, input BACK during any prompt.")
			print('\n')
			
			title = input("Please enter the title of the question: ")
			if title.lower().strip() == "back":
				return
			
			print('\n')
			
			body = input("Please enter the description of the question: ")
			if body.lower().strip() == "back":
				return
				
			while True:
				self.__terminal__.clear()
				self.__terminal__.printCenter(title)
				self.__terminal__.printCenter(body)
				print("\n")
			
				choice = input("Is this what you want to post? (Y or N):")
				if choice.upper() == "Y":
					repeat = False
					break
				elif choice.upper() == 'N':
					break
				else:
					input("Invalid input. Press enter to continue.")
				
			self.__body__.add_question(title, body, poster)
					
if __name__ == "__main__":
	
	postQuestionScreen = PostQuestionScreen(Terminal(), 'Miniproject_1.db')
	postQuestionScreen.printScreen()
