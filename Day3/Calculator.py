a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("-------- Menu of Operations --------\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Exit")
choice=int(input("Enter your choice (1-5): "))
if choice==1:
    print("Addition:",a+b)
elif choice==2:
    print("Subtraction:",a-b)
elif choice==3:
    print("Multiplication:",a*b)
elif choice==4:
    if b!=0:
        print("Division:",a/b)
    else:
        print("Error: Division by zero is not allowed.")
elif choice==5:
    print("Exiting the calculator. Goodbye!")
