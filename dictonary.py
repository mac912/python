dict1 = {1:'start', 'name':'saini', 'age':10}
print(dict1)
print(dict1['name'])
#or
print(dict1.get('age'))
print(dict1.get(1))
print("After making some changes")
print()
dict1[1] = 'end'
dict1['name']= 'manish'
dict1['age'] = 20
print(dict1[1])
print(dict1['name'])
print(dict1['age'])     


