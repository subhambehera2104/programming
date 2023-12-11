def frequency_of_list_best(num):
    frequency_dict={}
    for i in num:
        if i in frequency_dict:
            frequency_dict[i]+=1
        else:
            frequency_dict[i]=1
    return frequency_dict

def frequency_of_list(num):
    n= len(num)
    frequency = [1]* n
    for i in range(n):
        if frequency[i]==-1:
            continue
        for j in range(i+1,n):
            if num[i]==num[j]:
                frequency[i]+=1
                frequency[j]=-1 
    return frequency

num=[1, 4, 1, 2, 1, 4]

frequency_dict= frequency_of_list_best(num)
# print(f"frequency dict {frequency_dict}")
print("frequency dict ")
for k, v in frequency_dict.items():
    print(f"key {k} value {v}")


frequency = frequency_of_list(num)
print("frequency list ")
n = len(num)
for i in range(n):
    if frequency[i] != -1:
        print(f"key {num[i]} value {frequency[i]}")
     