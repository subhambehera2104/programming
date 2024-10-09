def binarysearch(arr, search):
    n = len(arr)
    mid = n // 2 # calculate middle index
    if (search >= arr[mid]):
        for i in range(mid, n):
            if(arr[i] == search):
                print(f"Your searched element is founded at index {i}")
                return
    elif (search < arr[mid]):
        for i in range(mid, -1, -1):
            if arr[i] == search:
                print(f"Your searched element id founded at index {i}")
                return
    #if not found, print not instead using else
        print("Your element is not found")

n = [1, 2, 3, 4, 5, 6]
print("Your array is [1, 2, 3, 4, 5]")
s = int(input("Enter search number : "))
binarysearch(n, s)