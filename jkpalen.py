n=input("Enter the string:")
m=''
for i in range(len(n)-1,-1,-1):
    m=m+n[i]
print(m)
if n==m:
    print("The word {} is a palindrome .".format(m))
else:    
    print("The word {} is a not palindrome .".format(m))
