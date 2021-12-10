import random
p=int(input("Enter prime number 1::")) #383
q=int(input("Enter prime number 2::")) #503
X=[]
B=[]
n=p*q
if (p%4==3 and q%4==3):
    s= random.randint(1,n-1)
    if(s%n==0):
        while(s%n==0):
            s= random.randint(1,n-1)
    else:
        X.append((s**2)%n)
        for i in range(1,49):
            X.append((X[i-1]**2)%n)
            B.append(X[i]%2)
    print("The random numbers are",X)
    print("The binary numbers are",B)
    print("The value of S is",s)

    
else:
    print("Not a valid pair of prime numbers")

