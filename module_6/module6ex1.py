import random

dice_roll = int(input("How many dice to roll: "))
total = 0

for i in range(dice_roll):
    total += random.randint(1, 6)

print(f"Sum of the dice: {total}")