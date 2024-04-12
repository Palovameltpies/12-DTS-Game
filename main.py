import time
import random


#VERSON 10   note to self change this every time you upload to github

#Infected stats These are randomised
INFECTED = [
    {"Name": "Clicker", "Health": random.randint(5,8), "Attack": random.randint(3,5)},
    {"Name": "Runner", "Health": random.randint(2,6), "Attack": random.randint(3,5)},
    {"Name": "Bloater", "Health": random.randint(10,20), "Attack": random.randint(2,5)
     }]

#Scar Stats (WLF)
Scar = {"Name":"Scar",
        "Health": 8,
        "Attack": 4
        }


#2,4 Is blocked at the start of the game due to not having the key therefor it is set as FALSE
#3,5 Is blocked at the start of the game due to not having the chrowbar therefor it is set as FALSE
#This holds the values of the map, False statments are area's without any Value and Area's with a number is the ID of that area
area_adjacent  = [[False,False,False,False,"13",False,False,False,False],#0
                  [False,False,False,False,"12",False,False,False,False], #1
                  [False,False,False,False,False,False,False,"b14",False], #2
                  [False,"c14","c12","c11","10",False,"b12","b13",False], #3
                  [False,False,"c13",False,"09",False,False,"a12",False], #4
                  [False,False,False,False,"08",False,False,"a11",False], #5
                  [False,False,False,False,"07","a8","a9","a10",False], #6
                  [False,False,False,False,"06",False,False,False,False], #7
                  [False,False,False,False,"05",False,False,False,False], #8
                  [False,False,False,"03","04",False,False,False,False], #9
                  [False,False,False,"02",False,False,False,False,False], #10
                  [False,False,False,"01",False,False,False,False,False], #11
                  [False,False,False,False,False,False,False,False,False]] #12
                    #0    #1    #2   #3    #4    #5     #6   #7     #8

name = "place_holder_name"

#This function prints the inventory and how many itesm you have in the inventory
def show_inventory():
    print("-----Inventory-----")
    for i in range(len(inventory["Weapons"])):
        print(inventory["Weapons"][i])
    print(inventory["Bullets"], ": Bullets")
    print(inventory["Silencer"], " : Silencers")
    print(inventory["Molotov"], ": Molotovs")
    print(inventory["Shiv"], ": Shivs")
    print(inventory["Medkit"], ": MedKits")
    print("-----Resorces-----")
    print(inventory["Bottle"], ": Bottles")
    print(inventory["Alcohol"], ": Alcohol")
    print(inventory["Blade"], ": Blades")
    print(inventory["Tape"], ": Tape")
    print(inventory["Gun_powder"], ": Gun Powder")


