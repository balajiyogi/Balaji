n=int(input())
def fact(n):
  fact=1
  for i in range(1,n+1):
    fact*=i
  return fact
for i in range(1,n+1):
	if(i%2 != 0):  
		print(fact(i),end=" ")
