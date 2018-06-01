##Funktions##
#Title Screen
def titlescreen():
    print ("")
    print ("")
    print ("                                               ██████╗██╗  ██╗██╗ ██████╗██╗  ██╗███████╗███╗   ██╗     ██████╗ ██╗   ██╗███████╗███████╗████████╗")
    print ("                                              ██╔════╝██║  ██║██║██╔════╝██║ ██╔╝██╔════╝████╗  ██║    ██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝")
    print ("                                              ██║     ███████║██║██║     █████╔╝ █████╗  ██╔██╗ ██║    ██║   ██║██║   ██║█████╗  ███████╗   ██║   ")
    print ("                                              ██║     ██╔══██║██║██║     ██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   ")
    print ("                                              ╚██████╗██║  ██║██║╚██████╗██║  ██╗███████╗██║ ╚████║    ╚██████╔╝╚██████╔╝███████╗███████║   ██║   ")
    print ("                                               ╚═════╝╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ")

#Main Menu
def mainmenu():
    print ("")
    print ("                                                                                        +------------+")
    print ("                                                                                        ¦ Start Game ¦")
    print ("                                                                                        ¦    Help    ¦")
    print ("                                                                                        ¦    Quit    ¦")
    print ("                                                                                        +------------+")
    print ("")
    print ("")

##Main Menu Functions [New Game, Help and Quit]
#Prints the help text
def readMe():
    print("                                                     +--------------------------------------------------------------------------------------+")
    print("                                                     |                                                                                      |")
    print("                                                     |   HELP                                                                               |")
    print("                                                     |                                                                                      |")
    print("                                                     +--------------------------------------------------------------------------------------+")
    print("                                                     |                                                                                      |")
    print("                                                     | + The Game understands only simple Commands such as: |help|start game|quit|go to|    |")
    print("                                                     |                                                                                      |")
    print("                                                     +--------------------------------------------------------------------------------------+\n")


#Closes the game
def quitGame(alive):
    alive = false;
    return alive;

#Starts the game
def startGame():
    readMe();

#Function that asks player for input as long as he is alive
def playerInput():
    pinput = "";
    pinput = input("                                                                                 What would you like to do?\nInput: ")

    if (pinput == "Start" or pinput == "Start Game" or pinput == "start" or pinput == "start game" or pinput == "play" or pinput == "play game" or pinput == "Play" or pinput == "Play Game"):
        startGame();
    elif (pinput == "Help" or pinput == "help"):
        readMe();
    elif (pinput == "Quit" or pinput == "quit"):
        quitGame();

#Game Loop
def loop(alive):
    while (alive == True):
        playerInput();

#Values
alive = True;
import random;
rnd = random;

#Execute Code
titlescreen();
mainmenu();
loop(alive);
