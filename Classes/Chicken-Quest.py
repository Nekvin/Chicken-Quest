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

#Creates Character
def createChar():
    #Player chooses Name
    pinput = input("                                              > Name Your Character: ")
    pname = pinput;
    print ("\n")
    while (len(pinput) > 10):
        if (len(pinput) <= 10):
            break;
        pinput = input("                                              > Name Your Character: ")
        pname = pinput;
        print ("\n")

    #Player chooses Gender
    pinput = input("                                              > Choose your Gender: ")
    print ("\n")
    while (pinput != "Male" or pinput != "male" or pinput != "Female" or pinput != "female"):
        if (pinput == "Male" or pinput == "male" or pinput == "Female" or pinput == "female"):
            break;
        pinput = input("                                              > Choose your Gender: ")
        print ("\n")
    pgender = pinput;

    print ("\n")
    print ("                                              > Welcome to the Kingdom of Dileran, Adventurer " + pname)
    print ("\n")



#Game Loop
def gameLoop(alive):
    while (alive == True):
        playerInput();

#Function that asks player for input as long as he is alive
def playerInput():
    pinput = "";
    pinput = input("                                                                                 What would you like to do?\n> ")

    if (pinput == "Quit" or pinput == "quit"):
        quitGame();
    elif (pinput == "Help" or pinput == "help"):
        readMe();
    elif (pinput == "go to" or pinput == "goto" or pinput == "Go to"):
        goto();

#Function that moves player from one place to another
def goto():
    pinput = input("                                                                                 Where would you like to go?\n> ")
    pPosition = pinput;
    print ("                                              > You have gone to: " + pPosition)
    print ("\n")

#Values
alive = True;
pname = "";
pgender = "";
pPosition = "Wilderness";
Places = ["Shanty Town","Tallgrass Town","Wilderness"]
import random;
rnd = random;

#Execute Code
titlescreen();
readMe();
createChar();
gameLoop(alive);
