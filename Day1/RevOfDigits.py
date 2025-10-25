n=123
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n//=10

print("Reverse of the number is ",rev)