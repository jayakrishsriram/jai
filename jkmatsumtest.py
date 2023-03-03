n=int(input("enter the no of row:"))
m=int(input("enter the no of column:"))
def matrix(n,m):
    c=[]
    for k in range(0,n):
        a=[]
        for l in range(0,m):
            b=int(input("enter the elements:"))
            a.append(b)
        c.append(a)
    return(c)
print("1'st matrix")
a=matrix(n,m)
print("2'st matrix")
b=matrix(n,m)
def add(a,b):
    add=[]
    for i in range(n):
        f=[]
        for j in range(m):
            g=a[i][j]+b[i][j]
            f.append(g)
        add.append(f)
    return(add)
ans=add(a,b)
print("Sum of two matrix is:")
for i in ans:
    print(i)
        

