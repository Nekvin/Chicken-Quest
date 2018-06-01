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
    print("                                                                  +-------------------------------------------------------------------+")
    print("                                                                  |                                                                   |")
    print("                                                                  |   HELP                                                            |")
    print("                                                                  |                                                                   |")
    print("                                                                  +-------------------------------------------------------------------+")
    print("                                                                  |                                                                   |")
    print("                                                                  |  +                                                                |")
    print("                                                                  |                                                                   |")
    print("                                                                  |  +                                                                |")
    print("                                                                  |                                                                   |")
    print("                                                                  |  +                                                                |")
    print("                                                                  |                                                                   |")
    print("                                                                  |  +                                                                |")
    print("                                                                  |                                                                   |")
    print("                                                                  |  +                                                                |")
    print("                                                                  |                                                                   |")
    print("                                                                  |  +                                                                |")
    print("                                                                  |                                                                   |")
    print("                                                                  |  +                                                                |")
    print("                                                                  |                                                                   |")
    print("                                                                  +-------------------------------------------------------------------+\n")


#Closes the game
def quitGame(alive):
    alive = false;
    return alive;

#Starts the game
def startGame():
    readMe();

#Function that asks player for input as long as he is alive
def playerInput():
    pinput = input("                                                                                 What would you like to do?\nInput: ")

    if (pinput == "Start" or "Start Game" or "start" or "start game" or "play" or "play game" or "Play" or "Play Game"):
        startGame();
    elif (pinput == "Help" or "help"):
        readMe();
    elif (pinput == "Quit" or "quit"):
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
