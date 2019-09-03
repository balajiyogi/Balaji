n,k=input().split()
n=int(n)
k=int(k)
array = [int(x) for x in input().split(' ',n-1)]
if(k in array):
  print("yes")
else:
  print("no")
