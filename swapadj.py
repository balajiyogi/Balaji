n=int(input())
a=[int(x) for x in input().split(' ',n-1)]
i=0
while(i < len(a)-1):
	a[i],a[i+1] = a[i+1],a[i]
	i+=2
for i in a:
	print(i,end=" ")
