import sys 
import random




class NormalMode:

    index_cavepath1_loc = 1
    index_cavepath2_loc = 2
    index_cavepath3 = 3
    index_cavepath4 = 4

    index_wumpus = 5
    index_bat = 6
    index_pit = 7
    index_arrow = 8

    def __init__(self, caves_nums):
        self.cave = []

        for caving in range(caves_nums)
            self.cave[caving] = [0, 0, 0, 0, False, False, False, False]

                self.cave[1] = {''}
        if caves_nums == '25':

            # 1 2 3 4 5
            # 6 7 8 9 10
            # 11 12 13 14 15
            # 16 17 18 19 20
            # 21 22 23 24 25

            #Cave Numbering = up, down, right, left, 4 things:                     
            self.cave[1] = [1, 6, 2, 1, False, False, False, False]
            self.cave[2] = [2, 7, 3, 1, False, False, False, False]
            self.cave[3] = [3, 8, 4, 2, False, False, False, False]
            self.cave[4] = [4, 9, 5, 3, False, False, False, False]
            self.cave[5] = [5, 10, 5, 4, False, False, False, False]
            self.cave[6] = [1, 11, 7, 6, False, False, False, False]
            self.cave[7] = [2, 12, 8, 6, False, False, False, False]
            self.cave[8] = [3, 13, 9, 7, False, False, False, False]
            self.cave[9] = [4, 14, 10, 8, False, False, False, False]
            self.cave[10] = [5, 15, 10, 9, False, False, False, False]
            self.cave[11] = [6, 16, 12, 11, False, False, False, False]
            self.cave[12] = [7, 17, 13, 11, False, False, False, False]
            self.cave[13] = [8, 18, 14, 12, False, False, False, False]
            self.cave[14] = [9, 19, 15, 13, False, False, False, False]
            self.cave[15] = [10, 20, 15, 14, False, False, False, False]
            self.cave[16] = [11, 21, 17, 16, False, False, False, False]
            self.cave[17] = [12, 22, 18, 16, False, False, False, False]
            self.cave[18] = [13, 23, 19, 17, False, False, False, False]
            self.cave[19] = [14, 24, 20, 18, False, False, False, False]
            self.cave[20] = [15, 25, 20, 19, False, False, False, False]
            self.cave[21] = [16, 21, 22, 21, False, False, False, False]
            self.cave[22] = [17, 22, 23, 21, False, False, False, False]
            self.cave[23] = [18, 23, 24, 22, False, False, False, False]
            self.cave[24] = [19, 24, 25, 23, False, False, False, False]
            self.cave[25] = [20, 25, 25, 24, False, False, False, False]
        else:
            sys.exit()

        #Adding my Wumpus :D
        wumpus_place = 0 #This makes sure that the Wumpus will actually be placed and not forgotten, I used while to make sure it will never skip this as that would remove the entire point of winning if no Wumpus.
        wumpus_in = 1
        while wumpus_in != wumpus_place:
            put_random = random.randrange(caves_nums)
            self.cave[put_random][index_wumpus] = True
            wumpus_place = wumpus_place + 1

        #Adding my Bat :D
        bat_place = 0
        bat_in = 1
        while pits_in != pits_place:
            put_random = random.randrange(caves_nums)
            if self.cave[put_random][index_wumpus] == False:
               self.cave[put_random][index_bat] = True
               bat_place = bat_place + 1

            

        #Adding my Pit :D
        pit_place = 0
        pit_in = 1
        while pit_in != pit_place:
            put_random = random.randrange(caves_nums)
            if (self.cave[put_random][index_wumpus] == False: and self.cave[put_random][index_bat] == False):
               self.cave[put_random][index_pit] = True
               pit_place = pit_place + 1

               







        #Adding my bat :D




        


    




class SimpleMode:

    cavepath1 = 1
    cavepath2 = 2
    cavepath3 = 3
    cavepath4 = 4

    wumpus = 5
    arrow1 = 6
    arrow2 = 7

    


class HardMode:

    cavepath1 = 1
    cavepath2 = 2
    cavepath3 = 3
    cavepath4 = 4

    wumpus = 5
    bat1 = 6
    bat2 = 7
    pit1 = 8
    pit2 = 9














