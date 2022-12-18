print("Hi my dear friend!:3", end="\n")
print("Welcome to my program, it is a caculator, but it is another version", end="\n")
print("It use functions", end="\n")
print("You can use:'+', '-', '*', '/', ", end="\n")
print("+ =it is addition", end="n")
print("- =it is subtraction", end="\n")
print("* =it is multiplication", end="\n")
print("/ =it is division", end="\n")
print("You must use two numbers")
first=0
second=0
act=0
result=0
def numbers():
    first=int(input("Your first number: "))
    second=int(input("Your second number: "))
    return [first,second]
def action():
    numberlist=numbers()
    act=str(input("Enter your action"))
    if act=='+':
        result=numberlist[0]+numberlist[1]
    if act=='-':
        result=numberlist[0]-numberlist[1]
    if act=='*':
        result=numberlist[0]*numberlist[1]
    if act=='/':
        result=numberlist[0]/numberlist[1]
    print(result)
    

action()

       

