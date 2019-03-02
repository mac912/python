#deletion in the dictonary
square = {1:1, 2:4, 3:9, 4:16, 5:25}
print(square.pop(4))
print(square)
print(square.popitem())
print(square)
del square[5]
print(square)
#square.clear()
print(square)
#del square
d = {2:1}
square.update(d)
print(square)
