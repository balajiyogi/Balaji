n=str(input())
n=list(n)
l=[]
for i in range(len(n)):
    if(n.count(n[i])>1):
        l.append(n[i])
l=set(l)
print(len(l))
