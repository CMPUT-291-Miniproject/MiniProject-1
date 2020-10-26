from WelcomeScreen import WelcomeScreen
from Terminal import Terminal
from MainMenu import MainMenu

terminal = Terminal()
welcomeScreen = WelcomeScreen(terminal)
isUser = welcomeScreen.checkUserRegistration()
menu = MainMenu(terminal)
