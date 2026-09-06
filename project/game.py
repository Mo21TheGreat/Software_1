name = input("Write your beautiful name: ")
age = int(input("Enter your age: "))

if age < 12:
    print("You are a minor. The program will now shut down. ")
else:
    print("Welcome to the game!")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. start")
        print("2. explore")
        print("3. inventory")
        print("4. lopeta")

        command = input("Enter command: ")

        if command == "start":
            print("The game has started!")

        elif command == "explore":
            print("You explore the mysterious forest.")

        elif command == "inventory":
            print("Your inventory is empty.")

        elif command == "lopeta":
            print("Goodbye!")
            break

        else:
            print("Unknown command.")

print("Name:",name)
print("Age:",age)
