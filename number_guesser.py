import random

print("Welcome to number guesser!")

playing = input("Would you like to guess some numbers?(Type Y/N): ")

if playing.lower().strip() != "y":
    print("Okay, guess, another time...")
else:
    print("Awesome let's get to guessing!")

# Random number
r = random.randrange(25)
guesses = 0

print("What number am I thinking of? (Any number between 0 and 25)")

while True:

    # The users input value
    answer = input("Your guess: ")
    
    # Check if the number is a 'number'
    if not answer.isdigit():
        guesses += 1
        print("Enter a real number please!")
        continue
    
    # Answer if it is a number
    answer = int(answer)

    # Make sure it's greater than 0
    if answer < 0:
        guesses += 1
        print("Type a number bigger than 0!")
        continue

    # Make sure it's smaller than 25
    elif answer > 25:
        guesses += 1
        print("Type a number smaller than 25!")
        continue

    # If the user is wrong indicate that
    elif answer != r:
        guesses += 1
        print("WRONG!")

    # Other wise they've won!
    else:
        guesses += 1
        print("How did you know the number was " + str(r) + "??????")
        break
if(guesses <= 2):
    print("Did you cheat? You only guessed", guesses,"times.")
elif(guesses >= 3):
    print("Dang you're good... You guessed", guesses,"times")
elif(guesses >= 10):
    print("Not bad")
else:
    print("The force is not strong with this one... You had to guess", guesses,"times")