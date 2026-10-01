import random

# Generate random number
secret_number = random.randint(1, 300)

attempts = 0

print("===== GUESS THE NUMBER GAME =====")
print("I have selected a number between 1 and 300.") 
print("Try to guess the number!")
print()

while True:

    guess = int(input("Enter your guess: "))

    attempts += 1

    if guess < secret_number:

        print("Higher! Try again.")

    elif guess > secret_number:

        print("Lower! Try again.")

    else:

          print("\nCongratulations! You guessed the correct number.")
          print("Number of attempts:", attempts)
          print("The secret number was:", secret_number)
          print("Thanks for playing!")

          break 