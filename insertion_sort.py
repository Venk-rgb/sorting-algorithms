def insertion_sort(nums):
    n = len(nums)
    for i in range(n):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
    
    return nums


my_list = []
num_elements = int(input("How many elements will you enter? "))
for _ in range(num_elements):
    element = int(input("Enter an element: "))
    my_list.append(element)

print("Unsorted list")
print(my_list)

my_list = insertion_sort(my_list)
print("Sorted list")
print(my_list)
