import random

def menu():  #This is my menu for the Wumpus game, I plan to make a few gamemodes here to make it unique and a rules sheet.
    print("Welcome to Hunt the Wumpus!")
    print("---------------------------/n/n")
    print("Menu Choices:")
    print("-------1. Play Normal Mode: ---------")
    print("-------2. Play Baby Mode: -----------")
    print("-------3. Play Hard Mode: -----------")
    print("-------4. Read Rules: ---------------")
    print("-------5. Exit Game: ----------------\n\n")
    game_choice = input("Please select an option between (1 to 5):")

    if game_choice == '1':
        print("\nOk then, let's bring you into the classic version of the Hunt the Wumpus Game!\n")
        PlayNormal()
    elif game_choice == '2':
        print("\nOk then, let's bring you into the simple version of Hunt the Wumpus Game!\n")
        PlayBaby()
    elif game_choice == '3':
        print("\nOk then, you will be sorry :D. Let's bring you into the hard version of the Hunt the Wumpus Game!\n")
        PlayHard()
    elif game_choice == '4':
        print("\nOk then, Goodbye :D")
        rules_sheet()
    elif game_choice == '5':
        print("\nOk then, Goodbye :D")
        sys.exit
    else:
        print("Invalid Choice, please type 1,2,3,4,5 in the game menu.\n")
    

def rules_sheet():
    print("Welcome to the Rules Sheet, Your Guide to Know How to Play:")
    print("\nOk, what would you like to learn about? Just Select the Number Options:")
    print("-------1. General Rules: ---------")
    print("-------2. Normal Mode Rules: -----------")
    print("-------3. Baby Mode Rules -----------")
    print("-------4. Hard Rules: ---------------")
    print("-------5. Return to Menu: ----------------\n\n")
    menu_choice = input("Please select an option between (1 to 5):")

    if menu_choice == '1':
        print("\nHere are the General Rules!")
        print("----------------------")
    elif menu_choice == '2':
        print("\nHere are the Normal Game Mode Rules!")
        print("----------------------")
    elif menu_choice == '3':
        print("\nHere are the Baby Game Mode Rules!")
        print("----------------------")
    elif menu_choice == '4':
        print("\nHere are the Hard Game Mode Rules!")
        print("----------------------")
    elif menu_choice == '5':
        print("\nReturning to menu!\n")
        sys.exit
    else:
        print("Invalid Choice, please type 1,2,3,4,5 in the rules menu.\n")
   


