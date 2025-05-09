import sys 

def menu():  #This is my menu for the Wumpus game, I plan to make a few gamemodes here to make it unique and a rules sheet.
    print("Welcome to Hunt the Wumpus!")
    print("---------------------------\n")
    print("Menu Choices:")
    print("-------1. Play Normal Mode: ---------")
    print("-------2. Play Baby Mode: -----------")
    print("-------3. Play Hard Mode: -----------")
    print("-------4. Read Rules: ---------------")
    print("-------5. Exit Game: ----------------\n")
    game_choice = input("Please select an option between (1 to 5):")

    if game_choice == '1':
        print("\nOk then, let's bring you into the classic version of the Hunt the Wumpus Game!\n")
    elif game_choice == '2':
        print("\nOk then, let's bring you into the simple version of Hunt the Wumpus Game!\n")
    elif game_choice == '3':
        print("\nOk then, you will be sorry :D. Let's bring you into the hard version of the Hunt the Wumpus Game!\n")
    elif game_choice == '4':
        print("\nOk then, taking you to rules!\n")
        rules_sheet()
    elif game_choice == '5':
        print("\nOk then, Goodbye :D")
        sys.exit()
    else:
        print("Invalid Choice, please type 1,2,3,4,5 in the game menu.\n")
    

def rules_sheet():
    print("Welcome to the Rules Sheet, Your Guide to Know How to Play!")
    print("-----------------------------------------------------------\n")
    print("\nOk, what would you like to learn about? Just Select the Number Options:")
    print("-------1. General Rules: ---------")
    print("-------2. Normal Mode Rules: -----------")
    print("-------3. Baby Mode Rules -----------")
    print("-------4. Hard Rules: ---------------")
    print("-------5. Return to Menu: ----------------\n\n")
    menu_choice = input("Please select an option between (1 to 5):")

    if menu_choice == '1':
        print("\nHere are the General Rules!")
        print("---------------------------\n")
        print("You are a hunter tasked to find and eliminate a putrid creature known as the Wumpus! This Wumpus hides in a cave system \
        and it is your job to use your arrows to kill this Wumpus! Here are some of the fundamentals:\n")
        ("Player: You will start on a random tile in the cave and may have the option to go up, down, right, or left! The Wumpus will \
        not move when you do, but that will not stop you from potentially running into it or other hazards.\n")
        continue_gen1 = input("Please type 1 if you wish to continue explanation")

        if continue_gen1 == '1':
            print("\nArrows: The Player will start with a variety of arrows used to kill the Wumpus. Be warned though, shooting an \
            arrow and not killing the Wumpus will startle it, causing it to flee to another tile in the cave or it could just kill you \
            for fun right then and their. Arrows can be found maybe on certain tiles, but it depends on mode. Once you run out of arrows \
             and tiles to collect them, you are most likely doomed, so just commit Wumpuside.")
            print("\nBats: Awaiting in the cave system could be a swarm of angry bats. If you run into bats, they will carry you and \
            drop you onto a random tile in the cave. This random tile could be safe but also dangerous to potentially cause your death. \
            In harder modes, the bats may just rip you into shreds. You cannot kill bats with arrows, so don't even try.\n" )
            continue_gen2 = input("Please type 1 if you wish to continue explanation")
        else:
            print("Invalid: Waiting for 1")

            if continue_gen2 == '1':
                print("\nPit: There can be deep pits in the cave that will cause your death if you walk onto the tile with one. The Wumpus can walk on these pits. \
                Arrows of course are useless on a pit because you obviously can't kill it. Just avoid the pits to be okay.\n")
                print("Warnings: You will receive an audible warning if their is a draft, bats, or Wumpus near your cave tile. \
                This will obviously help you avoid danger and kill the Wumpus for good.\n")
                print("Overall, those are rules best of luck Player and kill that horrible Wumpus before he devours you like a jelly donut!\n")
                end_gen = input("Please type 1 to return to rules sheet")
            else:
                print("Invalid: Waiting for 1")
                
                if end_gen == '1':
                    rules_sheet()
                else:
                    print("Invalid: Waiting for 1")           
    
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
        menu()
    else:
        print("Invalid Choice, please type 1,2,3,4,5 in the rules menu.\n")
   

print(menu())
