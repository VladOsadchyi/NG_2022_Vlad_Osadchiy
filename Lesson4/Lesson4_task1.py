import platform
import psutil
print("Hi me dear friend!\n This program will give the information about your computer\n Punkts of it you will see now")
options={
  "a-CPU"
  "b- RAM"
  "c-Architecture"
  "d-CPU Family"
  "y-Proceed"
}
print("The last option you must choose after all your desires, for choosing you must put only the first letter, like a or b")
punkts={
  "a":False,
  "b":False,
  "c":False,
  "d":False,
  "y":False
}
while True:
  if punkts["y"]:break
  desire=input("Enter your desires: ").split(",")
  for element in desire:
    if punkts[element]==False:
       punkts[element]=True
    if element=='a':
      print("Your CPU: "+platform.processor().split(" ")[0])
    if element=='b':
      memory=psutil.virtual_memory()
      memory2=round(float(memory.total / 1073741824), 2)
      print("Your RAM: ",memory2)
    if element=='c':
      print("Architecture: "+platform.architecture()[0])
    if element=='d':
      print("CPU Family: "+platform.machine())
print(punkts)
