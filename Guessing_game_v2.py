import random

print("NUMBER GUESSING GAME")
print()
print("1. I guess the computer's number.")
print("2. Computer guesses my number.")

while True:
    choice = input("Choose a mode (1 or 2): ")

    if choice == "1":
        low = int(input("Enter the lowest number: "))
        high = int(input("Enter the highest number: "))
        guesses = 0

        secret_number = random.randint(low, high)
        guess = 0

        while True:
            guess = int(input("Guess the Number: "))
            guesses += 1

            if guess < secret_number:
                print ("It's more than that. Guess higher.")
            elif guess > secret_number:
                print ("It's not that high. Guess lower.")
            elif guess == secret_number:
                print("Good Job! You guessed right.")
                print("You got it in ", guesses, "guesses.")
                break
            else:
                print("Invalid choice")

    elif choice == "2":

        low = int(input("Enter the lowest number: "))
        high = int(input("Enter the highest number: "))

        guesses = 0

        while True:
            guess = (low + high) // 2
            guesses += 1

            print("My Guess is: ", guess)
            print("Current range: ", low, "to",high)

            feedback = input("Is it '1. lower', '2. higher', or '3. correct': ")

            if feedback == "3":
                print("I got it!")
                print("It took me ", guesses, " gueses.")
                break
            elif feedback == "1":
                high = guess - 1
            elif feedback == "2":
                low = guess + 1
            else:
                print("Please enter high, low, or correct.")
