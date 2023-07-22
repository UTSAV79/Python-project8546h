import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("You have to guess the number within", max_attempts, "attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == secret_number:
                print("Congratulations! You guessed the correct number", secret_number, "in", attempts, "attempts!")
                break
            elif guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print("Out of attempts. The secret number was", secret_number)

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
