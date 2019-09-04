n=input()
l=[]
for i in n:
    l.append(i)
sum=0
for i in range(len(n)):
    sum+=int(l[i])
if(sum%2 == 0):
    print("E")
else:
    print("O")
