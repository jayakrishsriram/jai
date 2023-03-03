a=int(input("Enter the number of terms:"))
b=-1
c=1
d=0
for i in range(1,a+1):
    d=b+c
    print(d,end=",")
    (b,c)=(c,d)
print("...")
