def reverse(element):
    n = len(element)
    res = ""
    for i in range(n-1, -1, -1):
        res += element[i]
    return res
def isplme(element):
    if element == reverse(element):
        print("Your element is palandrome")
    else:
        print("Not palandrome")

s = input("Enter name or number ")
isplme(s)