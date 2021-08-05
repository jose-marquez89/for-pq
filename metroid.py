import random

if __name__ == "__main__":
    rooms = random.choice(range(1, 11))

    print("Welcome to the game!")
    print(f"There are {rooms} rooms.")
    print("Check each room for danger.")
    input("Press enter to get your chances of being caught!\n")
    winning_prob = random.random()
    print(f"You have a {int(round(winning_prob, 2) * 100)}% chance of being caught!")
    input("Press enter to start checking rooms!\n")

    while rooms > 0:
        result = random.choices([1, 0], cum_weights=[winning_prob, 1.00])[0]
        if result == 1:
            print("You were captured! Thanks for playing!")
            exit()
        else:
            rooms -= 1
            print(f"The room was clear, there are {rooms} rooms remaining")
            response = input("Check another room? [y/n] ")

        if response.lower() == 'n':
            print("Thanks for playing!")
            exit()
    
    print("The coast is clear! Thanks for playing!")
    exit()