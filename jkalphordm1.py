a=input("enter strings:")
b=a.lower()
o=[]
for c in b:
   o+=c
print(o)
for i in range(0,len(o)-1):
    for j in range(0,len(o)-1):
        for k in range(0,i+1):
            if o[j]>o[j+1]:
                o[j],o[j+1]=o[j+1],o[j]
print(o)                
