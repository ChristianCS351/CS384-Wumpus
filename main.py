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
    game_choice = input("Please select an option between (1 to 4):")

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
    elif game_choice == '5'
        print("\nOk then, Goodbye :D")
        sys.exit
    else:
        print("Invalid Choice, please type 1,2,3,4,5 in the menu.\n")
    
   


