secret=7
guess=0
while guess!=secret:
    guess=int(input("Guess the number between 1 to 10: "))
    if(guess<secret):
        print("Too low!")
    elif guess>secret:
        print("Too High")
    
print("congrats!! you guessed it")