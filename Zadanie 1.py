a=float(input())
b=float(input())
c=float(input())
D=b**2-4*a*c
if D<0:
    print('Korney net')
elif D==0:
    x=-(b**2)/(2*a)
    print(x)
else:
    x1=(-b+(D**0.5))/(2*a)
    x2=(-b-(D**0.5))/(2*a)
    print(x1, x2)