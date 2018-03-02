#guessing_game
#Lab 5 part 1
def answer(guess):
    print("Nope! Guess again")
    guess = input("Your guess:")
    return guess    
def game():
    print("Hello, I am thinkiing of an animal. Can you guess what animal I am thinking of?:")
    animal = ('pig')
    guess = input("Your guess:")
    while guess != animal:
        return(answer(guess))
    else:
        print("You're right! I was thinking of a", animal)
    print("Thanks for playing!")     
game()