#This function opens the crafting system
def crafting():
    show_inventory()
    print("-----Recipes-----")
    print("[1] : 1 Bottle + 2 Alcohol = Molotov(1)")
    print("[2] : 1 Blade + 1 Tape = Shiv(1)")
    print("[3] : 2 Tape + 1 Alcohol + 2 blade = Medkit(1)")
    print("[4] : 2 Bottles + 3 Gun_powder = Bullets(3)")
    print("[5] : 2 Bottles + 3 Tape = Silencer(2)")
    print("\n[6] To leave")

    #Crafting loop, untill the user crafts an item or leaves it will ask them what they want to craft
    while True:
            try:
                crafting_input = int(input(":"))
                if crafting_input == 1 and inventory["Bottle"] >= 1 and inventory["Alcohol"] >= 2:  # Crafting for Molotov
                    inventory["Bottle"] -= 1
                    inventory["Alcohol"] -= 2
                    inventory["Molotov"] += 1
                    print("You Craft one Molotov")
                    print("-1 Bottle")
                    print("-2 Alcohol")
                    print("+1 Molotov")
                    show_inventory()
                elif crafting_input == 2 and inventory["Blade"] >= 1 and inventory["Tape"] >= 1:  # Crafting for Shiv
                    inventory["Shiv"] += 1
                    inventory["Blade"] -= 1
                    inventory["Tape"] -= 1
                    print("You Craft one Shiv")
                    print("-1 Blade")
                    print("-1 Tape")
                    print("+1 Shiv")
                    show_inventory()

                elif crafting_input == 3 and inventory["Tape"] >= 2 and inventory["Alcohol"] >= 1 and inventory["Blade"] >= 2:  # Crafting for Medkit
                    inventory["Medkit"] += 1
                    inventory["Tape"] -= 2
                    inventory["Alcohol"] -= 1
                    inventory["Blade"] -= 2
                    print("You Craft one Medkit")
                    print("-2 Tape")
                    print("-1 Alcohol")
                    print("-2 Blades")
                    print("+1 Medkits")
                    show_inventory()

                elif crafting_input == 4 and inventory["Bottle"] >= 2 and inventory["Gun_powder"] >= 3:  # Crafting for Bullets
                    inventory["Bottle"] -= 2
                    inventory["Gun_powder"] -= 3
                    inventory["Bullets"] += 3
                    print("You Craft 3 Bullets")
                    print("-2 Bottles")
                    print("-3 Gun powder")
                    print("+3 Bullets")
                    show_inventory()
                elif crafting_input == 5 and inventory["Bottle"] >= 2 and inventory["Tape"] >= 3: #Crafting for silencerS
                    inventory["Bottle"] -= 2
                    inventory["Tape"] -= 3
                    inventory["Silencer"] += 2
                    print("You craft 2 silencers")
                    print("-2 Bottles")
                    print("-3 Tape")
                    print("+2 Silencers")
                    show_inventory()

                #Exit code
                elif crafting_input == 000:
                    intro()

                #Leaveing the function
                elif crafting_input == 6:
                    return
                else:
                    print("Please input a valid number")

            except ValueError:
                print("Please input A number")

# This is the loot fuctions this can be acted apon every location
def loot(a):
    # Checks if the area has been looted before
    if looted[str(a)] == False:
        for index in range(2):
            item_pick = random.randint(1, 5)  #Picks what item to find
            item_amount = random.randint(1, 3)  #Picks how many of that item they find
            # Bullets
            if item_pick == 1:
                inventory["Bullets"] += item_amount
                print("You found", item_amount, "Bullets")
            # Bottles
            elif item_pick == 2:
                inventory["Bottle"] += item_amount
                print("You found", item_amount, "Bottles")
            # Alcohol
            elif item_pick == 3:
                inventory["Alcohol"] += item_amount
                print("You found", item_amount, "Alcohol")
            # Tape
            elif item_pick == 4:
                inventory["Tape"] += item_amount
                print("You found", item_amount, "Tape")
            # Bottles
            elif item_pick == 5:
                inventory["Blade"] += item_amount
                print("You found", item_amount, "Blades")
            timer(1)
        return

    # If the area has been looted then it outputs the player found nothing
    else:
        print("You found Nothing")
        timer(1)
        return


# Prints out the Map
def map():
    print("-------------------------------------")
    print("               [12]                  ")
    print("               [11]          [b14]   ")
    print("[c14][c12][c11][10][b11][b12][b13]   ")
    print("     [c13]     [09]          [a12]   ")
    print("               [08]          [a11]   ")
    print("               [07][a08][a09][a10]   ")
    print("               [06]                  ")
    print("               [05]                  ")
    print("- N -      [03][04]                  ")
    print("W + E      [02]                      ")
    print("- S -      [01]                      ")
    print("-------------------------------------\n")


# Timer function, this shortens the amount of code needed when trying to run time.sleep
def timer(a):
    print("...")
    #time.sleep(a)
    return

