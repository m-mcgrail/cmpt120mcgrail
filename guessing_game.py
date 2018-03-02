#guessing_game
#Lab 5 part 1   
def game():
    print("Hello, I am thinking of an animal. Can you guess what animal I am thinking of?:")
    animal = ('pig')
    guess = input("Your guess:")
    if guess !=animal:
        False
    while (True):
        print("Nope! Guess again")
        guess = input("Your guess:")

        if guess ==animal:
            print("You're right! I was thinking of a", animal)
            return guess

game()
