# program to print calender of the month
y = int(input("Enter the number of days in a month :"))
for i in range(1, y, 7):
    for x in range(i, i+7):
        if x<y+1:
            print(x, end = " ")
    print()
        
