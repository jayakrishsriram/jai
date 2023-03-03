n=int(input("enter the no of row:"))
m=int(input("enter the no of column:"))
c=[]
for k in range(0,n):
    a=[]
    for l in range(0,m):
        b=int(input("enter the elements:"))
        a.append(b)
    c.append(a)
print(c)
t=[]
for o in range(0,m):
    e=[]
    for l in range(0,n):
        w=int(l)
        e.append(w)
    t.append(e)
print(t)    
for i in range(len(c)):
    for j in range(len(c[0])):
        t[j][i]=c[i][j]
print('\nActual matrix' )
for i in c:
    print(i)
print("\nTranspose")
for i in t:
    print(i)

