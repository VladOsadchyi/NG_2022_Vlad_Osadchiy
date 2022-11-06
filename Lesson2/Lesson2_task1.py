print("Hi my dear friend!:3", end="\n")
print("Welcome to my program, which will count letters in  your words", end="\n")
print("Firstly you should write your words, but you must write only words, without other symbols")
print("If you want to write a new word, you shoul put after the previous ")
print("Good luck)")
Yourlist=input("Enter your list: ")
Lettercounts={}
uniqueletters=set(Yourlist)
for element in uniqueletters:
    Lettercounts[element]=Yourlist.count(element)
print(Lettercounts)
