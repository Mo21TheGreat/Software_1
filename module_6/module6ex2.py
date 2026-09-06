numbers = []

while True:
    num = input("Enter a number: ")

    if num == "":
        break

    numbers.append(int(num))

numbers.sort(reverse=True)

print("The greatest numbers in descending order: ")

for number in numbers[:5]:
    print(f"{number:.1f}")