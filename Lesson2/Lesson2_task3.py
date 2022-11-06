print("Hello my friend!:3")
print("Welcome to my program, it will work like unixtime")
print("Firstly write your number")
Yournumber=int(input("Enter your number: "))
while Yournumber>0:
    for row in range(-Yournumber,0):
        print(-row,end=" ")
    print()
    Yournumber=Yournumber-1


