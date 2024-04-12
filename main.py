import random
import time

player_bike = []
bike_name = []
enemy_bike = []
level_engine = 1
level = 1
motorb = 0
tank_size = 1
track = 1
player_money = 0
player_name = "Nine of Hearts"
user_input = 0


def restart():
    print()
    print("-Really cool music starts playing-")
    print()
    print("""Welcome to the Te Papa exhibition "The Wonderful World of Words". """)
    print("Please use full screen to maximize the enjoyablility of this experance")
    starting()

    import random


import time

player_bike = []
bike_name = []
enemy_bike = []
level_engine = 1
level = 1
motorb = 0
tank_size = 1
track = 1


def random_race():  # This is a function that acts like a teleporter to display the next lines of code
    global player_bike

    if motorb == 1:
        player_bike = [{"Name": "Ducati Panigale V4,", "Top speed": "310", "Engine": level_engine,
                        "Health": 30,
                        "Ability": ["High rpm", random.randint(6, 10), "Aerodynamic", random.randint(5, 14)]}]
    if motorb == 2:
        player_bike = [{"Name": "BMW S1000RR,", "Top speed": "295", "Engine": level_engine,
                        "Health": 45,
                        "Ability": ["High beam", random.randint(8, 14), "Flame exaust", random.randint(7, 16)]}]
    if motorb == 3:
        player_bike = [{"Name": "Kawasaki Ninja H2R,", "Top speed": "325", "Engine": level_engine,
                        "Health": 20,
                        "Ability": ["Low suspention", random.randint(2, 11), "Flame exaust", random.randint(3, 13)]}]

    # enemy pokemon
    enemy_bike = [
        {"Name": "Yamaha R1", "Top speed": "280", "Engine": random.randint(1, 2),
         "Health": random.randint(20, 30),
         "Ability": ["Stealth mirrors", random.randint(3, 6), "Burnout", random.randint(8, 16)]},
        # Motorbike 1 (index 0, this is a list of the diferent motorbikes and what their stats are to describe what they do in battle).
        {"Name": "Hayabusa", "Top speed": "305", "Engine": random.randint(1, 2),
         "Health": random.randint(15, 35),

         "Ability": ["140 in first gear", random.randint(3, 10), "Strait piped", random.randint(1, 20)]},
        # Motorbike 2 (Index 1)
        {"Name": "Aprilia RSV 1000R", "Top speed": "315", "Engine": random.randint(1, 2),
         "Health": random.randint(4, 12),
         "Ability": ["Stretched", random.randint(1, 15), "Dual pipes", random.randint(10, 14)]}  # Motorbike 3 (index 2)
    ]

    x = random.randint(0, 2)
    bike = enemy_bike[x]
    player_motorbike = player_bike[0]
    player_motorbike_health = player_bike[0]["Health"]
    enemy_health = bike["Health"]

    print("A", bike["Name"], "has challaged you to a race")
    print("It's has a top speed of", bike["Top speed"], "Km/h")
    print("Level engine:", bike["Engine"])
    print("It has", bike["Health"], "fuel")

    while True:
        print("Press R to race or B to ruturn to garage")
        player_choice = input(":").upper()  # User inputs a letter and program responds
        print(player_choice)

        if player_choice == "R":
            print("You choose to race with:", player_motorbike["Name"])
            break
        elif player_choice == "B":
            garage()
            return
        else:
            print("Input error")

    print(player_motorbike["Name"], "has", player_motorbike["Health"], "fuel")

    while enemy_health > 0 and player_motorbike_health > 0:
        enemy_attack_randomiser = random.randrange(0, 3, 2)

        print(bike["Name"], "to use ability", bike["Ability"][enemy_attack_randomiser],
              "for", bike["Ability"][enemy_attack_randomiser + 1], "damage")
        player_motorbike_health -= bike["Ability"][enemy_attack_randomiser + 1]
        print(player_motorbike["Name"], "has", player_motorbike_health, "fuel")
        if player_motorbike_health > 0:
            print("Press 1 for", player_motorbike["Name"], "to use ability",
                  player_motorbike["Ability"][0], "or 2 to use ability",
                  player_motorbike["Ability"][2])
            attack_choice = int(input())

            if attack_choice == 1:
                player_attack = player_motorbike["Ability"][1]
                print(player_motorbike["Name"], "to use ability", player_motorbike["Ability"][0],
                      "for", player_attack)
                enemy_health -= player_attack
                print("Enemy fuel is", enemy_health)
            elif attack_choice == 2:
                player_attack = player_motorbike["Ability"][3]
                print(player_motorbike["Name"], "to use ability", player_motorbike["Ability"][2],
                      "for", player_attack)
                enemy_health -= player_attack
                print("Enemy fuel is", enemy_health)

    if player_motorbike_health > 0:
        print()
        print("You Win")
        print()
        global track
        global player_money
        player_money = player_money + 3000
        track = track + 1
        if track == 10:
            print()
            print("Congrats, you have compleated the game!")
            print()
        print("Going to garage...")
        garage()

        return

    else:
        print("You lost the race ):")
        print("going back to garage...")
        garage()


