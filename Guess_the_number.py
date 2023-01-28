import random

# Set the range of numbers to choose from
number_range = range(1, 11)

# Select a random number from the range
random_number = random.choice(number_range)

# Set initial score and guess count
score = 100
guess_count = 0

while True:
    # Get user's guess
    user_guess = int(input("Guess a number between 1 and 10: "))
    guess_count += 1

    if user_guess == random_number:
        print("You guessed correctly! Your score is: ", score)
        break
    else:
        score -= 10
        if user_guess > random_number:
            print("Your guess is greater than the number. You have ", score, " points remaining")
        else:
            print("Your guess is less than the number. You have ", score, " points remaining")
    if guess_count == 5:
        print("You have reached the maximum number of guesses! The number was: ", random_number)
        break