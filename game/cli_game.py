import random

def generate_number(level):
    return random.randint(1, 100 + (level - 1) * 50)  # Increase range with level

def display_score(attempts):
    global score
    score += max(0, 100 - attempts * 10)  # Simple scoring system
    print(f'Your current score is: {score}')

score = 0

# Function to play the guessing game

def guessing_game():
    global score
    level = 1
    while True:
        number_to_guess = generate_number(level)
        attempts = 0
        print(f'Level {level}: Guess the number between 1 and {100 + (level - 1) * 50}!')
        while True:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            attempts += 1
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f'Congratulations! You guessed the number in {attempts} attempts.')
                display_score(attempts)
                level += 1  # Increase level after a successful guess
                break

# Main function to run the game

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

# Function to save high scores
high_scores = []

def save_score(score):
    high_scores.append(score)
    high_scores.sort(reverse=True)
    if len(high_scores) > 5:
        high_scores.pop()  # Keep only top 5 scores
    print('High Scores:', high_scores)

# Update the display_score function to save scores

def display_score(attempts):
    global score
    score += max(0, 100 - attempts * 10)  # Simple scoring system
    print(f'Your current score is: {score}')
    save_score(score)

# Function to implement a timed guessing game mode
import time
from game.scoring import save_score
from game.leaderboard import display_score

def timed_guessing_game():
    global score
    level = 1
    time_limit = 30  # 30 seconds for each level
    while True:
        number_to_guess = generate_number(level)
        print(f'Level {level}: Guess the number between 1 and {100 + (level - 1) * 50} within {time_limit} seconds!')
        start_time = time.time()
        attempts = 0
        while True:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if time.time() - start_time > time_limit:
                print('Time is up!')
                return
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f'Congratulations! You guessed the number in {attempts} attempts.')
                display_score(attempts)
                level += 1  # Increase level after a successful guess
                break
