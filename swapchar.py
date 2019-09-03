s=input()
l=[]
for i in s:
	l.append(i)
for j in range(0,len(s),2):
	l[j],l[j+1]=l[j+1],l[j]
for k in l:
	print(k,end="")
