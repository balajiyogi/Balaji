a,b=map(str,input().split(" "))
c=0
for i in range(len(a)-1):
    for j in range(len(b)-1):
        if(a[i] == b[j]):
            if(a[i+1] == b[j+1]):
                c+=1
if(c > 1):
	print("yes")
else:
	print("no")