#The start of the game
def intro():
    global inventory
    global attacked_before
    global looted
    global combat
    global player_health
    global next_area
    global current_area
    global has_map
    global name

    global information
    global dialogue
    #Reset all values so that when the player plays the game a 2nd time they don't keep items or can loot areas 2 times
    inventory = {"Weapons": ["Gun"],
                 "Bullets": 10,
                 "Silencer":3,
                 "Molotov": 0,
                 "Shiv": 0,
                 "Medkit": 0,
                 "Bottle": 3,
                 "Alcohol": 4,
                 "Blade": 2,
                 "Tape": 1,
                 "Gun_powder": 4

                 }

    #Checks if the area has been looted before
    looted = {"00": False,
              "01": False,
              "02": False,
              "03": False,
              "04": False,
              "05": False,
              "06": False,
              "07": False,
              "08": False,
              "09": False,
              "10": False,
              "11": False,
              "12": False,

              "a8": False,
              "a9": False,
              "a10": False,
              "a11": False,
              "a12": False,
              "a13": False,

              "b11": False,
              "b12": False,
              "b13": False,
              "b14": False,

              "c11": False,
              "c12": False,
              "c13": False,
              "c14": False}
    attacked_before = {
              "03":False,
              "06":False,
              "09":False,
              "a9":False,
              "a12":False,
              "b14":False,
              "c14":False
    }

    #Holds current combat values
    combat = []
    player_health = 1000
    next_area = "00"
    current_area = "00"
    has_map = False

    #Introduction
    print("Welcome to the Tunnels")
    print("PLEASE NOTE THAT EVERY INPUT WILL RESTART THE GAME IF INPUTED '000'")
    #Gets input for the usersname
    name = str(input("Please input a name\n:"))
    if name == "000": #Exit code
        intro()
    while True:
        try:
            #Confrims if the play would like to keep their name or change it
            confirm = int(input("1 To Confirm\n2 To Input a different name\n:"))
            if confirm == 1:
                break
            if confirm == 2:
                name = str(input("Please input a name\n:"))
            if confirm == 000: #Exit code
                intro()
            else:
                print("Please input a valid number")

        except ValueError:
            print("Please input a valid input")


    name = ""
    # Holds all the information that is convayed  to the player
    information = {"Movement": ["This game has an area system",
                                "You can only move in 2 dimension (Up, Down, left, Right)",
                                "When not in combat you are able to move in these directions at any time",
                                "When choseing a direction to move in you press",
                                "W for forward (up)",
                                "S for Backwards (Down)",
                                "D for Right",
                                "A for Left",
                                "Have Fun :)"],
                   "Combat": ["This game has combat",
                              "When in combat you will be against a specific number of infected or scars",
                              "Every turn you will be able to attack with a choice of 3 weapons",
                              "Gun : Makes noise (*Silencers make no noise), low damage",
                              "Molotov : Makes noise, high damage, difficult to craft",
                              "Shiv : Silence, instant kill, can only use when in stealth",
                              "As long as you stay silent you will not be attacked and this means you won't take damage",
                              "Once the enemy know your their you only get attacked by them one at a time"],
                   "Crafting": ["In this game you will need to craft items to use in combat",
                                "Every time you enter an area you are able to loot the area",
                                "Note: you cannot loot the same area more than once",
                                "You can find Bottles which can be used to craft bullets or molotov's or silencers",
                                "You can find Alcohol which can be used to craft medkit's or molotov's",
                                "You can find Blades which can be used to craft shivs or medkit's",
                                "You can find Tape which can be used the craft shivs or medkit's or silencers",
                                "You can find gun powder which can be used to craft bullets"]
                   }
    # Holds all the dialogue between characters inside the game
    dialogue = {"Part 1": ["Part 1 - The Tunnel",
                           ("Radio - Hey, "+ name+ " You there?"),
                           (name+ " - Yea im here?"),
                           "Radio - So you remeber when the scars took out our western base?",
                           (name+ " - Yes they took those people hostages"),
                           "Radio - Welllll, Issac had intell that the scars where keeping them hostage in these tunnels",
                           (name+ " - You're shitting me"),
                           (name+ " - Aren't these the tunnels where all those hoards bloaters are traped?"),
                           "Radio - Yep",
                           (name+ " - And you sent me in, alone, with 10 bullets"),
                           "Radio - Its fine we just need you to scout for us",
                           "Radio - Also we trap the bloaters on the other side of the system, there blocked off by the train's",
                           (name+ " - Im not going this im going back to the stadium"),
                           "Radio - If you come back you will be hung, Issac will not appreciate you leaving your post",
                           (name+ " - Just to scout?"),
                           "Radio - Yes, just to scout",
                           "Radio - Goodluck"],
                "Part 2": ["As you move forwards you hear people talking",
                           "You pear through a crack in a door and see the hostages",
                           "Scar 1 - Does anyone know how the hell we get out of these tunnels",
                           "Scar 2 - No dumbass were suck in here",
                           "Scar 1 - There must be a way out",
                           "Scar 2 - We could keep looking through the tunnels?",
                           "Scar 1 - If you want to become infected then be my guest",
                           "Scar 3 - Shut up your going to attracted them",
                           (name+ " - *clash"),
                           "You knocked over a bottle",
                           "Scar 3 - *Wistle",
                           "Scar 2 - *Wistle",
                           "Scar 1 - *Wistle",
                           "You regognise the first wistle it is code for flank them",
                           "Be ready to enter combat",
                           "You pick up a piece of glass on the floor"],
                "Conclusion": [("Radio - Hey "+ name+ " whats your 20?"),
                               (name+ " - I just found the hostages"),
                               (name+ " - I also took out the scars"),
                               "Radio - You did fucking what",
                               "Radio - Get the hell out of there now",
                               "You find a ladder that leads towards a man hole",
                               "You climb the ladder",
                               "You open the man hole and smell the fresh air",
                               (name+ " - Im out")],
                "Area 3": [(name+ " - HEY THERE ARE INFECTED IN THE TUNNELS"),
                           "Radio - wh^#&@% @*HE CON#&@(T#ON I*# B@* @E C@9N'*# HE(*R Y)*",
                           (name+ " - fuck there isn't a connection"),
                           (name+ " I need to find a way out of here")]
                }



    #Additional information for the player
    while True:
        try:
            print("Would you like more to know how to play?")
            more_info = int(input("1 to learn about movement\n2 to learn about combat\n3 to learn about crafting\n4 to leave\n:"))

            if more_info == 1: #Learn about player movment
                for i in information["Movement"]:
                    print(i)
                    timer(3.5)

            elif more_info == 2:#Learn about combat
                for i in information["Combat"]:
                    print(i)
                    timer(3.5)

            elif more_info == 3:# Learn about looting and crafting
                for i in information["Crafting"]:
                    print(i)
                    timer(3.5)
            elif more_info == 4: # Exit to contiune
                print("Goodluck")
                timer(1.5)
                break
            elif more_info == 000:
                intro()

            else:
                print("Please input a valid number")


        except ValueError:
            print("Please input a valid input")


    print("Game Loading")
    timer(2)
    part_1()



