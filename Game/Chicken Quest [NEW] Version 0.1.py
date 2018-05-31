##Funktions##
#Function doesnt let game close
def DONTCLOSE():
    DONTCLOSE = input("")

#Game Loop
def loop(alive):
    while (alive == True):
        playerInput();

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
    print ("                                                                                         ----------")
    print ("                                                                                        ¦ New Game ¦")
    print ("                                                                                        ¦   Help   ¦")
    print ("                                                                                        ¦   Quit   ¦")
    print ("                                                                                         ----------")
    print ("")
    print ("")

#Prints the help text
def readMe():
    print ("                                                     This Option doesn't exist!\n")

#Main Menu Functions [New Game, Help and Quit]
def newGame():
    readMe();

#Function that asks player for input as long as he is alive
def playerInput():
    pinput = input("                                                                                 What would you like to do?\nInput: ")

    if (pinput == "Help" or pinput == "help"):
        readMe()


#Values
alive = True;
import random

#Execute Code
titlescreen();
mainmenu();
loop(alive);
