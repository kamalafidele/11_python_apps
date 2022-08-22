import random

def bin_search(nums, target, low, high):
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return bin_search(nums, target, mid + 1, high)
        elif nums[mid] > target:
            return bin_search(nums, target, low, mid - 1)
    return -1 

sorted_list = list()
length = 1000
target = 345

while len(sorted_list) < length:
    sorted_list.append(random.randint( -3 * length, 3 * length))
sorted_list = sorted(sorted_list)

print(bin_search(sorted_list, target, 0, len(sorted_list)))






