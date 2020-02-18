s=str(input())
s=list(s)
l=[]
for i in range(len(s)):
    if(s[i] != s[len(s)-1-i]):
        l.append(s[i])
if(l == []):
    print("Minimal string is empty")
else:
    print(*l,sep="")
