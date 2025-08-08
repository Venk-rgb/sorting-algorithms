def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i < high:
            i += 1
        while arr[j] > pivot and j >= low:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot)
        quick_sort(arr, pivot + 1, high)

my_list = []
num_elements = int(input("How many elements will you enter? "))
for _ in range(num_elements):
    element = int(input("Enter an element: "))
    my_list.append(element)

print("Unsorted list")
print(my_list)

quick_sort(my_list, 0, len(my_list) - 1)
print("Sorted list")
print(my_list)

    