number = int(input("Enter an integer: "))

prime = True

if number < 2:
    prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break

if prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")