def comb(l):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i!=j and j!=k and k!=i):
                    print(l[i],l[j],l[k])
a=input("enter a 3 digit number:")
comb(a)                    
