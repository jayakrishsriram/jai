m=[[1,2,3],[4,5,6]]
t=[[0,0],[0,0],[0,0]]
for i in range(len(m)):
    for j in range(len(m[0])):
        t[j][i]=m[i][j]
print('\nActual matrix' )
for i in m:
    print(i)
print("\nTranspose")
for i in t:
    print(i)
