print("Hi my dear friend!:3")
print("Welcome to my program!It will find square roots of your equations")
print("We wil use the discriminant")
print("Write your three numbers: a, b, c")
print("It will look like: ax^2+-bx+-c=0")
print("Write your numbers")
a=int(input("Enter your a: "))
b=int(input("Enter your b: "))
c=int(input("Enter your c: "))
D=b**2-4*a*c
print("D=", D)
print("We should  find x1 and x2", end="\n")
x1=float 
x2=float
if D>=0:
    x1=(-b-(D*0.5))/(2*a)
    x2=(-b+(D*0.5))/(2*a)
    print("x1= ", x1)
    print("x2= ", x2)
else:
    print("There are no arguments of this equation1!If D<0 so we can not find x1 and x2")