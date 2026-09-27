
from item import Item
from room import Room
from player import Player


def start_game():
    print("The game has started! ")


def explore(player):
    print("\nYou are currently in:", player.location.name)

    if player.location.item is not None:
        print("There is an item here:", player.location.item.name)
    else:
        print("There are no more items here.")


name = input("Write your beautiful name: ")
age = int(input("Enter your age: "))


print("\nName:",name)
print("Age:",age)

if age < 12:
    print("You are a minor. The program will now shut down. ")
else:
    print("Welcome to the game!")


    #Items
    sword = Item("Sword", 5)
    knife = Item("Knife", 1)
    water_bucket = Item("Water bucket", 2)

    #Rooms
    kitchen = Room("Kitchen", knife)
    bedroom = Room("Bedroom", sword)
    well = Room("Well", water_bucket)

    #Player
    player = Player(name, kitchen)


    while True:
        print("\n--- MAIN MENU ---")
        print("1. start")
        print("2. explore")
        print("3. collect item")
        print("4. inventory")
        print("5. end")

        command = input("Enter command: ")

        if command == "1":
            start_game()

        elif command == "2":
            explore(player)

        elif command == "3":
            player.collect_item()

        elif command == "4":
            player.show_inventory()

        elif command == "5":
            print("Goodbye!")
            break

        else:
            print("Unknown command.")

