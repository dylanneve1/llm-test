
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
