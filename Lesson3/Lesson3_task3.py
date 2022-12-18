print("Hi my dear friend!:3", end="\n")
print("Welcome to my program, which will count letters in  your list", end="\n")
print("Firstly you should write your list")
print("Good luck)")
def youraction():
    Yourlist=input("Enter your list, please: ")
    Lettercounts={}
    count=set(Yourlist)
    for element in count:
        Lettercounts[element]=Yourlist.count(element)
    print(Lettercounts)
youraction()
