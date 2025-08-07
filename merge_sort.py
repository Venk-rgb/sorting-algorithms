def merge(arr, low, mid, high):
    # arr1 -> [low: mid]
    # arr2 -> [mid + 1, high]

    l = low
    r = mid + 1
    res = []

    while l <= mid and r <= high:
        if arr[l] < arr[r]:
            res.append(arr[l])
            l += 1
        
        else:
            res.append(arr[r])
            r += 1
    
    while l <= mid:
        res.append(arr[l])
        l += 1
    
    while r <= high:
        res.append(arr[r])
        r += 1
    
    return res

def merge_sort(arr, low, high):
    if low == high:
        return
    
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    sorted_part = merge(arr, low, mid, high)
    arr[low: high + 1] = sorted_part


my_list = []
num_elements = int(input("How many elements will you enter? "))
for _ in range(num_elements):
    element = input("Enter an element: ")
    my_list.append(element)

print("Unsorted list")
print(my_list)

merge_sort(my_list, 0, len(my_list) - 1)
print("Sorted list")
print(my_list)
