Mastercard,VISA,AmericanExpress=['5',],['4',],['3',]
Number=input("Enter the number of your credit card: ")
result=0
if Number[0] in Mastercard and len(Number)==16:
    Yournumber, Yournumber2=[],[]
    for index in range(0,len(Number),2):
        Yournumber.append(int(Number[index])*2)
    firstaction=Yournumber
    for i in str(firstaction):
        for element in list(i):
            Yournumber2.append(int(element))
    secondaction=sum(Yournumber2)       

print(firstaction)
        
       
        



if Number[0] in VISA and len(Number)==13 or len(Number)==16:
    print("VISA")
if Number[0] in AmericanExpress and len(Number)==15:
    print("American Express")
else:
    print("Error!Maybe you do not enter a number correctly")
