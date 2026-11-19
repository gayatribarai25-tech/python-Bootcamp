import random
computer_number = random.randint(1, 5)
count = 0

while count < 3:
    user_input = int(input("Enter a number (1-5): "))
    count = count + 1

    if user_input == computer_number:
        print("Congrats! You guessed it right!")
        break
    else:
        if count < 3:
            print("Wrong guess, attempt again.")
        else:
            print("Attempts over, Good luck next time!")