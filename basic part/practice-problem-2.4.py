a = int(input("Enter your Number between 1 to 100 : "))

if a > 90 and a <= 100:
    print("grade A")
elif a > 80 and a <= 90:
    print("grade B")
elif a >= 60 and a <= 80:
    print("grade C")
elif a >= 1 and a < 60:
    print("grade D")
else:
    print("Please input a valid number")