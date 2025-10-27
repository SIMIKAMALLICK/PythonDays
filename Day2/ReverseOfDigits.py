x=int(input("Enter a number: "))
rev=0
while True:
    rev=rev*10 + x%10
    x=x//10
    if x==0:
        break
print("Reverse of the number is:",rev)