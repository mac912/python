#copy makes the duplicate in new dictionary
data = {1:1, 2:2, 3:3}
new  = data.copy()
print(data)
print(new)
del data
print(new)
for i in new:
    print(new[i])
