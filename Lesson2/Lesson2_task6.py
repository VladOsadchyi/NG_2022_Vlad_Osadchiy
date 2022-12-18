print("Hello my friend!:3\n This program will decipher your task from Caesar's cipher\n Good luck!")
list=(input("Enter your message: "))
key=int(input("Enter your key: "))
result=''
alfavit='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in list:
    pos=alfavit.find(i)
    newpos=pos+key
    if i in alfavit:
        result+=alfavit[newpos]
    else:
        result+=i
print("================================================================")
print(result)



