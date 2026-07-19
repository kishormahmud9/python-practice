# 2d list comperehension

# 2d matrix convert into transpose matrix 
matrix = [[1,3], [3,4], [5,6], [7,8]]

a = []
for row in range(2):
    b = []
    for col in matrix:
        b.append(col[row])
    a.append(b)

print(a)

b = [[col[row] for col in matrix] for row in range(2)]
print(b)