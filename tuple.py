#tuples are immutable but lists are the mutable in nature
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
tup3 = tup1+tup2
print(tup3)
print(tup3[1:4])
print(tup3*3)

#inserting element in the tuple
tup2 = tup2[:3]+(9,)+tup2[3:]
print(tup2)

#TO replace a value in tuple at particular position  
tup2 = tup2[:2]+('test',)+tup2[3:]
print(tup2)

#delete from tuple
tup2 = tup2[:1]+tup2[2:]
print(tup2)

#method2 to different operation on typle
list1 = []
list1 = list(tup2)
list1.remove(4)
list1.pop(1)

tup2 = tuple(list1)
print(tup2)

#method 3
tup2 = tup2+(3, 6)
print(tup2)

