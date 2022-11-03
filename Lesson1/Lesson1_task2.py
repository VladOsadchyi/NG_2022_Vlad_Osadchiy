print("Hi my dear friend!:p", end="\n")
print("Choose two numbers, you can use subtract or positive kinds of numbers", end="\n")
Firstnumber=int(input("Enter first number: "))
Secondnumber =int(input("Enter second number: "))
print("Nice!Now you must choose some actionc", end="\n")
print("You can choose:+, -, /, *", end="\n")
print("+ =it is addition", end="n")
print("- =it is subtraction", end="\n")
print("* =it is multiplication", end="\n")
print("/ =it is division", end="\n")
print("Please, choose your action,you must write it under this phrase :3")
Youraction=(input("Your action:"))
if Youraction == '+':
    print(Firstnumber+Secondnumber)
elif Youraction =='-':
    print(Firstnumber-Secondnumber)
elif Youraction =='*':
    print(Firstnumber*Secondnumber)
elif Youraction =='/':
    print(Firstnumber/Secondnumber)
else:
    print("Error!Do you choose the right action?Try again")