#Start of the game
def part_1():
    # Introduction

    #For loop that gets the first value inside the dialogue dictionary and prints it, this then loops until it has printed every piece of dialogue inside the list
    for i in dialogue["Part 1"]:
        print(i)
        timer(3.5)

    #Area 00 (Before you enter the tunnels)
    while True:
        print("You can go forward into to tunnels(W) or look for loot(L)")
        player_action = str(input(":"))
        player_action = player_action.upper()
        #Player "Starts the game" by moving forwards them into area 1
        if player_action == "W":
            area_1()
            break
        #Loots area 00
        elif player_action == "L":
            loot("00")
            looted["00"] = True

        #Exit code
        elif player_action == "000":
            intro()
        else:
            print("Invalid input Please try again")

#Area(y = y value of the area, x = x value of the area, a =  Area name, b =  text a, c = text b )
def area_general(y,x,a,b,c):
    global next_area
    global has_map
    current_area = a
    current_location = [x,y]
    print(current_area)
    #If the player has the map then it prints
    if has_map == True:
        map()

    #Prints the text A and Text B
    print(b)
    print(c)

    #Checks if the current area the player is in has adjacent areas by checking the Nested list
    while True:

        #If the Value in front of the current area inside area_adjacent has a value other than False it tells the player they can move in that direction,
        #This also runs for every other direction, x and y axis
        if area_adjacent[y-1][x]:
            print("You see a tunnel forward(W)\n")

        if area_adjacent[y][x-1]:
            print("You see a tunnel to the Left(A)\n")

        if area_adjacent[y][x+1]:
            print("You see a tunnel to the Right(D)\n")

        if area_adjacent[y+1][x]:
            print("You can go backwards(S)\n")

        #If they player dosen't have the map they can find it
        if has_map == False:
            print("You can look around(E)")

        #If the player has looted the area it checks
        if looted[current_area] == False:
            print("You can loot(L)")

        print("You can craft (Q)")

        #Gets the players action for turn Eg, Craft, loot, move
        player_action = str(input(":"))
        player_action = player_action.upper()  #Makes the players actin upper case

        #Movment for the player, First it checks if the area adjancent has a value, if it does then it checks if the player inputed that direction,
        #Once it has checked if it can move there and the player wants to move there it prints the direction they more and sets next_area to the adjacent area's value eg "c12"
        if area_adjacent[y-1][x]:
            if player_action == "W":
                print("Forward")
                next_area = area_adjacent[y-1][x]
                return #Returns the player to main, this then means that the "Next_area" is different and it will run Main differently

        if area_adjacent[y][x-1]:
            if player_action == "A":
                print("Left")
                next_area = area_adjacent[y][x - 1]
                return

        if area_adjacent[y+1][x]:
            if player_action == "S":
                print("Down")
                next_area = area_adjacent[y+1][x]
                return

        if area_adjacent[y][x+1]:
            if player_action == "D":
                print("Right")
                next_area = area_adjacent[y][x+1]
                return


        if player_action == "000": #Exit code
            intro()

        #You find the map if the player dosn't have the map and it was their action
        if player_action == "E" and has_map == False:
            print("You look around")
            timer(2)
            print("You find a piece of paper")
            timer(1)
            print("Its a map of the tunnel system")
            timer(1)
            map()
            timer(2)
            has_map = True #Makes sure the player cannot find the map twice
        #Loots
        elif player_action == "L":
            loot(current_area)
            looted[current_area] = True
        # This is for crafting
        elif player_action == "Q":
            crafting()
        else:
            print("Invalid input")

