n=int(input())
arr1=[int(x) for x in input().split()]
arr2=[int(y) for y in input().split()]
for i in range(n):
    arr1[i] = arr1[i]+arr2[i]
for i in arr1:
    print(i,end=" ")
