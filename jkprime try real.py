import math
n=int(input("Enter the number:"))
m=math.sqrt(n)
o=round(m)
if n%m==0:
    print("not prime")
else:
    for i in range(2,o):
        if n%i==0:
            print("not_prime")
            break
    else:
        print("prime")
