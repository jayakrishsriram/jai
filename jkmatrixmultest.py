n1=int(input("Enter the number of row in matrix 1:"))
m1=int(input("Enter the number of column in matrix 1:"))
n2=int(input("Enter the number of row in matrix 2:"))
m2=int(input("Enter the number of column in matrix 2:"))
def matrix(n,m):
    a=[]
    for i in range(n):
        b=[]
        print(" {}'st row:".format(i+1))
        for j in range(m):
            c=int(input("Enter the element:"))
            b.append(c)
        a.append(b)
    return(a)
def multiply(q,u):
     mul=[]
     for d in range(n1):
        jk=[]
        for p in range(m2):
            m=0
            for s in range(len(q[0])):
                m=m+q[d][s]*u[s][p]
            jk.append(m)
        mul.append(jk)
     for y in mul:
           print(y)
if (n1==m2):
    print("matrix 1")
    q=matrix(n1,m1)
    print("matrix 2")
    u=matrix(n2,m2)
    multiply(q,u)                
else:
    print("no of row of first matrix must be equal to column of second matrix")
