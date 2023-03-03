n=['zero','one','two','three','four','five','six','seven','eight','nine']
c=[]
e=int(input("Enter a number: "))
while e!=0:
    r=e%10
    e=e//10
    c.append(r)
c.reverse()
for i in c:
    print(n[i],end=" ")
