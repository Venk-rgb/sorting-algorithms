def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    
    return nums


my_list = []
num_elements = int(input("How many elements will you enter? "))
for _ in range(num_elements):
    element = int(input("Enter an element: "))
    my_list.append(element)

print("Unsorted list")
print(my_list)

my_list = bubble_sort(my_list)
print("Sorted list")
print(my_list)
