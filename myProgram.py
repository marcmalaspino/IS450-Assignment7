#Trick or Treat Game - myProgram.py

import random

#Lists of Tricks and Treats
treats = ["chocolate bar", "sour candy", "gummy worm", "candy corn", "peanut butter cup"]
tricks = ["rock", "tube of toothpaste", "ketchup packet", "box of paperclips", "hot glue stick"]

#Dictionary to store collected tricks and treats, tied to counts of each
bag = {}

#Running totals of tricks and treats
total_treats = 0
total_tricks = 0

while True:
    choice = input("\nWould you like to knock on the door? (y/n)\n").strip().lower()

    if choice == 'y':
        if random.choice(["trick", "treat"]) == "treat":
            item = random.choice(treats)
            total_treats += 1
            bag[item] = bag.get(item, 0) + 1
            print(f"Treat! You got a {item}.")
        else:
            item = random.choice(tricks)
            total_tricks += 1
            bag[item] = bag.get(item, 0) + 1
            print(f"Uh oh! Trick! You got a {item}.")

    elif choice == 'n':
        if bag:
            print("\nThanks for playing! Here's what's in your bag:")
            for item, count in bag.items():
                print(f" {item}: {count}")
            print(f"Total Treats: {total_treats}")
            print(f"Total Tricks: {total_tricks}")
            break
        else:
            print("\nThanks for playing! Your bag is empty")
            break
    else:
        print("Please enter y or n.")