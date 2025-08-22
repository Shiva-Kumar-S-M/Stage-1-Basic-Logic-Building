import random

# 🎲 Dice Rolling Simulator

# Randomly simulate rolling a dice.
def roll_dice():
    return random.randint(1, 6)

if __name__ == "__main__":
    while True:
        input("Press Enter to roll the dice or type 'q' to quit: ")
        result = roll_dice()
        print(f"You rolled a {result}")
        if input("Roll again? (y/n): ").lower() != 'y':
            break

# End of the dice rolling simulator
# This simple program allows users to roll a dice by pressing Enter and displays the result.
# It continues to prompt the user until they choose to quit by entering 'q'.
# The random module is used to generate a random integer between 1 and 6, simulating a dice roll.       