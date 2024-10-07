def frequency_string1(name):
    frequency_dict={}
    n=len(name)
    for i in range(n):
        if name[i] in frequency_dict:
            frequency_dict[name[i]] +=1
        else:
            frequency_dict[name[i]]=1
    return frequency_dict


def frequency_string2(name):
    frequency_dict={}
    for c in name:
        if c in frequency_dict:
            frequency_dict[c]+=1
        else:
            frequency_dict[c]=1
    return frequency_dict
    


name = input("Enter name ")
res1=frequency_string1(name)
for k,v in res1.items():
    print(f"key {k}, value {v}")

print("\n")
res2=frequency_string2(name)
for k,v in res2.items():
    print(f"key {k}, value {v}")