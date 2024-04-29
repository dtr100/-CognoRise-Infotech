import random

def roll_dice(num_rolls, num_sides):
    print(f"Rolling {num_rolls} {num_sides}-sided dice:")
    for roll in range(1, num_rolls + 1):
        result = random.randint(1, num_sides)
        print(f"Roll {roll}: {result}")
    print("Done rolling!")

def main():
    print("Welcome to the Dice Rolling Simulator")
    while True:
        try:
            num_sides = int(input("Enter the number of sides on the dice: "))
            if num_sides <= 0:
                raise ValueError
            num_rolls = int(input("Enter the number of rolls: "))
            if num_rolls <= 0:
                raise ValueError
            roll_dice(num_rolls, num_sides)
            break
        except ValueError:
            print("Please enter a positive integer.")

if __name__ == "__main__":
    main()
