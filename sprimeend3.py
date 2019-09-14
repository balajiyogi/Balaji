n=int(input())
sum=0
for i in range(2,n+1):
  for j in range(2,i):
    if(i%j == 0):
      break
  else:
    if(i%10 == 3):
      sum+=i
print(sum)
