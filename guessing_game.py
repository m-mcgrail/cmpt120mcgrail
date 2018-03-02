#guessing_game
#Lab 5 part 1   
def game():
    print("Hello, I am thinking of an animal. Can you guess what animal I am thinking of?:")
    animal = ('pig')
#lab 5 pt 2: quit function
    stop = ('quit')
    guess = input("Your guess:") 
#lab 5 pt2 : lower/upper cases
    if guess.lower() !=animal:
        False
    while (True):
        print("Nope! Guess again or quit")
        guess = input("Your guess:")
        #quit function
        if guess.lower() ==stop:
            print("Goodbye, thanks for playing!")
            return guess
        if guess.lower() ==animal:
            print("You're right! I was thinking of a", animal)
            return guess

game()
