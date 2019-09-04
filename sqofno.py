n=input()
a=[]
for i in n:
  a.append(i)
sum=0
for i in range(len(n)):
  sum+=int(a[i])**2
print(sum)
