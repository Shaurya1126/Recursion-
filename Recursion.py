'''def fibonnaci(x):
    if x == 0:
        return 0
    elif x==1: 
        return 1
    else:
        return fibonnaci(x-2)+fibonnaci(x-1)
        

for x in range(6):
    print(fibonnaci(x))
'''


money=int(input("How much money do you have: "))
m=0
x=0
def cho(money): 
    global m
    global x
    if money==2:
        m+=1 
    elif money%2==0:
        m=m+money/2
        return cho(money/2)
    elif money%2!=0:
        if x%2!=0: 
            money=money+x
        else:
            money=money-1
            x=x+1
        return cho(money)
cho(money)
print(m)

