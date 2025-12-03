def binarysearch(arr,x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid]==x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
             high = mid - 1

    return -1

if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        val = int(input())
        arr.append(val)

    x = int(input(f"Enter the value os key x : "))

    result = binarysearch(arr,x)

    if result != -1:
        print("Element is present at index ",result)

    else:
        print("Element is not present")

