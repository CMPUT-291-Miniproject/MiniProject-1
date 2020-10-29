from Terminal import Terminal
dbName = 'Miniproject_1.db'

terminal = Terminal()
welcomeScreen = WelcomeScreen(terminal)
isUser = welcomeScreen.checkUserRegistration()
if isUser:
	uid =
elif not isUser:
	#register, then log in
elif isUser is None:
	#send goodbye message and quit
	return
menu = MainMenu(terminal)
