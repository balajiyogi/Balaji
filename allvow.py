n=int(input())
l=[]
for i in range(n):
    l.append(input())
count=0
for i in range(n):
    if(('a' in l[i]) or ('e' in l[i]) or ('i' in l[i]) or ('o' in l[i]) or ('u' in l[i]) or ('A' in l[i]) or ('E' in l[i]) or ('I' in l[i]) or ('O'in l[i]) or ('U' in l[i])):
        count+=1
if(count == n):
    print("yes")
else:
    print("no")
