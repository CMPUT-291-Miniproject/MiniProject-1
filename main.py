import sqlite3
from Terminal import Terminal
from LoginScreen import LoginScreen
from RegisterScreen import RegisterScreen
from WelcomeScreen import WelcomeScreen
from MainMenuScreen import MainMenuScreen
from PostScreen import PostScreen
from SearchForPostsScreen import SearchForPostsScreen
from PostQuery import QuestionQuery
from PostQuery import AnswerQuery
from Vote import Vote
from PostEditScreen import PostEditScreen
from BadgeScreen import BadgeScreen
from TagScreen import TagScreen
from MarkAccepted import AcceptedAnswer
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
			if uid is None:
				continue
			#checks if the user is a privileged user
			priv = check_priv(terminal.getDBName(), uid)
			#testing below
			#print(priv)			
			
		#funny tidbit, the statement "not isUser" returns true if isUser is not True, even if isUser is NoneType.
		elif isUser == False:
			#register, then log in
			uid = RegisterScreen(terminal, terminal.getDBName()).printScreen()
			if uid is None:
				continue
			
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
				
			#search for posts
			elif menu == 1:				
				#PseudoCode for how searchforposts works
				
				#Grab the post to perform the action on, 
				#Returned as a tuple in the form (title, votecount, answer count, body, pid) for questions
				#Returned as a tuple in the form (title, votecount, body, pid) for answers
				#difference is isinstance(x, QuestionQuery)
				post = SearchForPostsScreen(terminal).printScreen()				

				#while the user is still using the menue
				while True:
					#clean terminal and print title of post
					if post is None:
						break
					terminal.clear()
					terminal.printCenter("Title: "+  post[0])
					#if its a question
					if isinstance(post, QuestionQuery):
						#Options are:
							#reply to post
							#vote on post
							#exit to menue
						#if the user is privileged, also includes:
							#edit post
							#give badge
							#add tag
						
						#special line for printing the body, since the location of the body in the tuple is [3], not [2]
						terminal.printCenter("Body: " + post[3])
						print("\n")
						
						#print the options for the user
						print("1) Reply to the post\n2) Upvote the post")
						
						#privileged user actions only
						if priv:
							print("3) Edit Post\n4) Give Badge\n5) Add Tag\n6) Exit")
							choice = input("Please select which action to take: ")
							
							#reply to post
							if choice == '1':
								terminal.clear()
								PostScreen(terminal, uid).printAnswerScreen(post[4])
								
							#upvote post. Checks to see if user has voted on the post before adding vote
							#this simplifies error handling by not allowing errors 
							elif choice == '2':
								v = Vote(terminal.getDBName())
								if v.check_vote(post[4], uid) == False:
									v.vote(post[4], uid)
									input("Vote placed. Press enter to continue:")
								else:
									input("You have already voted on this post. Press enter to continue:")
									
							#TODO: edits posts (needs fix)
							elif choice == '3':
								newPost = PostEditScreen(terminal, post).printScreen()
								if newPost is not None:
									post = newPost
							
							#TODO: adds badge (needs fix)
							elif choice == '4':
								BadgeScreen(terminal, post).printScreen()
								
							#TODO: adds badge (needs fix)
							elif choice == '5':
								TagScreen(terminal, post).printScreen()
								
							#returns back to main menu
							elif choice == '6':
								break
							else:
								input("Invalid input. Press enter to continue:")
									
						else:
							print("3) Exit")
							choice = input("Please select which action to take: ").strip()
							
							#reply to post
							if choice == '1':
								terminal.clear()
								PostScreen(terminal, uid).printAnswerScreen(post[4])
								
							#upvote post. Checks to see if user has voted on the post before adding vote
							#this simplifies error handling by not allowing errors
							elif choice == '2':
								v = Vote(terminal.getDBName())
								if v.check_vote(post[4], uid) == False:
									v.vote(post[4], uid)
									input("Vote placed. Press enter to continue:")
								else:
									input("You have already voted on this post. Press enter to continue:")
									
							#exit back to main menu
							elif choice == '3':
								break
							else:
								input("Invalid input. Press enter to continue:")
							
						
					else:
						#Options are:
							#vote on the answer
							#exit to menu
						#If the user is privileged, also includes:
							#edit post
							#give badge
							#add tag
							#mark as the accepted answer
							
						#print body of post, special due to differences in QuestionQuery and AnswerQuery return
						terminal.printCenter("Body: " + post[2])
						print("\n")
						
						#print the options for the user
						print("1) Upvote the post")
						
						#for privileged users:
						if priv:
							#additional commands
							print("2) Edit Post\n3) Give Badge\n4) Add Tag\n5) Mark Accepted Answer\n6) Exit")
							
							#user choice of commands
							choice = input("Please select which action to take: ").strip()
							
							#upvote post. Checks to see if user has voted on the post before adding vote
							#this simplifies error handling by not allowing errors 
							if choice == '1':
								v = Vote(terminal.getDBName())
								if v.check_vote(post[3], uid) == False:
									v.vote(post[3], uid)
									input("Vote placed. Press enter to continue:")
								else:
									input("You have already voted on this post. Press enter to continue:")
									
							#TODO: edits posts (needs fix)
							elif choice == '2':
								PostEditScreen(terminal, post).printScreen()
								
							#TODO: add badge (needs fix)	
							elif choice == '3':
								BadgeScreen(terminal, post).printScreen()
								
							#TODO: add tags (needs fix)
							elif choice == '4':
								TagScreen(terminal, post).printScreen()
								
							#TODO: Mark accepted answer
							elif choice == '5':
								#TODO: mark accepted answer
								AcceptedAnswer(terminal, post[3]).acceptAnswer()
								input("Successfully set the answer as the accepted answer. Press enter to continue:")
								
							#exit back to main menu
							elif choice == '6':
								break
							else:
								input("Invalid input. Press enter to continue:")
							
							
						#non-privileged users
						else:
							#print options, only ones are add vote and exit
							print("2) Exit")
							
							#user choice of commands
							choice = input("Please select which action to take: ").strip()
							
							#upvote post. Checks to see if user has voted on the post before adding vote
							#this simplifies error handling by not allowing errors
							if choice == '1':
								v = Vote(terminal.getDBName())
								if v.check_vote(post[3], uid) == False:
									v.vote(post[3], uid)
									input("Vote placed. Press enter to continue:")
								else:
									input("You have already voted on this post. Press enter to continue:")
								
							#return back to main menu
							elif choice == '2':
								break
							else:
								input("Invalid input. Press enter to continue:")
							
							
				#end of search posts, including all of the options for selected post

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