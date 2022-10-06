import random

magic_num = 0
guess_num = 0
guessed = False
num_attempts = 0
keep_playing = True
play_again = ""

print("WELCOME TO --GUESS MY NUMBER--")
print()

while keep_playing is True:
    magic_num = random.randint(1, 100)

    while guessed is False:
        num_attempts += 1
        if num_attempts != 1:
            guess_num = int(input(f">>Guess #{num_attempts} "))
        else:
            guess_num = int(input(f">>Enter your first guess! "))
        if guess_num < magic_num:
            print("Higher")
        elif guess_num > magic_num:
            print("Lower")
        else:
            print("You guessed it!")
            guessed = True
            break

    print(f"You made {num_attempts} guesses!")

    while play_again not in ("y", "n"):
        play_again = (input("Play again? [y/n] ")).lower()
    if play_again == "y":
        play_again = ""
        guessed = False
        num_attempts = 0
        guess_num = 0
        keep_playing = True
    else:
        keep_playing = False

print()
print("THANK YOU FOR PLAYING --GUESS MY NUMBER--")


