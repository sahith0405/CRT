#1.Linear search
def LinearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
#driver code
arr = [1,2,3,4,5]
target = 5
result = LinearSearch(arr,target)
if result != -1:
    print("Element found at index:",result) 
else:
    print("Element not found in the array.")
#2.Binary search