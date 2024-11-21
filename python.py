import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I am thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    guesses_taken = 0
    
    while True:
        # Ask the user for their guess
        guess = int(input("Enter your guess: "))
        guesses_taken += 1
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number} in {guesses_taken} attempts.")
            break

guess_the_number()
