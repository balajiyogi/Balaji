n=int(input())
a=[int(x) for x in input().split(' ',n)]
res=0
for i in range(len(a)-1):
	res=(res|a[i])
print(res)
