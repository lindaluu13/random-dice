import random

while True:
    choice = input("Do you want to roll the dice ? (y/n) : ").lower()
    if choice == 'y':
        print("Rolling dice...\nAnd the number is... " + str(random.randint(1,6)))
    elif choice == 'n':
        print("Thank you for playing! See you soon.")
        break
    else: print("Invalid choice, try again.")