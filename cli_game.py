
import random

def main():
    print("Welcome to the CLI Game!")
    while True:
        user_input = input("Enter a command (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            print(f'You entered: {user_input}')

if __name__ == '__main__':
    main()

import random

# Function to generate a random number
def generate_number():
    return random.randint(1, 100)

# Function to play the guessing game
def guessing_game():
    number_to_guess = generate_number()
    attempts = 0
    print("Guess the number between 1 and 100!")
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f'Congratulations! You guessed the number in {attempts} attempts.')
            break

# Update the main function to include the guessing game

def main():
    print("Welcome to the CLI Game!")
    while True:
        user_input = input("Enter a command (type 'guess' to play the guessing game, 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        elif user_input.lower() == 'guess':
            guessing_game()
        else:
            print(f'You entered: {user_input}')

if __name__ == '__main__':
    main()

# Function to display the score
score = 0

def display_score(attempts):
    global score
    score += max(0, 100 - attempts * 10)  # Simple scoring system
    print(f'Your current score is: {score}')

# Update the guessing game to include scoring

def guessing_game():
    global score
    number_to_guess = generate_number()
    attempts = 0
    print("Guess the number between 1 and 100!")
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f'Congratulations! You guessed the number in {attempts} attempts.')
            display_score(attempts)
            break
