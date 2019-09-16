n=int(input())
a=list(map(int,input().split(" ",n-1)))
b=[]
for i in range(n):
    for j in range(n):
        if(i != j):
            if(a[i] == a[j]):
                b.append(a[i])
                break
b=set(b)
if(b == set()):
    print(-1)
else:
    for i in b:
        print(i,end=" ")