def menu():  #This is my menu for the Wumpus game, I plan to make a few gamemodes here to make it unique and a rules sheet.
    print("Welcome to Hunt the Wumpus!")
    print("---------------------------\n")
    print("Menu Choices:")
    print("-------1. Play Normal Mode: ---------")
    print("-------2. Play Baby Mode: -----------")
    print("-------3. Play Hard Mode: -----------")
    print("-------4. Read Rules: ---------------")
    print("-------5. Exit Game: ----------------\n")
    game_choice = input("Please select an option between (1 to 5): ")

    if game_choice == '1':
        print("\nOk then, let's bring you into the classic version of the Hunt the Wumpus Game!\n")
        caves_nums = 25
        
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
        menu()
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
    menu_choice = input("Please select an option between (1 to 5): ")

    if menu_choice == '1':
        print("\nHere are the General Rules!")
        print("---------------------------\n")
        print("You are a hunter tasked to find and eliminate a putrid creature known as the Wumpus! This Wumpus hides in a cave system and it is your job to use your arrows to kill this Wumpus! Here are some of the fundamentals:\n")
        print("Player: You will start on a random tile in the cave and may have the option to go up, down, right, or left! The Wumpus will not move when you do, but that will not stop you from potentially running into it or other hazards.\n")
        continue_gen1 = input("Type anything to continue: ")
        print("\nArrows: The Player will start with a variety of arrows used to kill the Wumpus. Be warned though, shooting an arrow and not killing the Wumpus will startle it, causing it to flee to another tile in the cave or it could just kill you for fun right then and their. Arrows can be found maybe on certain tiles, but it depends on mode. Once you run out of arrows and tiles to collect them, you are most likely doomed, so just commit Wumpuside.")
        print("\nBats: Awaiting in the cave system could be a swarm of angry bats. If you run into bats, they will carry you and drop you onto a random tile in the cave. This random tile could be safe but also dangerous to potentially cause your death. In harder modes, the bats may just rip you into shreds. You cannot kill bats with arrows, so don't even try.\n" )
        continue_gen2 = input("Type anything to continue: ")
        print("\nPit: There can be deep pits in the cave that will cause your death if you walk onto the tile with one. The Wumpus can walk on these pits. Arrows of course are useless on a pit because you obviously can't kill it. Just avoid the pits to be okay.\n")
        print("Warnings: You will receive an audible warning if their is a draft, bats, or Wumpus near your cave tile. This will obviously help you avoid danger and kill the Wumpus for good.\n")
        print("Overall, those are the main rules, best of luck Player and kill that horrible Wumpus before he devours you like a jelly donut!\n")
        end_gen = input("Please type anything to return to rules sheet: ")
        rules_sheet()
    
    elif menu_choice == '2':
        print("\nHere are the Normal Game Mode Rules!")
        print("------------------------------------\n")
        print("Cave System: There will be 25 cave tiles 5 by 5 to navigate, you will be on a random one and could spawn into death possibly.\n")
        print("Arrows: You will start with 3 arrows. One tile in the cave will have a free backup arrow.\n")
        print("Bats and Pits: There will be one bat and one pit tile and you will get warning if near one.\n")
        continue_nor1 = input("Type anything to continue: ")
        print("\nWumpus: If you miss a shot the Wumpus will have an 80% to move and a 20% to kill you instantly from anywhere you are.")
        print("\nBats: Bats will not be able to kill you in this mode, just move you randomly, which could kill you if you are put on the wrong tile.\n")
        end_nor = input("Please type anything to return to rules sheet: ")
        rules_sheet()

    elif menu_choice == '3':
        print("\nHere are the Baby Game Mode Rules!")
        print("----------------------------------\n")
        print("Cave System: There will be 20 cave tiles 4 by 5 to navigate, you will be on a random one and could spawn into death possibly.\n")
        print("Arrows: You will start with 3 arrows. Two tiles in the cave will have a free backup arrow.\n")
        print("Bats and Pits: No bats or pits will spawn in this particular mode.\n")
        continue_sim1 = input("Type anything to continue: ")
        print("\nWumpus: If you miss a shot the Wumpus will have a 100% to move and none to kill you, unless it happens to land on you in random move.")
        end_sim = input("Please type anything to return to rules sheet: ")
        rules_sheet()
    elif menu_choice == '4':
        print("\nHere are the Hard Game Mode Rules!")
        print("----------------------------------\n")
        print("Cave System: There will be 36 cave tiles 6 by 6 to navigate, you will be on a random one and could spawn into death possibly.\n")
        print("Arrows: You will start with 2 arrows. No tiles will have an arrow on it.\n")
        print("Bats and Pits: There will be two bat and two pit tiles and you will get warning if near one.\n")
        continue_har1 = input("Type anything to continue: ")
        print("\nWumpus: If you miss a shot the Wumpus will have an 50% to move and a 50% to kill you instantly from anywhere you are.")
        print("\nBats: Bats will be able to kill you if you encounter one at 20%, and of course 80% to just move you randomly, which could kill you if you are put on the wrong tile.\n")
        end_har = input("Please type anything to return to rules sheet: ")
        rules_sheet()

    elif menu_choice == '5':
        print("\nReturning to menu!\n")
        menu()
    else:
        rules_sheet()
        print("Invalid Choice, please type 1,2,3,4,5 in the rules menu.\n")
   

print(menu())
