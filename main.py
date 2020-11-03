import sqlite3
from Terminal import Terminal
from LoginScreen import LoginScreen
from RegisterScreen import RegisterScreen
from WelcomeScreen import WelcomeScreen
from MainMenuScreen import MainMenuScreen
from PostScreen import PostScreen
from SearchForPostsScreen import SearchForPostsScreen
#dbName = 'Miniproject_1.db'

def check_priv(dbName, uid):
	"""
	checks the database to see if the user has the title of privileged. 
	
	Parameters:
		dbName: String. Name of the database, derived from terminal.py
		uid: 4 character string. Unique ID of the user, used for loads the things in the program.
		
	Returns:
		check: Boolean. True when a match between the uid of the user and a uid in the Privileged table in the database, False otherwise.
	"""
	#connect to database and create cursor to query
	db = sqlite3.connect(dbName)
	cur = db.cursor()
	
	#grab a matching uid in privileged table, then closes the database.
	cur.execute("SELECT uid FROM privileged WHERE ? = uid", (uid,))
	check = cur.fetchone()
	db.close()
	
	#if a match is found, return true. If no matches were found, return false.
	if check is None:
		return False
	else:
		return True
		

"""START OF PROGRAM"""
if __name__ == "__main__":
	terminal = Terminal()

	#Main program loop, includes the welcome screen and login sequence. This loop handles cases such as users logging out and back into another account.
	exit = False
	while not exit:
			
		#prints the welcome screen, which lets users login, register, or exit the program 
		welcomeScreen = WelcomeScreen(terminal)
		isUser = welcomeScreen.printScreen()
		
		#open the login screen and log the user in. They can return back if they want to too.
		if isUser:
			#log the user in
			uid = LoginScreen(terminal).log_in()
			
			#checks if the user is a privileged user
			priv = check_priv(terminal.getDBName(), uid)			
			
		#funny tidbit, the statement "not isUser" returns true if isUser is not True, even if isUser is NoneType.
		elif isUser == False:
			#Registers the user. TODO: allow the user to stop making a new account, needs to be done in RegisterScreen.py
			uid = RegisterScreen(terminal, terminal.getDBName()).printScreen()
			
			#if the user doesn't make a new account, return to main menue (start of loop)
			if uid is None:
				continue
				
			#checks if the user is a privileged user	
			priv = check_priv(terminal.getDBName(), uid)
			
		else:
			#Quitting the program, leads to a goodbye message outside of loop.
			break
		
		#Input loop for command choice.
		while True:
			#prints the menue and returns the choice the user makes as an int. error handling and processing takes place in menu.py, so
			#there's no need to worry about it here
			menu = MainMenuScreen(terminal).printScreen()
			
			#post question
			if menu == 0:
				PostScreen(terminal, uid).printQuestionScreen()
				
			#TODO: search for posts
			elif menu == 1:
				#grab a 
				post = SearchForPostsScreen(terminal, terminal.getDBName()).printScreen()
				try:
					if post[1][0] is 1:
						question = False
				except:
					question = post[1]
				print(post)
				print(question)
				input()
				
				terminal.clear()
				terminal.printCenter("Title:" + post[0][0])
				
				if question == True:
					#question is a question
					terminal.printCenter("Body:" + post[0][3])
				else:
					#question is an answer
					terminal.printCenter("Body:" + post[0][2])
				
				print("\n")
				stuff = int(input("Please enter an action on this post.\n1) Reply to this post\n2) Vote for this post\n"))
				#print(stuff)
				input()
				
				#reply to the post
				if stuff == 1:
					terminal.clear()
					PostScreen(terminal, uid).printAnswerScreen(post[0][4])
								
			#log out of account
			elif menu == 2:
				break
				
			#exit program
			elif menu == 3:
				exit = True
				break
			
			#end of input loop
	#end of main program loop

#When the user quits the program.
print("Goodbye!")
