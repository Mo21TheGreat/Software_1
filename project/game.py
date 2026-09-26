items = []

def start_game():
    print("The game has started! ")


def explore():
    print("You explore the map! ")

def inventory():
    item = input("Enter an item: ")
    items.append(item)
    

    print("Your inventory: ")
    for item in items:
        print(item)



name = input("Write your beautiful name: ")
age = int(input("Enter your age: "))


print("\nName:",name)
print("Age:",age)

if age < 12:
    print("You are a minor. The program will now shut down. ")
else:
    print("Welcome to the game!")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. start")
        print("2. explore")
        print("3. inventory")
        print("4. end")

        command = input("Enter command: ")

        if command == "1":
            start_game()

        elif command == "2":
            explore()

        elif command == "3":
            inventory()

        elif command == "4":
            print("Goodbye!")
            break

        else:
            print("Unknown command.")

