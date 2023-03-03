import random
st,p,s='stone','paper','scissor'
a=[st,p,s]
b={1:st,2:p,3:s}
c=int(input("Enter the number of round:"))
wn=[(p,st),(st,s),(s,p)]
user=0
comp=0
draw=0
def score():
    print("User score:",user,"\nComputer score",comp,"\nNumber of draw:",draw)
    if(user>comp):
        print("You won the match in {} point.".format(user-comp))
    elif(user<comp):
        print("You lost the match in just {} point.".format(comp-user))    
    else:
        print("Match draw.")
for i in range(c):
    print("===============================")
    print("Press:\n1->stone\n2->paper\n3->scissor")
    d=int(input("Enter your choice:"))
    if(d>=1 and d<=3):
        e=random.choice(a)
        print("User choice:",b[d],"\nComputer choice:",e)
        if((b[d],e) in wn):
            print("Hey you won the round {}.".format(i+1))
            user+=1
        elif(b[d] in a and b[d]==e):
            print("Draw in round {}.".format(i+1))
            draw+=1
        else:
            print("Hey you lost the round {}.".format(i+1))
            comp+=1
    else:
        print("Invalid choice")
print("===============================")
score()
        









            
            
