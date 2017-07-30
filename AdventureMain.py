#! /usr/bin/python3

import random

class NPCNames:
    def __init__(self):
        self.narrator = "Giles"
        self.king = "Wilhye"
NPC = NPCNames()

player = [""]

class Warrior:
    def __init__(self, name):
        self.name = name
        self.cName = "warrior"
        self.hp = 150
        self.ar = 4
        self.str = 3
        self.spd = 2
        self.int = 1
class Wizard:
    def __init__(self, name):
        self.name = name
        self.cName = "wizard"
        self.hp = 75
        self.ar = 2
        self.str = 1
        self.spd = 3
        self.int = 5
class Rouge:
    def __init__(self, name):
        self.name = name
        self.cName = "rouge"
        self.hp = 100
        self.ar = 2
        self.str = 4
        self.spd = 5
        self.int = 2

def startGame(NPC):
    print(NPC.narrator + ":")
    print("   Hello weary traveler, I hope your adventure has served you well.\n"
          "   My name is %s I am Tavilon's travel guide and will be helping\n"
          "   you prepare for vast adventures that await. King %s needs brave\n"
          "   adventurers to scout the land's of Tavilon and find it's mysterious\n"
          "   secrets. I can only train you in three arts, becoming a warrior,\n"
          "   wizard, or rouge. But do not worry, there are many more paths to\n"
          "   discover in these vast lands.\n"
          "\n"
          "   So what will it be hero? 'warrior', 'wizard', or ' rouge'." % (NPC.narrator, NPC.king))

def heroClass(player):
    userClass = input(">> ")
    if userClass == 'warrior':
        userInput = input("   So, you want to be a warrior? (y/n)\n>>")
        if userInput == 'y' or userInput == 'Y':
            userName = input("   What is your name hero?\n>>")
            player[0] = Warrior(userName)
            firstAct(NPC, player)
        elif userInput =='n' or userInput == 'N':
            print("   Alright, 'warrior', 'wizard', or ' rouge'.")
            heroClass(player)
        else:
            print("   I do not understand you.")
            print("   Alright, 'warrior', 'wizard', or ' rouge'.")
            heroClass(player)
    elif userClass == 'wizard':
        userInput = input("   So, you want to be a wizard? (y/n)\n>>")
        if userInput == 'y' or userInput == 'Y':
            userName = input("   What is your name hero?\n>>")
            player[0] = Wizard(userName)
            firstAct(NPC, player)
        elif userInput =='n' or userInput == 'N':
            print("   Alright, 'warrior', 'wizard', or ' rouge'.")
            heroClass(player)
        else:
            print("   I do not understand you.")
            print("   Alright, 'warrior', 'wizard', or ' rouge'.")
            heroClass(player)
    elif userClass == 'rouge':
        userInput = input("   So, you want to be a rouge? (y/n)\n>>")
        if userInput == 'y' or userInput == 'Y':
            userName = input("   What is your name hero?\n>>")
            player[0] = Rouge(userName)
            firstAct(NPC, player)
        elif userInput =='n' or userInput == 'N':
            print("   Alright, 'warrior', 'wizard', or ' rouge'.")
            heroClass(player)
        else:
            print("   I do not understand you.")
            print("   Alright, 'warrior', 'wizard', or ' rouge'.")
            heroClass(player)
    else:
        print("   I do not understand you.")
        print("   Alright, 'warrior', 'wizard', or ' rouge'.")
        heroClass(player)
        
def firstAct(NPC, p):
    print(NPC.narrator + ":")
    print("   Hello %s, you chose to be a %s. That is a mighty class with\n"
          "   %s health\n"
          "   %s armor\n"
          "   %s strenth\n"
          "   %s speed\n"
          "   %s intelligence\n\n"
          "   These values will change over the course of your travels, so prepare\n"
          "   for growth!"
          % (p[0].name, p[0].cName, p[0].hp, p[0].ar, p[0].str, p[0].spd, p[0].int))
    userInput = input("   Do you like these stats? (y/n)\n>>")
    if userInput == 'n' or userInput == 'N':
        print(NPC.narrator + ":")
        print("   What would you like to change your class too?")
        print("   Alright, 'warrior', 'wizard', or ' rouge'.")
        heroClass(player)
    elif userInput == 'y' or userInput == 'Y':
        print("   Welcome courageous %s" % (p[0].cName))
    
startGame(NPC)
heroClass(player)


