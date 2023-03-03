per=[]
while True:
    a=input("Enter your name:")
    b=int(input("Enter your age:"))
    per.append([a,b])
    c=input("continue[y/n]:")
    if c in ('n','N'):
        break
print(per)
print("\n sno \t Name \tAge \tEligible Status")
for i in range(len(per)):
    if per[i][1]>=18:
           print("\n {} \t {} \t{} \tEligible".format(i+1,per[i][0],per[i][1]))
    else:
           print("\n {} \t {} \t{} \tNot Eligible".format(i+1,per[i][0],per[i][1]))
