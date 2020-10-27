from WelcomeScreen import WelcomeScreen
from Terminal import Terminal
from MainMenuScreen import MainMenuScreen
from SearchForPostsScreen import SearchForPostsScreen
from PostMenuScreen import PostMenuScreen


terminal = Terminal()
welcomeScreen = WelcomeScreen(terminal)
isUser = welcomeScreen.checkUserRegistration()
menu = MainMenuScreen(terminal)
userSelection = menu.getUserSelection()
print(userSelection)
spScreen = SearchForPostsScreen(terminal)
spScreen.printScreen()
spScreen.getKeyWords()

p = ["Sunshine", "Lolipops", "Rainbows", "Everything", "So Wonderful", "When We Are Together", "I ate 3 meals today!"]

pMenu = PostMenuScreen(terminal, p)
pMenu.printScreen()
print(terminal.getDBName())
