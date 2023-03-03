a=input("Enter the number:")
b=len(a)
c=0
d=0
for i in range(b):
    if(int(a[i])%2==0):
        c+=1
    else:
        d+=1
print("Number of even numbers are:",c)
print("Number of odd numbers are:",d)        

