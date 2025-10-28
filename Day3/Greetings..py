time=int(input("Enter time in hour (0-23): "))
if time>=12 and time <16:
    print("Good Afternoon")
elif time>=16 and time<20:
    print("Good Evening")
elif time>=20 and time<=23:
    print("Good Night")
else:
    print("Good Morning")