def mod_shop():  # function for the modshop
    global player_money
    global level_engine
    global tank_size
    while True:
        print()
        print()
        print("Welcome to the Motorbike Mod shop.")
        print("You currently have", player_money)
        if player_money == 0:
            print("'You currently dont have any money, win some races to gain mony to buy upgrades.")
            print("Come back when you have money")
            print()
            print("Press W to return to you Garage")
            while True:
                user_input = input(":").upper()

                if user_input == "W":
                    garage()
                    break
                else:
                    print("Input Error")

        print("What we sell:")
        print(" 1. Engines ( Speed )")
        print(" 2. fuel tanks ( Fuel )")
        print(" Or press 3 to return to the garage.")
        print()
        print("Which part of the Mod shop would you like to show? ( 1, 2 or 3 )")
        try:
            user_input = int(input(":"))
            if user_input == 1:
                print()
                print("Enine sizes:")
                print("Level 1 engine +0 ( equipped )")
                print("Level 2 engine +50 ( $10,000 )")
                print()
                if player_money <= 10000:
                    print("You currently dont have enough money for this upgrade")
                    print("returning you to shop")
                    mod_shop()
                    break
                if player_money >= 10000:
                    print("Would you like to buy Level 2 engine?")
                    while True:
                        print("Press 1 to continue or 2 to quit.")

                        try:
                            user_input = int(input(":"))
                            if user_input == 1:
                                print()
                                print("You bike now has a Level 2 engine")
                                player_money = player_money - 10000
                                print("You now have $", player_money)
                                level_engine = 2
                                print()
                                mod_shop()
                                break

                            elif user_input == 2:
                                print("Returning back to shop")
                                mod_shop()
                            else:
                                print("input error please press 1 or 2")

                        except ValueError:
                            print("input error please press 1 or 2")

                break

            if user_input == 2:
                print()
                print("Fuel tak sizes:")
                print("Stock tank +0L( equipped )")
                print("Overdrive tank +10L ( $5,000 )")
                print()
                if player_money <= 5000:
                    print("You currently dont have enough money for this upgrade")
                    print("returning you to shop")
                    mod_shop()
                    break
                if player_money >= 5000:
                    print("Would you like to buy Overdrvetank for $5,000?")
                    while True:
                        print("Press 1 to continue or 2 to quit.")

                        try:
                            user_input = int(input(":"))
                            if user_input == 1:
                                print()
                                print("You bike now has a Level 2 engine")
                                player_money = player_money - 5000
                                tank_size = 2
                                print("You now have $", player_money)
                                print()
                                mod_shop()
                                break

                            elif user_input == 2:
                                print("Returning back to shop")
                                mod_shop()
                            else:
                                print("input error please press 1 or 2")

                        except ValueError:
                            print("input error please press 1,2 or 3")
                break

            elif user_input == 3:
                print("Going to garage...")
                garage()
                break

            else:
                print("input error please press 1,2 or 3")
        except ValueError:
            print("input error please press 1,2 or 3")


def motorbike_track1():  # function
    print()
    print()
    print("Welcome to the Lake side Motorbike race track")
    print(" You will be racing a Random bike")
    print("Possible compeditors:")
    print("Yamaha R1, Hayabusa, Aprilia RSV 1000R")
    print("Good luck!")
    random_race()


def motorbike_track2():  # function
    print()
    print()
    print("Welcome to the Underground Motorbike race track")
    print(" You will be racing a Random bike")
    print("Good luck!")
    random_race()


def motorbike_track3():  # function
    print()
    print()
    print("Welcome to the Parking lot Motorbike race track")
    print(" You will be racing another Random bike....")
    print("Good luck!")
    random_race()


def motorbike_track4():
    print()
    print()
    print("Welcome to the Airport Motorbike race track")
    print(" You will be racing a random bike")
    print("Good luck!")
    random_race()


def motorbike_track5():
    print()
    print()
    print("Welcome to the Mountain Motorbike race track")
    print(" You will be racing a random racer")
    print("Good luck with the race!")
    random_race()


def motorbike_track6():
    print()
    print()
    print("Welcome to the City streets Motorbike race track")
    print(" You will be racing a random racer")
    print("Good luck with the race!")
    random_race()


