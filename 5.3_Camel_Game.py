'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''

Done = False
import random
Thirst = 0
Canteen = 3
MLS_AHD = 0 #miles ahead of the natives
Camel_eng = 0
Natives = -20 #how far away the natives are
print("In this game you are supposed to travel the desert with your camel while running away from natives.")
print("You have to manage your camels energy and your health as well to make sure your camel dosent die or")
print("you dehydrate. if you make it 200 miles you win the game good luck!")
print()
while not Done:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")

    if Natives >= MLS_AHD:
        print()
        print("The natives caught up to you Your dead")
        print()
        Done = True
    elif Natives-MLS_AHD >= 15:
        print()
        print("The natives are getting close")
        print()
    if Thirst > 4:
        print()
        print("You are thirsty")
        print()
    elif Thirst > 6:
        print()
        print("You died of thirst!")
        print()
        Done = True
    if Camel_eng > 5:
        print()
        print("Your camel is getting tired.")
        print()
    elif Camel_eng > 8:
        print()
        print("Your camel is dead.")
        print()
        Done = True
    if MLS_AHD >= 200:
        print()
        print("You Won")
        print()
        Done = True
    PLR = input("What would you like to do? ")

    if PLR.lower() == "a":
        print()
        if Canteen == 0:
            print("You ran out of Water")
        else:
            Canteen = Canteen - 1
            Thirst = 0
            print("You have",Canteen,"drinks left")
            print()

    elif PLR.lower() == "b":
        print()
        Oasis = (random.randrange(1, 21))
        if Oasis == 8:
            Camel_eng = 0
            Canteen = 3
            Thirst = 0
            PLR_Mile = (random.randrange(5, 13))
            MLS_AHD = MLS_AHD + PLR_Mile
            NTV_Mile = (random.randrange(7, 15))
            Natives = Natives + NTV_Mile
            print("YOU FOUND AN OASIS")
            print("you moved", PLR_Mile, "miles")
            print("The natives are", MLS_AHD - Natives, "miles away")
            print()
        else:
            PLR_Mile = (random.randrange(5, 13))
            MLS_AHD = MLS_AHD + PLR_Mile
            NTV_Mile = (random.randrange(7, 15))
            Natives = Natives + NTV_Mile
            Thirst = Thirst + 1
            Camel_eng = Camel_eng + 1
            print("you moved",PLR_Mile,"miles")
            print("The natives are", MLS_AHD - Natives, "miles away")
            print()

    elif PLR.lower() == "c":
        print()
        Oasis = (random.randrange(1, 21))
        if Oasis == 8:
            Camel_eng = 0
            Canteen = 3
            Thirst = 0
            PLR_Mile = (random.randrange(10, 20))
            MLS_AHD = MLS_AHD + PLR_Mile
            NTV_Mile = (random.randrange(7, 15))
            Natives = Natives + NTV_Mile
            print("YOU FOUND AN OASIS")
            print("you moved", PLR_Mile, "miles")
            print("The natives are", MLS_AHD - Natives, "miles away")
            print()
        else:
            PLR_Mile = (random.randrange(10, 20))
            MLS_AHD = MLS_AHD + PLR_Mile
            NTV_Mile = (random.randrange(7, 15))
            Natives = Natives + NTV_Mile
            Thirst = Thirst + 1
            CML_Mile = (random.randrange(1, 4))
            Camel_eng = Camel_eng + CML_Mile
            print("you moved", PLR_Mile, "miles")
            print("The natives are", MLS_AHD - Natives, "miles away")
            print()

    elif PLR.lower() == "d":
        print()
        NTV_Mile = (random.randrange(7, 15))
        Natives = Natives + NTV_Mile
        Camel_eng = 0
        print("The Camel is happy.")
        print("The natives are", MLS_AHD - Natives, "miles away")
        print()

    elif PLR.lower() == "e":
        print()
        print("Your Thirst is at:", Thirst)
        print("You have",Canteen,"drinks left")
        print("Your camels tiredness is", Camel_eng)
        print("The natives are", MLS_AHD - Natives, "miles away")
        print()
    else:
        Done = True








