import time
import random


#VERSON 2   note to self change this every time you upload to github

#Infected stats
INFECTED = [
    {"Name": "Clicker", "Health": 8, "Attack": 5},
    {"Name": "Runner", "Health": 4, "Attack": 4},
    {"Name": "Bloater", "Health": 20, "Attack": 5
     }]

#Scar Stats (WLF)
Scar = {"Health": 8,
       "Attack": 4
       }


#2,4 Is blocked at the start of the game due to not having the key therefor it is set as FALSE
#3,5 Is blocked at the start of the game due to not having the chrowbar therefor it is set as FALSE

area_adjacent  = [[False,False,False,False,False,False,False,False,False],#0
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
                    #0    #1    #2   #3    #4    #5     #6   #7     #8S

def show_inventory():
    print("-----Inventory-----")
    for i in range(len(inventory["Weapons"])):
        print(inventory["Weapons"][i])
    print(inventory["Bullets"], ": Bullets")
    print(inventory["Molotov"], ": Molotovs")
    print(inventory["Shiv"], ": Shivs")
    print(inventory["Medkit"], ": MedKits")

def crafting():
    show_inventory()
    print("-----Resorces-----")
    print(inventory["Bottle"], ": Bottles")
    print(inventory["Alcohol"], ": Alcohol")
    print(inventory["Blade"], ": Blades")
    print(inventory["Tape"], ": Tape")
    print(inventory["Gun_powder"], ": Gun Powder")
    print("-----Recipes-----")
    print("[1] : 1 Bottle + 2 Alcohol = Molotov(1)")
    print("[2] : 1 Blade + 1 Tape = Shiv(1)")
    print("[3] : 2 Tape + 1 Alcohol + 2 blade = Medkit(1)")
    print("[4] : 2 Bottles + 3 Gun_powder = Bullets(3)")
    print("\n[5] To leave")
    while True:
        crafting_input = int(input(":"))
        if crafting_input == 1 and inventory["Bottle"] >= 1 and inventory["Alcohol"] >= 2:  # Crafting for Molotov
            inventory["Molotov"] += 1
            print("You Craft one Molotov")
            print("-1 Bottle")
            print("-2 Alcohol")
            print("+1 Molotov")
            show_inventory()
        elif crafting_input == 2 and inventory["Blade"] >= 1 and inventory["Tape"] >= 1:  # Crafting for Shiv
            inventory["Shiv"] += 1
            print("You Craft one Shiv")
            print("-1 Blade")
            print("-1 Tape")
            print("+1 Shiv")
            show_inventory()

        elif crafting_input == 3 and inventory["Tape"] >= 2 and inventory["Alcohol"] >= 1 and inventory["Blade"] >= 2:  # Crafting for Medkit
            inventory["Medkit"] += 1
            print("You Craft one Medkit")
            print("-2 Tape")
            print("-1 Alcohol")
            print("-2 Blades")
            print("+1 Medkits")
            show_inventory()

        elif crafting_input == 4 and inventory["Bottle"] >= 2 and inventory["Gun_powder"] >= 3:  # Crafting for Bullets
            inventory["Bullets"] += 3
            print("You Craft 3 Bullets")
            print("-2 Bottles")
            print("-3 Gun powder")
            print("+3 Bullets")
            show_inventory()
        elif crafting_input == 5:
            return

# This is the loot fuctions this can be acted apon every location
def loot(a):
    # Checks if the area has been looted before
    if looted[str(a)] == False:
        for index in range(2):
            item_pick = random.randint(1, 5)
            item_amount = random.randint(1, 3)
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
                inventory["Bottle"] += item_amount
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
    # time.sleep(a)
    return


def intro():
    global inventory
    global looted
    global combat
    global player_health
    global next_area
    global current_area
    global has_map
    global name
    #Reset all values
    inventory = {"Weapons": ["Gun"],
                 "Bullets": 10,
                 "Molotov": 0,
                 "Shiv": 0,
                 "Medkit": 0,
                 "Bottle": 0,
                 "Alcohol": 0,
                 "Blade": 0,
                 "Tape": 0,
                 "Gun_powder": 0

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

    #Holds current combat values
    combat = []
    player_health = 1000
    next_area = "00"
    current_area = "00"
    has_map = False
    print("Welcome to GAME NAME HERE")
    name = str(input("Please input a name\n:"))
    while True:
        try:
            confirm = int(input("1 To Confirm\n2 To Input a different name\n:"))
            if confirm == 1:
                break
            if confirm == 2:
                name = str(input("Please input a name\n:"))

        except ValueError:
            print("Please input a valid input")


    while True:
        try:
            print("Would you like more to know how to play?")
            more_info = int(input("1 to learn about movement\n2 to learn about combat\n3 to learn about crafting\n4 to leave"))
            if more_info == 1: #Learn about player movment
                print("This game has an area system")
                timer(1.5)
                print("You can only move in 2 dimension (Up, Down, left, Right)")
                timer(1.5)
                print("When not in combat you are able to move in these directions at any time")
                timer(1.5)
                print("When choseing a direction to move in you press")
                timer(1.5)
                print("W for forward (up)")
                timer(0.5)
                print("S for Backwards (Down)")
                timer(0.5)
                print("D for Right")
                timer(0.5)
                print("A for Left")
                timer(0.5)
                print("Have Fun :)")
            elif more_info == 2:#Learn about combat
                print("This game has combat")
                timer(1.5)
                print("When in combat you will be against a specific number of infected or scars")
                timer(1.5)
                print("Every turn you will be able to attack with a choice of 3 weapons")
                timer(1.5)
                print("Gun : Makes noise, low damage")
                timer(0.5)
                print("Molotov : Makes noise, high damage difficult to craft")
                timer(0.5)
                print("Shiv : Silence, instant kill can only use when in stealth")
                timer(0.5)
                print("As long as you stay silent you will not be attacked and this means you won't take damage")
                timer(1.5)
                print("One the enemy know your their you only get attacked by one at a time")
                timer(1.5)
                print("")
                timer(1.5)
                print("")



        except ValueError:
            print("Please input a valid input")


    print("Game Loading")
    timer(2)
    part_1()


def part_1():
    # Introduction
    print("Part 1 - The Tunnel")
    print()
    timer(2)
    print("Radio - Hey,", name, "You there?")
    timer(3.5)
    print(name, "- Yea im here?")
    timer(3.5)
    print(name, "- Why did Issac have me posted here?")
    timer(3.5)
    print("Radio - So you remeber when the scars took out our western base?")
    timer(3.5)
    print(name, "- Yes they took those people hostages")
    timer(3.5)
    print("Radio - Welllll, Issac had intell that the scars where keeping them hostage in these tunnels")
    timer(3.5)
    print(name, "- You're shitting me")
    timer(3.5)
    print(name, "- Aren't these the tunnels where all those hoards bloaters are traped?")
    timer(3.5)
    print("Radio - Yep")
    timer(3.5)
    print(name, "- And you sent me in, alone, with 10 bullets")
    timer(3.5)
    print("Radio - Its fine we just need you to scout for us")
    timer(3.5)
    print("Radio - Also we trap the bloaters on the other side of the system, there blocked off by the train's")
    timer(3.5)
    print(name, "- Im not going this im going back to the stadium")
    timer(3.5)
    print("Radio - If you come back you will be hung, Issac will not apreacheate you leaving your post")
    timer(3.5)
    print(name, "- Just to scout?")
    timer(3.5)
    print("Radio - Yes, just to scout")
    timer(3.5)
    print("Radio - Goodluck")
    while True:
        print("You can go forward into to tunnels(W) or look for loot(L)")
        player_action = str(input(":"))
        player_action = player_action.upper()
        if player_action == "W":
            area_1()
            break
        elif player_action == "L":
            print("Test")
            loot("00")
            looted["00"] = True
        else:
            print("Invalid input Please try again")

#Area(y value of the area, x value of the area, Area name, text a, text b,
def area_general(y,x,a,b,c):
    global next_area
    global has_map
    current_area = a
    current_location = [x,y]
    print(current_area)
    if has_map == True:
        map()


    print(b)
    print(c)
    #y = 11 , x = 3
    while True:

        if area_adjacent[y-1][x]:
            print("You see a tunnel forward(W)\n")

        if area_adjacent[y][x-1]:
            print("You see a tunnel to the Left(A)\n")

        if area_adjacent[y][x+1]:
            print("You see a tunnel to the Right(D)\n")

        if area_adjacent[y+1][x]:
            print("You can go backwards(S)\n")


        if has_map == False:
            print("You can look around(E)")

        if looted[current_area] == False:
            print("You can loot(L)")

        print("You can craft (Q)")

        player_action = str(input(":"))
        player_action = player_action.upper()  #10 , 3

        #Movment for the player
        if area_adjacent[y-1][x]:
            if player_action == "W":
                print("Forward")
                next_area = area_adjacent[y-1][x]
                return

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

        #You find the map
        if player_action == "E" and has_map == False:
            print("You look around")
            timer(2)
            print("You find a piece of paper")
            timer(1)
            print("Its a map of the tunnel system")
            map()
            timer(2)
            has_map = True
        #Loots
        elif player_action == "L":
            loot(current_area)
            looted[current_area] = True
        # This is for crafting
        elif player_action == "Q":
            crafting()
        else:
            print("Invalid input")

def combat_inf(a):   #COMBAT DISABLER
    print(a)
def combat_infe(a):  # Combat against INFECTED   MARKING ERROR AS I AM DISABLING COMBAT UNTILL FURTHER TESTING IS COMPLETE
    player_health_gain = 0
    global player_health
    visable = False

    for i in range(a):
        combat.append(INFECTED[random.randint(0, 2)])
        print(combat[i]["Name"])
    combat.append({"Name": "Place_Holder_Name", "Health": 999999999, "Attack": 0})

    while visable == False:
        # Choses Attack
        while True:
            print("You can attack with")
            print("1 : Gun *Noise(", inventory["Bullets"], "Bullets)")
            print("2 : Molotov *Noise(", inventory["Molotov"], "Molotovs)")
            print("3 : Shiv(", inventory["Shiv"], "Shivs)")
            print("4 : Medkit(", inventory["Medkit"], "Medkits)")

            try:
                attack = int(input(":"))

                if attack == 1 and inventory["Bullets"] > 0:  # Attack with gun
                    combat[0]["Health"] -= 4
                    visable = True
                    inventory["Bullets"] -= 1
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

                elif attack == 3 and inventory["Shiv"] > 0:  # Attack with shiv
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

                else:
                    print("You don't have any of that item >:(")
                #If you INFECTED has less than 0 health
                if combat[0]["Health"] <= 0:
                    timer(0.5)
                    print("You killed a", combat[0]["Name"])
                    combat.pop(0)

                #If you become visbale to the enemy they will attack
                if visable == True:
                    print("You get attacked by an", combat[0]["Name"])
                    print("You take", combat[0]["Attack"], "Damage")

                    player_health -= combat[0]["Attack"]

                    print("You have", player_health, "Health")

                #Death
                if player_health <= 0:
                    print("You die")
                    combat.pop(0)
                    timer(2)
                    while True:
                        try:
                            print("Would you like to try again\n1 To Try again\n2 To Exit\n")
                            try_again = int(input(":"))
                            if try_again == 1:
                                timer(1)
                                intro()
                            elif try_again == 2:
                                print("Thank you for playing")
                                exit(2)

                        except ValueError:
                            print("Please input a valid number")

                #Win
                if len(combat) == 1:
                    combat.pop(0)
                    print("You won")
                    timer(1)
                    return




            except ValueError:
                print("Input Error Please try again")
# Main
#Area(y value of the area, x value of the area, Area name, text a, text b)





def area_1():
    area_general(11, 3, "01", "You move forwards into the tunnels", "You don't see anything")
def area_2():
    area_general(10, 3, "02", "You find an opening, there seems to have bottles lying around", "Hear A noise Ahead")
def area_3(): #Has Combat
    combat_inf(1)

    #Progress in the story
    print(name,"- HEY THERE ARE INFECTED IN THE TUNNELS")
    timer(3.5)
    print("Radio - wh^#&@% @*HE CON#&@(T#ON I*# B@* @E C@9N'*# HE(*R Y)*")
    timer(3.5)
    print(name,"- fuck there isn't a connection")
    timer(3.5)
    print(name,"I need to find a way out of here")
    timer(3.5)
    area_general(9, 3, "03", "", "")


def area_4():
    area_general(9, 4, "04", "You See can far ahead of you", "You see the remains of dead infected")

def area_5():
    area_general(8, 4, "05", "You can still see far ahead of you ", "This causes you to feel very alone")

def area_6(): #Has Combat
    combat_inf(2)
    area_general(7, 4,"06", "The amount of infected causes you to feel worried", "You find a fire still smoking, people are nearby")

def area_7():
    area_general(6, 4, "07", "You see spore to the right of you", "You find a carving of a wooden statue resembling a woman with the words Feel Her love inscribed into the back ")

def area_8():
    area_general(5, 4, "08", "You hear a noise ahead, could it be the scars?", "")

def area_9(): #Has Combat
    combat_inf(2)
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
    combat_inf(3)
    print("----SPORES----")
    area_general(6, 6, "a9", "These tunnel are crawling with infected you need to figure out where the scars have taken the hosteges", "And get the hell out of here")

def area_a10():
    print("----SPORES----")
    area_general(6, 7, "a10", "", "")

def area_a11():
    print("----SPORES----")
    area_general(5, 7, "a11", "Even more noise ahead expect infected as you are still inside spores", "")

def area_a12(): #Has Combat
    combat_inf(2)
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
    combat_inf(2)
    area_general(2, 7, "b14", "You find a key? I wonder what it is for?", "")
    area_adjacent[2][4] = "11"

#C Area's
def area_c11():
    area_general(3, 3, "c11", "", "")

def area_c12():
    area_general(3, 2, "c12", "", "")

def area_c13():
    area_general(4, 2, "c13", "", "")

def area_c14(): #Has Combat
    combat_inf(2)
    area_general(3, 1, "c14", "One of the infected had a crowbar on them", "What could this help open")
    area_adjacent[3][5] = "b11"



intro()
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















