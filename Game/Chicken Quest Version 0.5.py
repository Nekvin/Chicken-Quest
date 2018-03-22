#Values

from Dragon import Dragon
from Warrior import Warrior
import random

Yes = ["Yes","yes"]
No = ["No","no"]
NewGame = ["new game","new"]
LoadGame = ["load game","load"]
Quit = ["quit","quit game"]
NameChar = ""
NameChar_sure = ""
genders = ["male","female"]
gender = ""
kingdomchoice = ""
kingdoms = ["Astralgard","Eisenheart","Syldria","Dileran"]
classes = ["Spellsword","Warrior","Rogue"]
namelength = [3,4,5,6,7,8,9,10,11,12,13,14,15]

#Funktions



#Title Screen
                         
print ("")
print ("")
print ("                                               ██████╗██╗  ██╗██╗ ██████╗██╗  ██╗███████╗███╗   ██╗     ██████╗ ██╗   ██╗███████╗███████╗████████╗")
print ("                                              ██╔════╝██║  ██║██║██╔════╝██║ ██╔╝██╔════╝████╗  ██║    ██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝")
print ("                                              ██║     ███████║██║██║     █████╔╝ █████╗  ██╔██╗ ██║    ██║   ██║██║   ██║█████╗  ███████╗   ██║   ")
print ("                                              ██║     ██╔══██║██║██║     ██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   ")
print ("                                              ╚██████╗██║  ██║██║╚██████╗██║  ██╗███████╗██║ ╚████║    ╚██████╔╝╚██████╔╝███████╗███████║   ██║   ")
print ("                                               ╚═════╝╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ")
    
#Main Menu

print ("")
print ("                                                                                         ----------")
print ("                                                                                        ¦ New Game ¦")
print ("                                                                                        ¦   Help   ¦")
print ("                                                                                        ¦   Quit   ¦")
print ("                                                                                         ----------")
print ("")
print ("")

menu_select = input("                                                                                 What would you like to do?\n")
menu_select = menu_select.lower()

while menu_select in Quit:
    print ("                                                        I didn't add a quit option so your gonna have to Alt + f4, if you wish to quit...")
    print ("                                                        ----------")
    print ("                                                        ¦Alt + f4¦")
    print ("                                                        ----------")
    asfjh = input("")
        
while menu_select not in NewGame:
    print ("")
    print ("                                                        This Option doesn't exist!")
    menu_select = input("                                                        What would you like to do?\n")
    menu_select = menu_select.lower()
    if menu_select in NewGame:
        break

while menu_select in NewGame:
    if NameChar == "":
        print ("")
        NameChar = input("Name your Character: ")
        if len(NameChar) not in namelength:
            print ("")
            print ("                                                                        The name is either to long or to short, please make it shorter/longer!")
            NameChar = input("Name your Character: ")
        if len(NameChar) in namelength:
            print ("                                                                        Do you wish to call your Character",NameChar,"?")
            NameChar_sure = input ("Your answer: ")
            NameChar_sure = NameChar_sure.lower()
            if NameChar_sure in Yes:
                break
            elif NameChar_sure in No:
                print ("")
                NameChar = input("Name your Character: ")
                print ("                                                                        Do you wish to call your Character",NameChar,"?")
                NameChar_sure = input ("Your answer: ")
                NameChar_sure = NameChar_sure.lower()
        elif NameChar_sure not in No:
            print ("")
            print ("                                                                        Give me a real answer!")
            NameChar_sure = input ("Your answer: ")
            
    if len(NameChar) in namelength:
        if NameChar_sure in Yes:
            break
        elif NameChar_sure in No:
            print ("")
            NameChar = input("Name your Character: ")
            print ("                                                                        Do you wish to call your Character",NameChar,"?")
            NameChar_sure = input ("Your answer: ")
            NameChar_sure = NameChar_sure.lower()
        elif NameChar_sure not in No:
            print ("")
            print ("                                                                        Give me a real answer!")
            NameChar_sure = input ("Your answer: ")
    if len(NameChar) not in namelength:
        print ("")
        print ("                                                                        The name is either to long or to short, please make it shorter/longer!")
        NameChar = input("Name your Character: ")

#Character Creation

print ("")
print ("")
print ("")
print ("                                                                        Welcome to the Character Creation!")
print ("")
print ("                                                                        What gender are you?")
gender = input ("I am ")
gender = gender.lower() 

while gender not in genders:
    print ("                                                                        That gender doens't exist!")
    print ("                                                                        Use a real gender!")
    print ("")
    gender = input ("I am ")
    gender = gender.lower()
    if gender in genders:
        break

