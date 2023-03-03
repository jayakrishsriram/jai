print("The even number will be printed till the last number given")
n=int(input("Enter the last number:"))
a=0
for i in range(2,n+1,2):
    a=a+i
print("The even sum from 2....{} is:{}".format(n,a))    