def combat_func(a,b):  # Combat
    #Rests combat based variables
    player_health_gain = 0
    global player_health
    global INFECTED
    global Scar
    combat = []
    visable = False

    #Gets a random amount of infected enemys and appends them into a list (a = number of enemys)
    #If b == "infe" combat gets appened with infected enemies
    if b == "infe":
        for i in range(a):
            combat.append(INFECTED[random.randint(0, 2)])
            print(combat[i]["Name"])
    #If b == "scar" combat gets appened with scars

    if b == "scar":
        for i in range(a):
            combat.append(Scar)
            print(combat[i]["Name"])

    #To make sure when you kill all the enemys it dosn't give you an index out of range error
    combat.append({"Name": "Place_Holder_Mikio", "Health": 999999999, "Attack": 0})

    #If the player is not visable
    while visable == False:
        # Choses Attack
        while True:
            # Win
            if len(combat) == 1:
                combat.pop(0)
                print("You won")
                timer(1)
                return
            print("You can attack with")
            print("1 : Gun *Noise(", inventory["Bullets"], "Bullets) - ", inventory["Silencer"], "Silencers")
            print("2 : Molotov *Noise(", inventory["Molotov"], "Molotovs)")
            if not visable: #If the player is visable they cannot use the SHIV
                print("3 : Shiv(", inventory["Shiv"], "Shivs)")
            else:
                print("3 : Shiv CANNOT USE YOU HAVE BEEN SPOTTED")
            print("4 : Medkit(", inventory["Medkit"], "Medkits)")

            try:
                #Gets the players attack choice set into the variable of "Attack"
                attack = int(input(":"))
                if attack == 1 and inventory["Bullets"] > 0:  # Attack with gun
                    combat[0]["Health"] -= 4 #Removes health from the enemy
                    inventory["Bullets"] -= 1 #Uses that item
                    if inventory["Silencer"] > 0: #If they have a silencer
                        print("You use a silencer")
                        timer(0.5)
                        inventory["Silencer"] -= 1
                    else:# If they don't have a silencer
                        visable = True
                        print("You make noise")
                        timer(0.5)
                        print("You shot a", combat[0]["Name"], "And dealt 4 damage")

                elif attack == 2 and inventory["Molotov"] > 0:  # Attack with molotov
                    combat[0]["Health"] -= 10
                    visable = True
                    inventory["Molotov"] -= 1
                    print("You make noise")
                    timer(0.5)
                    print("You throw a molotov at a", combat[0]["Name"], "And dealt 10 Damage")

                elif attack == 3 and inventory["Shiv"] > 0 and visable == False:  # Attack with shiv
                    combat[0]["Health"] -= 20
                    inventory["Shiv"] -= 1
                    print("You shank a", combat[0]["Name"])


                elif attack == 4 and inventory["Medkit"] > 0:  # MedKit
                    if player_health < 15:
                        player_health_gain += random.randint(2, 6)
                        timer(0.5)
                        print("You Gained", player_health_gain, "Health")
                        player_health += player_health_gain

                        inventory["Medkit"] -= 1
                    else:
                        print("You have max health")
                elif attack == 000: #Exit code
                    intro()

                else:
                    print("You don't have any of that item >:(")
                #If you INFECTED has less than 0 health
                if combat[0]["Health"] <= 0:
                    timer(0.5)
                    print("You killed a", combat[0]["Name"])
                    combat.pop(0) #Removes the infected from the combat list

                #If you become visbale to the enemy they will attack
                if visable == True and len(combat) != 1:
                    print("You get attacked by an", combat[0]["Name"])
                    print("You take", combat[0]["Attack"], "Damage")

                    player_health -= combat[0]["Attack"]

                    print("You have", player_health, "Health")

                #Death
                if player_health <= 0:
                    print("You die")
                    combat.pop(0)
                    timer(2)
                    #Try again, asks the player if they would like to leave or try again
                    while True:
                        try:
                            print("Would you like to try again\n1 To Try again\n2 To Exit\n:")
                            try_again = int(input(":"))
                            if try_again == 1 or try_again == 000:
                                timer(1)
                                intro()
                            elif try_again == 2:
                                print("Thank you for playing")
                                exit(2)

                        except ValueError:
                            print("Please input a valid number")






            except ValueError:
                print("Input Error Please try again")


