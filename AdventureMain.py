import random

class NPCNames:
    def __init__(self):
        self.narrator = "Giles"
        self.king = "Wilhye"
NPC = NPCNames()

class Warrior:
    def __init__(self, name):
        self.name = name
        self.hp = 150
        self.ar = 4
        self.str = 3
        self.spd = 2
        self.int = 1
class Wizard:
    def __init__(self, name):
        self.name = name
        self.hp = 75
        self.ar = 2
        self.str = 1
        self.spd = 3
        self.int = 5
class Rouge:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.ar = 2
        self.str = 4
        self.spd = 5
        self.int = 2

def startGame(NPC):
    print("   Hello weary traveler, I hope your adventure has served you well.\n"
          "   My name is %s I am Tavilon's travel guide and will be helping\n"
          "   you prepare for vast adventures that await. King %s needs brave\n"
          "   adventurers to scout the land's of Tavilon and find it's mysterious\n"
          "   secrets. I can only train you in three arts, becoming a warrior,\n"
          "   wizard, or rouge. But do not worry, there are many more paths to\n"
          "   discover in these vast lands.\n"
          "\n"
          "   So what will it be hero? 'warrior', 'wizard', or ' rouge'." % (NPC.narrator, NPC.king))


def heroClass():
    userClass = input(">> ")
    if userClass == 'warrior':
        userInput = input("   So, you want to be a warrior? (y/n)\n>>")
        if userInput == 'y' or userInput == 'Y':
            userName = input("   What is your name hero?\n>>")

        elif userInput =='n' or userInput == 'N':
            print("   Alright, 'warrior', 'wizard', or ' rouge'.")
            heroClass()

def classFunction(userName):
    player = Warrior(userName)
    return player

startGame(NPC)
heroClass()