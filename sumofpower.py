n=input()
l=[]
for i in n:
    l.append(i)
sum=0
for i in range(len(n)):
    sum+=int(n[i])**(len(n))
print(sum)
