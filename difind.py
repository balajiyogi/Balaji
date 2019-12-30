n=int(input())
l=list(map(int,input().split(" ",n-1)))
print((l.index(max(l)))-(l.index(min(l))))