#Part 2 this is when you find the hostages at the end of the game
def part_2():
    for i in dialogue["Part 2"]:
        print(i)
        timer(3.5)

    print("+1 Shiv")
    inventory["Shiv"] += 1
    combat_func(3,"scar")

    for i in dialogue["Conclusion"]:
        print(i)
        timer(3.5)

    print("THANK YOU FOR PLAYING YOU WON")
    while True:
        play_again = str(input("Would you like to play again\nY for yes\nN for no\n"))
        play_again = play_again.upper()
        if play_again == "Y" or play_again == "000":
            intro()
        elif play_again == "N":
            exit()

#Creates an function for every area in the game
def area_1():
    area_general(11, 3, "01", "You move forwards into the tunnels", "You don't see anything")
def area_2():
    area_general(10, 3, "02", "You find an opening, there seems to have bottles lying around", "Hear A noise Ahead")
def area_3(): #Has Combat
    if attacked_before["03"] == False:
        combat_func(1,"infe")
        attacked_before["03"] = True


    #Progress in the story
    for i in dialogue["Area 3"]:
        print(i)
        timer(3.5)

    area_general(9, 3, "03", "", "")


def area_4():
    area_general(9, 4, "04", "You See can far ahead of you", "You see the remains of dead infected")

def area_5():
    area_general(8, 4, "05", "You can still see far ahead of you ", "This causes you to feel very alone")

def area_6(): #Has Combat
    if attacked_before["06"] == False:
        combat_func(2, "infe")
        attacked_before["06"] = True

    area_general(7, 4,"06", "The amount of infected causes you to feel worried", "You find a fire still smoking, people are nearby")

