# calculator
import re
print("enter quit to exit")
previous =0
start = True
def function():
    global previous
    global start
    if previous==0:
        equation =input("enter the no:")
    else:
        equation = input(str(previous))
    if equation == "quit":
        print("Goodbye Friend")
        start = False
    else:
        equation = re.sub('[a-zA-Z,.""]', '', equation)
    if previous==0:
        previous=eval(equation)
    else:
        previous = eval(str(previous)+equation)
while start:
    function()
