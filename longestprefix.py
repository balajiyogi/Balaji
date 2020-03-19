n=int(input())
l=[]
for i in range(n):
    l.append(input())
c=l[0]
for i in range(1,n):
    temp = ""
    if len(c) == 0:
        break
    for j in range(len(l[i])):
        if j<len(c) and c[j] == l[i][j]:
            temp+=c[j]
        else:
            break
    c=temp
print(c)
