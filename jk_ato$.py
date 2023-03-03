b=input("enter the string:")
c=b.replace("a","$")
print(c)
#---------------------------------------
b=input("Enter the string:")
n=int(input("Enter the n'th value:"))
m=" "
for i in range(len(b)):
    if i==n:
        continue
    else:
        m+=b[i]
print(m)      
#----------------------------------------        
b=input("Enter the string:")
c=""
d=b[len(b)-1]
for i in range(0,len(b)):
    if i==0:
        c+=d
    elif i==(len(b)-1):
        c+=b[0]
    else:
        c+=b[i]
print(c)        

#----------------------------------------
b=input("Enter the string:")
c=0
for i in range(0,len(b)):
    if b[i].islower():
        c+=1
print("count:",c)   
#-----------------------------------------
b=input("Enter the string:")
c=input("Enter the string:")
if b>c:
    print(b)
else:
    print(c)

#-----------------------------------------
b=input("Enter the string:")
c=b.lower()
d={'a','e','i','o','u'}
e=0
for i in c:
    if i not in d:
        e+=1

print("no of consonants is: "+str(e))

#--------------------------------------------------


        





   



