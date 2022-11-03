print("Hi my dear friend :3", end="\n")
print("Welcome to my translator(homework) from seconds to day:hours:minutes:seconds", end="\n")
print("The name of this program is 'Gogol'", end="\n")
print("I hope you will like it", end="\n")
print("So you must write your seconds, without milliseconds", end="\n")
Yourseconds=int(input("Enter seconds: "))
Yourdays=Yourseconds//86400
Yourhours=(Yourseconds%86400)//3600
Yourminutes=(Yourseconds%3600)//60
Yorseconds2=(Yourseconds%60)//60



print(Yourdays, Yourhours, Yourminutes)