class ROOM:

    def __init__(self, description, west, east, south, north):
        self.description = description
        self.west = west
        self.east = east
        self.south = south
        self.north = north


def main():
    room_list = []

    # 0
    room = ROOM("You are in the entry way.\nThere is a door to the north.", None, None, "q", 1)
    room_list.append(room)

    # 1
    room = ROOM("You are in the south hall.\nThere are doors to the north, east, south, and west. ",
                4, 7, 0, 2)
    room_list.append(room)

    # 2
    room = ROOM("You are in the north hall.\nThere are doors to the north, east, south, and west.",
                5, 8, 1, 3)
    room_list.append(room)

    # 3
    room = ROOM("You are on the outside balcony in the Center.\nThere is more of the  balcony to the east "
                "and west, as well as a door to the south", 6, 9, 2, 10)
    room_list.append(room)

    # 4
    room = ROOM("You are in bedroom 1.\nThere are doors to the north and east."
                , None, 1, None, 5)
    room_list.append(room)

    # 5
    room = ROOM("You are in bedroom 2.\nThere are doors to the north, east, and south.", None, 2, 4, 6)
    room_list.append(room)

    # 6
    room = ROOM("You are on the outside balcony to the west.\nThere is more of the balcony east and a door south.",
                None, 3, 5, 10)
    room_list.append(room)

    # 7
    room = ROOM("You are in the dining room.\nThere are doors to the west and north.", 1, None, None, 8)
    room_list.append(room)

    # 8
    room = ROOM("You are in the kitchen.\nThere are doors to the south, west, and north.", 2, None, 7, 9)
    room_list.append(room)

    # 9
    room = ROOM("You are on the outside balcony on the east side.\nThere is more of the balcony west and a door south",
                3, None, 8, 10)
    room_list.append(room)

    # 10
    room = ROOM("You have fallen of the cliff and are now dead.", None, None, None, None)
    room_list.append(room)

    current_room = 0

    done = False

    while not done:
        if current_room == 10:
            print("You have fallen of the cliff and are now dead.")
            done = True

        else:
            print("  ")
            print(room_list[current_room].description)
            print("Where would you like to go? ")
            user_choice = input()

            # North
            if user_choice.lower() == "north":
                next_room = room_list[current_room].north
                if next_room == None:
                    print("You can't go that way.")
                else:
                    current_room = next_room

            # South
            elif user_choice.lower() == "south":
                next_room = room_list[current_room].south
                if next_room == None:
                    print("You can't go that way.")
                elif next_room == "q":
                    print("You have left the house. Goodbye")
                    done = True
                else:
                    current_room = next_room

            # West
            elif user_choice.lower() == "west":
                next_room = room_list[current_room].west
                if next_room == None:
                    print("You can't go that way.")
                else:
                    current_room = next_room

            # East
            elif user_choice.lower() == "east":
                next_room = room_list[current_room].east
                if next_room == None:
                    print("You can't go that way.")
                else:
                    current_room = next_room

            elif user_choice.lower() == "q":
                print("You have left the house. Goodbye")
                done = True

            # Not a command
            else:
                print("I don't under stand that. Do you want to go north, east, south, or west?")
                print("Or if you like to  quit type q.")


main()
