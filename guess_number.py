import random

number = int(input("Guess a number between 1 and 100: "))
random_number = random.randint(1, 100)

print(f"Debug {random_number}")

while True:
    if number < random_number:
        print("Too low! Try again.")
        number = int(input("Guess a number between 1 and 100: "))
    elif number > random_number:
        print("Too high! Try again.")
        number = int(input("Guess a number between 1 and 100: "))
    else:
        print("Congratulations! You guessed the correct number:", random_number)
        break