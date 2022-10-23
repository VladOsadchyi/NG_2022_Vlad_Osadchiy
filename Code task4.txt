print("We should find the discriminant" )
D=b**2-4*a*c
print("D=", D)
print("We should  find x1 and x2", end="\n")
x1=float 
x2=float
if D>=0:
    x1=(-b-math.sqrt(D))/(2*a)
    x2=(-b+math.sqrt(D))/(2*a)
    print("x1= ", x1)
    print("x2= ", x2)
else:
    print("There are no arguments of this equation1!If D<0 so we can not find x1 and x2")
