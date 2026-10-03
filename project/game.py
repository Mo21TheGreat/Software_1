
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

def show_intro():
    with open("intro.txt", "r") as file:
        text = file.read()
        print(text)


def show_instructions():
    with open("instructions.txt", "r") as file:
        text = file.read()
        print(text)

def save_game(player):
    with open("save.txt", "w") as file:
        file.write(player.name + "\n")
        file.write(player.location.name + "\n")

        for item in player.items:
            file.write(item.name + "\n")

    print("Game saved!")



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
        print("3. move")
        print("4. collect item")
        print("5. inventory")
        print("6. save game")
        print("7. end")

        command = input("Enter command: ")

        if command == "1":
            start_game()

        elif command == "2":
            explore(player)

        elif command == "3":
            print("\nWhere do you want to go?")
            print("1. Kitchen")
            print("2. Bedroom")
            print("3. Well")
             
            destination = input("Choose room: ")
            if destination == "1":
                player.move(kitchen)
            elif destination == "2":
                player.move(bedroom)
            elif destination == "3":
                player.move(well)
            else:
                print("Unknown room.")
        
        elif command == "4":
            player.collect_item()

        elif command == "5":
            player.show_inventory()

        elif command == "6":
            save_game(player)

        elif command == "7":
            print("Goodbye!")
            break

        else:
            print("Unknown command.")