def motorbike_track7():
    print()
    print()
    print("Welcome to the Loop Motorbike race track")
    print(" You will be racing a random racer")
    print("Good luck with the race!")
    random_race()


def motorbike_track8():
    print()
    print()
    print("Welcome to the Downhill Motorbike race track")
    print(" You will be racing a random racer")
    print("Good luck with the race!")
    random_race()


def motorbike_track9():
    print()
    print()
    print("Welcome to the Midnight Motorbike race track")
    print(" You will be racing a random racer")
    print("Good luck with the race!")
    random_race()


def motorbike_track10():
    print()
    print()
    print("Welcome to the Motorbike Drage strip")
    print()
    print("THIS IS THE LAST RACE")
    print(" You will be racing another random race ( suprise, suprise..)")
    print("Good luck with the race!")
    random_race()


# _________________________________________________________________________________________________________________________________________________________________________________________________________( This is a bookmark )_____
def garage():
    while True:

        print()
        print("-----Area 01 - Garage-----")
        print()
        print("You are in your Motorbike garage, this is your starting point of your career and storyline.")
        print(
            "You can choose to leave to go to the motorbike track to race other motorbikes or you can choose to go to the motorbike modification shop.")
        print("You can head Left to go to the motorbike shop by pressing A")
        print(
            "Or you can go Right to go to a motorbike track by pressing D ( Everytime you win a race you will go to a new track )")
        print("Press R to restart the game")
        print("There are 10 race tracks in total")
        print("Current motorbike track:", track)  # Varable

        user_input = input(":").upper()

        if user_input == "A":
            mod_shop()
            break

        if user_input == "R":  # if statements which only work "if" the input matches
            restart()
            break

        elif user_input == "D":
            if track == 1:
                motorbike_track1()

            if track == 2:
                motorbike_track2()

            if track == 3:
                motorbike_track3()

            if track == 4:
                motorbike_track4()

            if track == 5:
                motorbike_track5()
            break

        elif user_input == "A" or user_input == "D":
            print("You can't go that way!")
        else:
            print("Input Error")


def choose_bike():
    while True:
        global player_bike
        player_bike = 0
        bike_name = 0
        print(" ")
        print("Please choose your first motorbike to begin with: ( 1, 2 or 3 ).")
        print(" ")
        print(".___________________________________________________________________")
        print("|  No. | Name:                     Speed ( Km/h ) |  Fuel ( Liters ) | Abilitys:              ")
        print("|___________________________________________________________________")
        print("|   1.  | Ducati Panigale V4  |      310       |          30      | High rpm, Aerodynamic  ")
        print("|   2.  | BMW S1000RR       |      295       |          45      | High beam, Flame exaust")
        print("|   3.  | Kawasaki Ninja H2R |      325       |          20      | Low suspention, Turbo  ")

        try:
            user_input = int(input(":"))
            if user_input == 1:
                player_bike = [{"Name": "Ducati Panigale V4,", "Top speed": "310", "Engine": level_engine,
                                "Health": 30,
                                "Ability": ["High rpm", random.randint(6, 10), "Aerodynamic", random.randint(5, 14)]}]
                print()
                print("You selected", player_bike)
                motorb = 1
                garage()
                break

            if user_input == 2:
                player_bike = [{"Name": "BMW S1000RR,", "Top speed": "295", "Engine": level_engine,
                                "Health": 45,
                                "Ability": ["High beam", random.randint(8, 14), "Flame exaust", random.randint(7, 16)]}]
                print()
                print("You selected", player_bike)
                motorb = 2
                garage()
                break

            elif user_input == 3:
                player_bike = [{"Name": "Kawasaki Ninja H2R,", "Top speed": "325", "Engine": level_engine,
                                "Health": 20, "Ability": ["Low suspention", random.randint(2, 11), "Flame exaust",
                                                          random.randint(3, 13)]}]  # list that helps find varables
                print()
                print("You selected", player_bike)
                motorb = 3
                garage()
                break

            else:
                print("input error please press 1,2 or 3")

        except ValueError:
            print("input error please press 1,2 or 3")


def starting():
    print(" ")
    print("Please enter your name.")
    player_name = input(":")

    while True:
        print("Hi", player_name, "Press 1 to continue or 2 to quit.")

        try:
            user_input = int(input(":"))
            if user_input == 1:
                print(" ")
                print("- Welcome to Motorbike Trackday -")
                print(" ")
                print("How to play:")
                print(" ")
                print("Press W,S,A,D to move in that Direction.")
                choose_bike()
                break

            elif user_input == 2:
                print("Thanks for playing")
                exit(2)
            else:
                print("input error please press 1 or 2")

        except ValueError:
            print("input error please press 1 or 2")


restart()  # This function sends it back to the top where the code starts off
