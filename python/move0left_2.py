def move0toleft(arr, n):
    type0Index=0
    type1Index=n-1
    while(type0Index<type1Index):
        if type0Index==1:
            while(type1Index!=0):
                temp=type0Index
                type0Index=type1Index
                type1Index=temp
                type0Index-=1
            else:
                type1Index+=1


#main
arr = [0, 1, 0, 0, 1]
n=len(arr)
move0toleft(arr, n)
for i in range (0,n):
    print(arr[i])
