print("Hi my dear friend!:3", end="\n")
print("Welcome to my program that will find the min and max of your number, also it will find the sum of them", end="\n")
print("But you must write only numbers", end="\n")
print("After numbers put ','")
print("Let's start", end="\n")
YourNumbers=[]
YourNumbers=input("Enter your numbers: ")
YourNumbers=list(map(int,YourNumbers.split(",")))
YourNumbers.sort()
print(YourNumbers)
print(min(YourNumbers))
print(max(YourNumbers))
print("Very well!:3 And know we will find the sum of others numbers(without max and min)")
print(sum(YourNumbers[1:-1]))
