amt=int(input("Enter the amount: "))
if amt>1000:
    discount=0.1*amt
elif amt>500:
    discount=0.05*amt
else:
    discount=0.0

print("Discount amount is:",discount)