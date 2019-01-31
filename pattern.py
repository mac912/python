#program to print the pattern
#1
#12
#123
#1234
#12345


#1
#22
#333
#4444
#55555

for i in range(1, 6):
    for x in range(1, i+1):
        print(x, end="")
    print()

print()
for i in range(1, 6):
    for x in range(1, i+1):
        print(i, end="")
    print()
