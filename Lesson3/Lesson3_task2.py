print("Hi my dear friend!:3", end="\n")
print("Welcome to my program, which will give you some interesting actions", end="\n")
print("Firstly you should write your list")
print("Good luck)")
print("Firstly you should wite your list")
result=0
list=input("Enter yor list: ")
def youractions():
        print("And now we are going to show some actions!\n First-we can sort your list(put 1)\n Second-we can count symbols(put 2) ")
        print(" Third-we can write your vowels and constants of your list(put 3.1-if vowels or 3.2-if constants)\n")
        print(" Fourth-we can give you a proposal to break it down into words,and remove the words from the end(not backwards-forwards)(put 4) ")
        print(" Fifth-we can give you an offer to display the word by number(put 5)\n Sixth-we can give you a proposal to enter the deadline again\n")
        print(" Seventh-we can give you an offer to exit the program")
        action=input("Enter your number: ")
        if action=='1':
            result=set(list) 
            print(result)   
        if action=='2':
            result={}
            count=set(list)
            for element in count:
                result[element]=list.count(element)
            print(result)
        if action=='3.1':
           vowels={'a','e','i','o','u','y'}
           for letters in list:
            if letters in vowels:
                print(letters)
        if action=='3.2':
             vowels={'a','e','i','o','u','y'}
             result=set(list)-set(vowels)
             print(result)
        if action=='4':
            Yourlist=list.split(" ")
            result=Yourlist[::-1]
            print(result)
        if action=='5':
            i=0
            Yourlist2=list.split(" ")
            for element in Yourlist2:
                    i=i+1
                    print(element+" його номер:"+str(i))
        if action=='6':
             list2=(input("Enter your new list: "))
        if action=='7':
            SystemExit
        else: 
            print("Error")
    
           
        

youractions()
