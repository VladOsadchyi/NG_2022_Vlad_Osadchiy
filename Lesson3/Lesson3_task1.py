print("Hi my dear friend!:3", end="\n")
print("Welcome to my program, it is a caculator, but it is another version", end="\n")
print("It use functions", end="\n")
print("You can use:'+', '-', '*', '/', ", end="\n")
print("+ =it is addition", end="n")
print("- =it is subtraction", end="\n")
print("* =it is multiplication", end="\n")
print("/ =it is division", end="\n")
print("You must use two numbers")
Number1=float(input("Enter your fist number: "))
Number2=float(input("Enter your secomd number: "))
Youraction=input("Choose your action: ")
def Sum():
        Yoursum=int(Number1+Number2)
        return Yoursum
def Diff():
    Yourdiff=int(Number1-Number2)
    return Yourdiff
def Plural():
    YourPlural=int(Number1*Number2)
    return YourPlural
def Division():
    YourDivision=int(Number1/Number2)
    return YourDivision
if Youraction== '+':
    print("Your result: "+ str(Sum()))
elif Youraction== '-':
    print("Your result: "+ str(Diff()))
elif Youraction== '*':
     print("Your result: "+ str(Plural()))
elif Youraction== '/':
    print("Your result: "+ str(Division()))
else:
    print("Error")
print("You are great!:3")



