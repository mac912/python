# program to print calender of the month given by month number
# Assumptions: Leap year not considered when inputed is for February(2). Month doesn't start with specific day
mon = int(input("Enter the month number :"))
def calender():
    if mon <=7:
        if mon%2==0 and mon!=2:
            for j in range(1,31):
                print(j, end=' ')
                if j%7==0:
                    print()
        elif mon==2:
            for j in range(1,29):
                print(j, end=' ')
                if j%7==0:
                    print()
        elif mon<=7 and mon%2!=0:
            for j in range(1,32):
                print(j, end=' ')
                if j%7==0:
                    print()
    elif mon>7 and mon%2==0:
        for j in range(1,32):
            print(j, end=' ')
            if j%7==0:
                print()
    elif mon>7 and mon%2!=0:
        for j in range(1,31):
            print(j, end=' ')
            if j%7==0:
                print()
calender()
