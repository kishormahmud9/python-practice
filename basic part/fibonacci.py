
c = int(input("please enter your number: "))
a,b = 0,1
for i in range(c+1):
    print(a, end=" ")
    result = a+b
    a = b
    b = result