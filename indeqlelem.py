n=int(input())
l=list(map(int,input().split(" ",n-1)))
l1=[]
for i in range(n):
    if(i == l[i]):
        l1.append(l[i])
if(l1 == []):
	print(-1)
else:
	print(*(sorted(l1)))
