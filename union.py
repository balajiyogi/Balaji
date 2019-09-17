n=int(input())
a=list(map(int,input().split(" ",n-1)))
m=int(input())
b=list(map(int,input().split(" ",m-1)))
for i in b:
    a.append(i)
a=sorted(a)
for i in a:
    print(i,end=" ")
