def assending_order(num):
    n=len(num)
    for i in range(0,n):
        for j in range(i+1,n):
            if num[i]>num[j]:
                num[i],num[j]=num[j],num[i]
    return num

def descending_order(num):
    n=len(num)
    for i in range(0,n):
        for j in range(i+1,n):
            if num[i]<num[j]:
                num[i],num[j]=num[j],num[i]
    return num
    
#  main
num=[10, 2, 1, 3, 4]
res=assending_order(num)
print(f"assending order {res}")

res=descending_order(num)
print(f"desc order {res}")