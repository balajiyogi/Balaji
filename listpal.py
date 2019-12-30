n=int(input())
l=list(map(int,input().split(" ",n-1)))
l1=list(map(int,input().split(" ",n-1)))
if(l == l1[::-1]):
	print("yes")
else:
	print("no")
