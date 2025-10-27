while True:
    print("-------- Menu --------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Select an option (1-5): ")
    if choice == '1':
        print("You selected Add.")
    elif choice == '2':
        print("You selected Subtract.")
    elif choice == '3':
        print("You selected Multiply.")
    elif choice == '4':
        print("You selected Divide.")
    elif choice == '5':
        print("Exiting the menu. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")