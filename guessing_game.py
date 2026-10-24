import random

number = random.randint(1, 20)
attempts = 0
max_attempts = 5

print("Number Guessing Game")
print("Guess a number between 1 and 20!")
print(f"You have {max_attempts} attempts.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print(f"Correct! You won in {attempts} attempts!")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

if attempts == max_attempts and guess != number:
    print(f"Game over! The number was {number}.")
