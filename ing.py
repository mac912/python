str = input()
if len(str)<3:
    print(str)
else:
    if str[-3:]=="ing":
        print(str+"ly")
    else:
        print(str+"ing")
