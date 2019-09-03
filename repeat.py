n,m=input().split()
n=int(n)
m=int(m)
arr=[int(x) for x in input().split(' ',n-1)]
count=0
for i in range(len(arr)):
	if(m == arr[i]):
		count+=1
print(count)
