arr=[0, 1, 0, 0, 1]
n = len(arr)
count=0
for i in range (0,n):
    if arr[i]==0:
        count+=1
for j in range(0,count):
    arr[j]=0
    print(arr[j],end="")
for k in range(count,n):
    arr[k]=1
    print(arr[k],end="")

