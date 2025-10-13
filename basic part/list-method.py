# list add 
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
# list() convert string to list 
d = "hello"
print(list(d))

# append() adds an element at end of the list
e = [1,2,3,4,5,6,8]
e.append(89)
print(e)

# insert() Adds an element at the specific position
f = [1,2,3,4,5]
f.insert(3,30)
print(f)

# copy() Return a copy of the list
g = [1,2,3,4,5]
# h = g.copy()
h = g
print(h)

# count() Returns the number of element with the specific value 
i = [1,2,2,2,2,2,3,4,5]
print(i.count(2))

# extend() add the elements of a list to the end of the current list
j = [2,33,35,67,93]
# j.extend([89,23])
j = j + [67, 34]
print(j)

# pop() Remove and returnd last value from the list or the given index value
k = [2,33,35,67,93]
print(k.pop())
print(k)

# remove() remove a given object from the list 
l = [2,33,35,67,93]
l.remove(33)
print(l)

# clear() remove all items from the list
m = [2,33,35,67,93]
m.clear()
print(m)

# reverse() Reverse object from the list place
n = [2,33,35,67,93]
n.reverse()
print(n)

# sort() sort a list in ascending, descending
o = [23,3,97,45,9,-4,0,32,65,-7]
# o.sort() # default ascending 
o.sort(reverse=True) # descending
print(o)

# max() calculate the maximum of all elment of the list
p = [23,3,97,45,9,-4,0,32,65,-7]
print(max(p))

# min() calculate the minimum of all elment of the list
q = [23,3,97,45,9,-4,0,32,65,-7]
print(min(q))