def area_7():
    area_general(6, 4, "07", "You see spore to the right of you", "You find a carving of a wooden statue resembling a woman with the words Feel Her love inscribed into the back ")

def area_8():
    area_general(5, 4, "08", "You hear a noise ahead, could it be the scars?", "")

def area_9(): #Has Combat
    if attacked_before["09"] == False:
        combat_func(2, "infe")
        attacked_before["09"] = True
    area_general(4, 4, "09", "", "")

def area_10():
    area_general(3, 4, "10", "You see a locked door in front of you maybe there is a key some where around here?", "There is a cave in to the right of you, maybe something will let you get through it.")

def area_11():
    area_general(2, 4, "11", "Opening the door you find ladders and wooden crates scatered around the place", "This must be a scar base")

def area_12():
    area_general(1, 4, "12", "You see movement ahead", "It didn't look like a infected")


#A
def area_a8():
    print("----SPORES----")
    area_general(6, 5, "a8", "Putting on your mask you walk through the spores", "")

def area_a9(): #Has Combat
    if attacked_before["a9"] == False:
        combat_func(3, "infe")
        attacked_before["a9"] = True
    print("----SPORES----")
    area_general(6, 6, "a9", "These tunnel are crawling with infected you need to figure out where the scars have taken the hosteges", "And get the hell out of here")

def area_a10():
    print("----SPORES----")
    area_general(6, 7, "a10", "", "")

def area_a11():
    print("----SPORES----")
    area_general(5, 7, "a11", "Even more noise ahead expect infected as you are still inside spores", "")

def area_a12(): #Has Combat
    if attacked_before["a12"] == False:
        combat_func(3, "infe")
        attacked_before["a12"] = True
    print("----SPORES----")
    area_general(4, 7, "a12", "Fucking infected", "The spores seem to end ahead of you")



#B Area's
def area_b11():
    area_general(3, 5, "b11", "", "")

def area_b12():
    area_general(3, 6, "b12", "", "")

def area_b13():
    area_general(3, 7, "b13", "You see spores behind you", "")

def area_b14(): #Has Combat
    if attacked_before["b14"] == False:
        combat_func(2, "infe")
        attacked_before["b14"] = True

    area_general(2, 7, "b14", "You find a key? I wonder what it is for?", "")
    area_adjacent[2][4] = "11"

#C Area's
def area_c11():
    area_general(3, 3, "c11", "", "")

def area_c12():
    area_general(3, 2, "c12", "", "")

def area_c13():
    area_general(4, 2, "c13", "", "")

def area_c14(): # Has Combat
    if attacked_before["c14"] == False:
        combat_func(2, "infe")
        attacked_before["c14"] = True

    area_general(3, 1, "c14", "One of the infected had a crowbar on them", "What could this help open")
    area_adjacent[3][5] = "b11"


# MAIN
intro()
# next_area changes when the user inputs in the general area function
while True:
    if next_area == "01":
        area_1()
    elif next_area == "02":
        area_2()
    elif next_area == "03":
        area_3()
    elif next_area == "04":
        area_4()
    elif next_area == "05":
        area_5()
    elif next_area == "06":
        area_6()
    elif next_area == "07":
        area_7()
    elif next_area == "08":
        area_8()
    elif next_area == "09":
        area_9()
    elif next_area == "10":
        area_10()
    elif next_area == "11":
        area_11()
    elif next_area == "12":
        area_12()
    elif next_area == "13":
        part_2()

    elif next_area == "a8":
        area_a8()
    elif next_area == "a9":
        area_a9()
    elif next_area == "a10":
        area_a10()
    elif next_area == "a11":
        area_a11()
    elif next_area == "a12":
        area_a12()



    elif next_area == "b11":
        area_b11()
    elif next_area == "b12":
        area_b12()
    elif next_area == "b13":
        area_b13()
    elif next_area == "b14":
        area_b14()


    elif next_area == "c11":
        area_c11()
    elif next_area == "c12":
        area_c12()
    elif next_area == "c13":
        area_c13()
    elif next_area == "c14":
        area_c14()















