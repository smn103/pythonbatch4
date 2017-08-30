import cmath
def quadratic(a,b,c):
    d=b*b-4*a*c
    if(d==0):
        print("Roots are Real and Equal")
        r1=b/(2*a)
        r2=b/(2*a)
        return r1,r2
    elif(d>0):
        print("Roots are Real and Unequal")
        r1=(b+cmath.sqrt(d)/(2*a))
        r2=(b-cmath.sqrt(d)/(2*a))
        return r1,r2
    else:
        print("Roots are Imaginary")


print("Enter the Quadratic Equation")
a=int(input("Enter a\n"))
b=int(input("Enter b\n"))
c=int(input("Enter c\n"))
r1,r2=quadratic(a,b,c)
print("The Roots are ",r1,r2)
