a = [12, 98,45, 45, "some"]
print(a)
a[4]="kichu"
print(a)
print(len(a))

if 98 in a:
    print("found")
else:
    print("not found")

#  **** traversing ****
# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])

# for i in range(-1, -len(a)-1, -1):
#     print(a[i])

for i in range(len(a)-1, -1, -1):
    print(a[i])

# nested list 
b = [[90,92,38],["hello", "world", 2000], [12,13,14]]
b[0][1] = 56
print(b[0][1])


# **** List Slicing ****c
c = [1,2,3,4,"Kishor", "mahmud", [87,90]]
print(c[::])
print(c[1::])
print(c[2::4])
print(c)
# list reverse technique
print(c[::-1])
print(c[-1:-3:-1])
# empty list 
print(c[-1:-1:-1])
