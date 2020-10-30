from Terminal import Terminal
from LoginScreen import LoginScreen
from WelcomeScreen import WelcomeScreen
from MainMenuScreen import MainMenuScreen
from PostQuestionScreen import PostQuestionScreen
#dbName = 'Miniproject_1.db'

if __name__ == "__main__":
	terminal = Terminal()

	#Main program loop, includes the welcome screen and login sequence. This loop handles cases such as users logging out and back into another account.
	exit = False
	while not exit:
			
		welcomeScreen = WelcomeScreen(terminal)
		isUser = welcomeScreen.printScreen()
		print(type(isUser))
		
		if isUser:
			#log the user in
			uid = LoginScreen(terminal).log_in()
			
		#funny tidbit, the statement "not isUser" returns true if isUser is not True, even if isUser is NoneType.
		elif isUser == False:
			#register, then log in
			pass
			
		else:
			#send goodbye message and quit
			print("YES")
			exit = True
			break

		#print(uid)
		if not exit:
			while True:
				menu = MainMenuScreen(terminal).printScreen()
				print(type(menu), menu)
				if menu == 0:
					#post question
					PostQuestionScreen(terminal, uid).printScreen()
				elif menu == 1:
					#TODO: search for posts
					pass
				elif menu == 2:
					#log out of account
					break
				elif menu == 3:
					#exit program
					exit = True
					break
		

print("Goodbye!")

		
