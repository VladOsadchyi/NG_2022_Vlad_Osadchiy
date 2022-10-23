print("Hi my dear friend :3", end="\n")
print("Welcome to my translator(homework) fron seconds to day:hours:minutes:seconds", end="\n")
print("The name of this program is 'Gogol'", end="\n")
print("I hope you will like it", end="\n")
print("So you must write your seconds, without milliseconds", end="\n")
Yourseconds=int(input("Enter seconds"))
import datetime
print(datetime.datetime.fromtimestamp(Yourseconds).strftime('%d:%H:%M:%S'))