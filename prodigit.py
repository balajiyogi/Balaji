n=input()
l=[]
for i in n:
    l.append(i)
prod=1
for i in range(len(n)):
	prod*=int(l[i])
print(prod)
