import random

while True:
    choice = input("Do you want to roll the dice ? (y/n) : ").lower()
    if choice == 'y':
        try:
            num_dice = int(input("How many dice do you want to roll? (between 1 to 10) : "))
            if num_dice < 1 or num_dice > 10:
                print("Please enter a number greater than 0 and below 10.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        print("Rolling dice...")
        results = [random.randint(1, 6) for _ in range(num_dice)]
        print("You rolled: " + ", ".join(str(r) for r in results))

    elif choice == 'n':
        print("Thank you for playing! See you soon.")
        break
    else: print("Invalid choice, try again.")