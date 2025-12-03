n = int(input("Enter size: "))
arr = []
k = 5  

for i in range(n):
    val = int(input(f"Enter value for arr[{i}]: "))
    arr.append(val)

for i in range(n):
    if arr[i] == k:
        print("True")
        print(i)
    else:
        print("False")
