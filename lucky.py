n=int(input())
l=list(map(int,input().split(" ",n-1)))
count=0
for i in range(1,n+1):
    if((n*i) in l):
        count+=1
print(count)
