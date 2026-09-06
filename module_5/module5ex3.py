number = float(input("Enter a number (or press Enter to quit): "))

smallest = number
largest = number

while True:
    text = input("Enter a number (or press Enter to quit): ")

    if text == "":
        break

    number = float(text)

    if number < smallest:
        smallest = number

    if number > largest:
        largest = number

print(f"Smallest number: {smallest}")
print(f"Largest number: {largest}")
