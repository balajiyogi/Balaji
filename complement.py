n=input()
m=input()
l=[]
l1=[]
for i in n:
    l.append(i)
for i in m:
    l1.append(i)
if(all(l[i] not in l1) for i in range(len(n))):
    if(len(l+l1) == 26):
        print("yes")    
    else:
        print("no")
