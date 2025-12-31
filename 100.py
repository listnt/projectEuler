Y0=1
Yprev=1
X0=1
Xprev=1

x=(X0+1)//2
y=(Y0+1)//2

while y<=int(10**12):
    Y=Yprev*Y0*Y0+2*Yprev*X0*X0+2*2*Xprev*X0*Y0
    X=Xprev*Y0*Y0+2*Xprev*X0*X0+2*Yprev*X0*Y0
    Xprev=X
    Yprev=Y
    x=(X+1)//2
    y=(Y+1)//2
    print(x,y)