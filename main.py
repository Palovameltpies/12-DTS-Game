import time
import random

global current_area

# Player Inventory
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

player_health = 10

current_area = "00"
area_adjacent  = [[False,False,False,"12",False,False,False], #0
                  [False,False,False,"11",False,False,"b14"], #1
                  ["c14","c12","c11","10","b11","b12","b13"], #2
                  [False,"c13",False,"09",False,False,"a12"], #3
                  [False,False,False,"08",False,False,"a11"], #4
                  [False,False,False,"07","a8","a9","a10"], #5
                  [False,False,False,"06",False,False,False], #6
                  [False,False,False,"05",False,False,False], #7
                  [False,False,"03","04",False,False,False], #8
                  [False,False,"02",False,False,False,False], #9
                  [False,False,"01",False,False,False,False]] #10
# You can only every look each area once, this information will be used in the function loot
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

has_map = False
def show_inventory():
    print("-----Inventory-----")
    for i in range(len(inventory["Weapons"])):
        print(inventory["Weapons"][i])
    print(inventory["Bullets"], ": Bullets")
    print(inventory["Molotov"], ": Bullets")
    print(inventory["Shiv"], ": Bullets")
    print(inventory["Medkit"], ": Bullets")

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
    print("-------------------------------------")


# Timer function, this shortens the amount of code needed when trying to run time.sleep
def timer(a):
    print("...")
    # time.sleep(a)
    return


def intro():
    global name
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
    global has_map
    current_area = a     #5     #5
    current_location = [(y-1),(x-1)]
    if has_map == True:
        map()
    print(current_location)
    print("Up",area_adjacent[current_location[0] - 1][x])
    print("Left",area_adjacent[current_location[1] + 1][y])
    print("Down", area_adjacent[current_location[0] + 1][x])
    print("Right", area_adjacent[current_location[1] - 1][y])
    print(b)
    print(c)
    while True:
        if area_adjacent[current_location[0] - 1][x]:
            print("you can move forward")
        if area_adjacent[current_location[1] + 1][y]:
            print("You can move Left")
        if area_adjacent[current_location[0] + 1][x]:
            print("You can move Down")
        if area_adjacent[current_location[1] - 1][y]:
            print("You can move right")
        player_action = str(input(":"))
        player_action = player_action.upper()  #10 , 3
        if area_adjacent[current_location[0] - 1]:
            if player_action == "W":
                print("Forward")
        if area_adjacent[current_location[1] + 1]:
            if player_action == "A":
                print("Left")
        if area_adjacent[current_location[0] + 1]:
            if player_action == "S":
                print("Down")
        if area_adjacent[current_location[1] - 1]:
            if player_action == "D":
                print("Right")

        elif player_action == "E" and has_map == False:
            print("You look around")
            timer(2)
            print("You find a piece of paper")
            timer(1)
            print("Its a map of the tunnel system")
            map()
            timer(2)
            has_map = True
        elif player_action == "L":
            loot(current_area)
            looted[current_area] = True

        else:
            print("Invalid input")


#def area_2():
    #global has_map
    #current_area = "02"
    #if has_map == True:
    #    map()
    #
    #print("You moved even further into the tunnels")
    #print("You find plastic water bottles and clean clothes")
    #timer(1)
    #print("You hear a noise up ahead")
    #print("You can move forwards(W) *Noise ahead, you can move back(S) or loot(L)")
    #while True:
     #   player_action = str(input(":"))
     #   player_action = player_action.upper()
    #    if player_action == "W":
     #       area_3()
     #       break
     #   elif player_action == "S":
     #       area_1()
     #       break
     #   elif player_action == "L":
      #      loot("02")
      #      looted["02"] = True
#
      #      # Adds addtional items
      #      print("You find 2 more bottles")
      ##      print("You find 1 more Tape")
       #     inventory["Bottles"] += 2
     #       inventory["Tape"] += 1
      # else:
       #     print("Invaild input")


# Main
#Area(y value of the area, x value of the area, Area name, text a, text b,
area_general(6,6,"a9","Hello","Hello")













