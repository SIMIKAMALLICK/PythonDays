while True:
    x=input("Enter a number:")
    if int(x)<0:
        print("Negative number entered, exiting loop.")
        break
    else:
        print(f"Your number is positive")