a=input()
l=[]
for i in a:
    l.append(i)
b=l.copy()
for i in range(len(l)):
    for j in range((len(l))):
        if(i != j):
            if(l[i] == l[j]):
                b.remove(l[i])
                break
if(len(b) > 0):
  print(len(b))
else:
  print(-1)
