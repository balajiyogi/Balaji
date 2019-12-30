n=input()
for i in range(len(n)):
    if(n[i] in ('a','e','i','o','u','A','E','I','O','U')):
    	print(n[i],end="")
for i in range(len(n)):
    if(n[i] not in ('a','e','i','o','u','A','E','I','O','U')):
    	print(n[i],end="")
