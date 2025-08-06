def selection_sort(nums):
    for i in range(len(nums) - 1):
        min_idx = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    
    return nums


my_list = []
num_elements = int(input("How many elements will you enter? "))
for _ in range(num_elements):
    element = input("Enter an element: ")
    my_list.append(element)

print("Unsorted list")
print(my_list)

my_list = selection_sort(my_list)
print("Sorted list")
print(my_list)
