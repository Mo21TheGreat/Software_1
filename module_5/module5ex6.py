import random

n = int(input("How many random points: "))

inside = 0
count = 0

while count < n:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        inside += 1

    count += 1

pi = 4 * inside / n

print(f"Approximation of pi: {pi}")