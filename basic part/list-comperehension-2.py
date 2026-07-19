a = []

for i in range(1, 20):
    if i % 3 == 0:
        a.append(i)
    if i % 5 == 0:
        a.append(i)
print(a)

b = [i for i in range(1, 20) if i % 3 == 0 or i % 5 == 0]
print(b)

# if else in list comperehension
c = []

for i in range(1, 10):
    if i % 2 == 0:
        print("Even")
    else:
        print("Odd")

print(c)

d = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 10)]
print(d)