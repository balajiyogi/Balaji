import itertools
n=int(input())
l=list(map(int,input().split(" ")))
l1=[]
for i in range(n):
    if(l.count(l[i]) == 1):
        l1.append(l[i])
l3=[]
l1=sorted(l1)
for i in range(2,n):
    l2=[]
    for j in range(n):
        if(l.count(l[j]) == i):
            l2.append(l[j])
    if(l2 == []):
        break
    l3.append(sorted(l2))
print(*(l1+(list(itertools.chain(*l3)))),sep=" ")