while gender in genders:
    print ("")
    print ("                                                                        Are you sure about your Gender?")
    gender_sure = input ("Your answer: ")
    gender_sure = gender_sure.lower()
    if gender_sure in Yes:
        break
    if gender_sure not in No:
        print ("")
        print ("                                                                        Give me a real answer!")
        gender_sure = input ("Your answer: ")
    while gender_sure in No:
        if gender_sure in Yes:
            break
        print ("")
        gender = input ("I am ")
        gender = gender.lower()
        while gender not in genders:
            print ("                                                                        That gender doens't exist!")
            print ("                                                                        Use a real gender!")
            print ("")
            gender = input ("I am ")
            gender = gender.lower()
            if gender in genders:
                break
        print ("                                                                        Are you sure about your Gender?")
        gender_sure = input ("Your answer: ")
        gender_sure = gender_sure.lower()
        while gender_sure in No:
            if gender_sure in No:
                break
        if gender_sure in Yes:
            break
        while gender_sure not in No:
            print ("")
            print ("                                                                        Give me a real answer!")
            gender_sure = input ("Your answer: ")
            if gender_sure in Yes:
                break
            if gender_sure in No:
                break
    if gender_sure in Yes:
        break

#Kingdom Choice

print ("")
print ("                                                                        There are four kingdoms in the game:")
print ("")
print ("                                                                        The Kingdom of Astralgard, a nordic kindgom in the cold mountains, ruled by a Legion of Heroes.")
print ("                                                                        The Kingdom of Eisenheart, a kingdom in the forest, ruled by a Old King.")
print ("                                                                        The Kingdom of Syldria, a kingdom in the seas, ruled by Pirates.")
print ("                                                                        The Kingdom of Dileran, a kindgom in the dessert, ruled by a Demon King.")
print ("")
print ("                                                                        Which Kingdom do you choose?")
print ("")
print ("")
kingdomchoice = input ("I choose The Kingdom of ")

if kingdomchoice in kingdoms:
    print ("")
    print ("                                                                        Your Journey will begin in",kingdomchoice,"!")

while kingdomchoice not in kingdoms:
    print ("")
    print ("                                                                        This Kingdom doesn't exist!")
    kingdomchoice = input ("I choose The Kingdom of ")
    if kingdomchoice in kingdoms:
        print ("")
        print ("                                                                        Your Journey will begin in",kingdomchoice,"!")
        break

#Class Choice - BUG FIXING 

print ("")
print ("                                                                        But first you have to customize your Hero some more!")
print ("")
print ("                                                                        There are three Classes in the game:")
print ("")
print ("                                                                        The Warrior,a close range Class with a large amount of health.")
print ("                                                                        The Warrior uses a Axes, Swords, Maces and Shields. He has a lot of HP Points, but has low Stamina!")
print ("                                                                        He is one of the classic classes and is recommended for newcomers.")
print ("")
print ("                                                                        The Spellsword,DESCRIPTION MISSING.")
print ("                                                                        THIS CLASS WILL BE DEVELOPED LATER")
print ("")
print ("                                                                        The Rogue,a close range Class with a small amount of health.")
print ("                                                                        THIS CLASS WILL BE DEVELOPED LATER")
print ("                                                                        What Class do you choose?")

classchoice = input("I am a ")

while classchoice not in classes:
    print ("")
    print ("                                                                        That Class doesn't exist or is being developed!")
    print ("                                                                        What Class do you choose?")
    classchoice = input("I am a ")
    if classchoice in classes:
        break

while classchoice in classes:
    print ("                                                                        Are you sure about your choice?")
    class_sure = input ("Your answer: ")
    class_sure.lower()
    if class_sure in Yes:
        print ("")
        print ("                                                                        You are a",gender,",Warrior called",NameChar,"." )
        print ("                                                                        I wish you Luck and Fortune Hero!")
        break
    while class_sure not in No:
        print ("")
        print ("                                                                        Give me a real answer!")
        class_sure = input ("Your answer: ")
        if class_sure in Yes:
            break
        if class_sure in No:
            break
    while class_sure in No:
        print ("")
        classchoice = input("I am a ")
        while classchoice not in classes:
            print ("")
            print ("                                                                        That Class doesn't exist or is being developed!")
            print ("                                                                        What Class do you choose?")
            classchoice = input("I am a ")
            if classchoice in classes:
                break
        print ("                                                                     Are you sure about your choice?")
        class_sure = input ("Your answer: ")
        class_sure.lower()
        if class_sure in Yes:
            break
        while class_sure not in No:
            print ("")
            print ("                                                                        Give me a real answer!")
            class_sure = input ("Your answer: ")
            if class_sure in Yes:
                break
            if class_sure in No:
                break
    if class_sure in Yes:
        print ("")
        print ("                                                                        You are a",gender,",Warrior called",NameChar,"." )
        print ("                                                                        I wish you Luck and Fortune Hero!")
        break

#Exploring Towns and Traveling



#Basic Combat

player = Warrior(NameChar)
enemy = Dragon("Dragon")

def Combat(player,enemy):
	print ("")
	print ("                                                                        Your Party is under attack by a " + enemy.name)
	randomtext = input("                                                                        Press ENTER to continue")
	print ("")
	while player.isalive() and enemy.isalive():
		print ("                                                                        You attacked the " + enemy.name + "!")
		enemy.health = enemy.health - player.strength
		print("")
		print ("                                                                        The " + enemy.name + " attacked you!")
		print("")
		player.health = player.health - enemy.strength
	if player.isalive():
		print ("                                                                        You won!")
	else:
		print("                                                                        	You Died!")

Combat(player,enemy);
























                                                                                                    
DONTCLOSE = input("")
