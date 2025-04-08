name = input("Hey type your name: ")
print("Hello "  + name  +  " welcome to the game!" )

should_we_play = input("DO you want to play? ").lower()

if should_we_play == "y" or should_we_play == "yes":
    print("We are gonna play! ")

    direction = input ("Do you want to play in easy mode or hard mode? (easy/hard) ").lower()
    if direction == "easy":
        print("Okay playing in easy mode and you dont have game spirit, game over, try again.")
    elif direction == "hard":
        choice = input("Okay, you are playing in hard mode, do you want higher credit limit or higher intelligence? (credit/intelligence) ")
        if choice == "credit":
            print("you are getting zero limit, try again, from start!")
        else:
            print("you chose correct option and game on!")
    else:
        print("Sorry not a valid reply, come back again!")
else:
    print("You are not allowed...")