balance = 1000
while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    ch = input("Enter choice: ")
    if ch == "4":
        print("Thank you for using the ATM!")
        break
    elif ch == "1":
        print("Balance =", balance)
    elif ch == "2":
        amount = float(input("Enter deposit amount: "))
        balance += amount
    elif ch == "3":
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
        else:   
            print("Insufficient balance!")
    else:
        print("Invalid choice")