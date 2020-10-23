from WelcomeScreen import WelcomeScreen
from Terminal import Terminal

terminal = Terminal()
welcomeScreen = WelcomeScreen(terminal)
isUser = welcomeScreen.checkUserExistence()
print(isUser)
