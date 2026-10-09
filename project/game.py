from pathlib import Path
from item import Item
from room import Room
from player import Player


def start_game():
    print("The game has started!")
    show_intro()


def explore(player):
    print("\nYou are currently in:", player.location.name)

    if player.location.item is not None:
        print("There is an item here:", player.location.item.name)
    else:
        print("There are no more items here.")

def show_intro():
    file_path = Path(__file__).parent / "intro.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        print(text)


def show_instructions():
    file_path = Path(__file__).parent / "instructions.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        print(text)

def save_game(player):
    file_path = Path(__file__).parent / "save.txt"

    with open(file_path, "w", encoding = "utf-8") as file:
        file.write(player.name + "\n")
        file.write(player.location.name + "\n")

        for item in player.items:
            file.write(item.name + "\n")

    print("Game saved!")

def load_game(player, rooms, items):
    file_path = Path(__file__).parent / "save.txt"

    if not file_path.exists():
        print("No saved game found! ")
        return

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    if len(lines) < 2:
        print("Save file is incomplete!")
        return

    player.name = lines[0]
    room_name = lines[1]

    for room in rooms:
        if room.name == room_name:
            player.location = room
            break

    player.items = []

    for item_name in lines[2:]:
        for item in items:
            if item.name == item_name:
                player.items.append(item)
                break

    for room in rooms:
        if room.item is not None:
            for item in player.items:
                if room.item.name == item.name:
                    room.item = None

    print("Game loaded successfully!")


name = input("Enter your beautiful name: ")
age = int(input("Enter your age: "))


print("\nName:",name)
print("Age:",age)

if age < 12:
    print("You are a minor. The program will now shut down. ")
    ##########
else:
    print("Welcome to Escape!")


    #Items
    flashlight = Item("Flashlight", 2)
    fork = Item("Fork", 0.5)
    remote = Item("Remote", 0.8)
    razor = Item("Razor", 0.4)
    escape_key = Item("ESCAPE KEY", 0.2)
    

    #Rooms
    kitchen = Room("Kitchen", fork)
    bedroom = Room("Bedroom", flashlight)
    living_room = Room("Living Room", remote)
    front_yard = Room("Front yard")
    bathroom = Room("Bathroom", razor)
    laundry = Room("Laundry", escape_key)

    #Player
    player = Player(name, living_room)

    
    rooms = [kitchen, bedroom, living_room, front_yard, bathroom, laundry]
    
    items = [flashlight, fork, remote, razor, escape_key]


    while True:
        
        player.show_menu_inventory()


        print("\n----- MAIN MENU -----")
        print("1. Start")
        print("2. Explore")
        print("3. Move")
        print("4. Collect item")
        print("5. Instructions")
        print("6. Save game")
        print("7. Load game")
        print("8. End")

        command = input("Enter command: ")

        if command == "1":
            start_game()

        elif command == "2":
            explore(player)

        elif command == "3":
            print("\nWhere do you want to go?")
            print("1. Kitchen")
            print("2. Bedroom")
            print("3. Living room")
            print("4. Bathroom")
            print("5. Front yard")
            print("6. Laundry")
             
            destination = input("Choose room: ")
            if destination == "1":
                player.move(kitchen)
            elif destination == "2":
                player.move(bedroom)
            elif destination == "3":
                player.move(living_room)
            elif destination == "4":
                player.move(bathroom)
            elif destination == "5":
                has_key = False

                for item in player.items:
                    if item.name == "ESCAPE KEY":
                        has_key = True

                if has_key:
                    player.move(front_yard)
                    print("\nYou unlocked the door!")
                    print("You escaped!")
                    print("Congrats, YOU WON!")
                    break
                else:
                    print("The front yard is locked. You need the ESCAPE KEY!")
            
            elif destination == "6":
                has_flashlight = False

                for item in player.items:
                    if item.name == "Flashlight":
                        has_flashlight = True

                if has_flashlight:
                    player.move(laundry)
                    print("You used your flashlight to enter the dark laundry!")
                else:
                    print("The laundry room is too dark! You cannot enter without the flashlight!")
            else:
                print("Unknown room.")
        
        elif command == "4":
            player.collect_item()

        elif command == "5":
            show_instructions()

        elif command == "6":
            save_game(player)

        elif command == "7":
            load_game(player, rooms, items)

        elif command == "8":
            print("Goodbye!")
            break

        else:
            print("Unknown command.")

