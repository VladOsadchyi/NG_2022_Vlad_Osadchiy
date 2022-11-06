print("Hi my friend!:3")
print("It will work very similar to unixtime")
print("Please, put your seconds")
Yourseconds=int(input("Enter your numbers: "))
print("So we will find the days, hours, minutes and secomds, using your number")
Yourdays=Yourseconds//86400
#86400-seconds of one day, it is the example of your work with it
Yourhours=(Yourseconds%86400)//3600
Yourminutes=(Yourseconds%3600)//60
Yourseconds=(Yourseconds%60)%60
print("Your days: "+str(Yourdays))
print("Your hours: "+str(Yourhours))
print("Your minutes: "+str(Yourminutes))
print("Your seconds: "+str(Yourseconds))