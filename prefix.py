n=int(input())
l=list(map(str,input().split(" ",n-1)))
p=str(input())
count=0
for i in range(len(l)):
    if(p in l[i]):
    	count+=1
print(count)
