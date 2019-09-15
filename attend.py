n=int(input())
attend=input().split(" ",n-1)
count=0
for i in range(n):
	if('P' == attend[i]):
    	count+=1
if(int((count/n)*100) > 25):
	print("Not Blacklisted")
else:
	print("Blacklisted")
