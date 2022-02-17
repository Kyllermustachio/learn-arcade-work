import random


def main(user_choice=None):
    # Intro
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    # Variables
    camel_tiredness = 0
    thirst = 0
    miles_traveled = 0
    natives_distance = -20
    number_of_drinks = 3


    done = False

    while not done:
        are_natives_close = miles_traveled - natives_distance
        # Options
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")

        # Players input
        user_choice = input("What is your choice? ")

        # Quit
        if user_choice.upper() == 'Q':
            print("Game Over")
            done = True

        # Check status
        elif user_choice.upper() == 'E':
            print("Miles traveled: ", miles_traveled)
            print("Drinks in canteen: ", number_of_drinks)
            print("The natives are", are_natives_close, "miles behind you.")

        # Stop for the night
        elif user_choice.upper() == 'D':
            camel_tiredness = 0
            print("Camel is happy.")
            # random.randint is an inclusive range while random.randrange is not inclusive
            natives_distance += random.randint(7, 14)

        # Full speed ahead
        elif user_choice.upper() == 'C':
            miles_traveled += random.randint(10, 20)
            print("You have traveled ", miles_traveled, "miles.")
            natives_distance += random.randint(7, 14)
            thirst += 1
            camel_tiredness += random.randint(1, 3)
            # oasis chance
            oasis_chance = random.randrange(0, 21)
            if oasis_chance == 20:
                camel_tiredness = 0
                thirst = 0
                number_of_drinks = 3
                print("You found an oasis!!!!")

        # Moderate speed ahead
        elif user_choice.upper() == 'B':
            miles_traveled += random.randint(5, 12)
            print("You have traveled ", miles_traveled, "miles.")
            natives_distance += random.randint(7, 14)
            thirst += 1
            camel_tiredness += 1
            # oasis chance
            oasis_chance = random.randrange(0, 21)
            if oasis_chance == 20:
                camel_tiredness = 0
                thirst = 0
                number_of_drinks = 3
                print("You found an oasis!!!!")

        # Player goes to drink water
        elif user_choice.upper() == 'A':
            # Does the player have water
            if number_of_drinks > 0:
                number_of_drinks -= 1
                thirst = 0
                print("You feel hydrated")
            # Player doesn't have water
            else:
                print("Error you are out of water")

        # Is the player going to die of thirst
        if thirst > 6:
            print("You died of thirst!")
            done = True

        # Is the player thirsty
        elif thirst > 4:
            print("You are thirsty")

        # Is the camel dead tired ;)
        if camel_tiredness > 8:
            print("Your camel is dead!")
            done = True

        # Is the camel tired
        elif camel_tiredness > 5:
            print("Your camel is tired")

        #  Have the natives caught the player
        if are_natives_close <= 0:
            print("The natives caught you and you are screwed.")
            done = True

        # Are natives close
        elif are_natives_close < 15:
            print("The natives are getting close")

        # Victory!!!!
        if miles_traveled >= 200:
            print("YOU WIN!!!!!")
            print("You made it across the desert.")
            done = True


main()
