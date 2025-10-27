sec=6
while True:
    x=int(input("Guess the secret number: "))
    if (x!=sec):
        print("Congratulations! You guessed the secret number.")
        break
    else:
        print("Wrong guess. Try again!")