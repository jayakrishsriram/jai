p=float(input("Enter principal:"))
t=float(input("Enter time(in month):"))
r=float(input("Enter rate:"))
s_i=(p*t*r)/100
c_i=p*((1+r/100)**t-1)
print('simple interest is %f'%(s_i))
print('compound interest is %f'%(c_i))
