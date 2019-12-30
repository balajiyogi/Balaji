n=input().split(" ")
l=[]
for i in n[0]:
    l.append(i)
l=set(l)
if(all(x in l for x in n[1])):
    print("true")
else:
    print("false")
