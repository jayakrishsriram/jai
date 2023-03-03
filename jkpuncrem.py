n=input("Enter the string:")
m=''
for i in n:
    if i.isalnum():
        m=m+i
    else:
        continue
print(m)
