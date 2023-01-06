import platform
import psutil
def file():
      with open(r"out.text.txt", "w") as file:
        for element in elforcycle:
          file.write(element+'\n')
      file.close()
print("Hi me dear friend!\n This program will give the information about your computer\n Punkts of it you will see now")
options={
  "a-CPU"
  "b-RAM"
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
allelements=[]

while True:
  if punkts["y"]:break
  desire=input("Enter your desires: ").split(",")
  for element in desire:
    if punkts[element]==False:
       punkts[element]=True
    if element=='a':
      result=platform.processor().split(" ")[0]
      print("Your CPU: "+result)
    if element=='b':
      memory=psutil.virtual_memory()
      result=str(round(float(memory.total / 1073741824), 2))
      print("Your RAM:"+result)    
    if element=='c':
      result=platform.architecture()[0]
      print("Architecture:"+result)     
    if element=='d':
      result=platform.processor().split(" ")[2]
      print("CPU Family:"+result)
    if punkts[element]==True:
          allelements.append(result)
    if punkts[element]==True:
          allelements.append(result)
          elforcycle=set(allelements)

file()

print(punkts)
