n=input()
l=[]
for i in n:
  l.append(i)
print(l)
count=0
for i in range(len(l)-1):
  if(int(l[i])==int(l[i+1])):
    count+=1
if(count >= 1):
  print("yes")
else:
  print("no")
