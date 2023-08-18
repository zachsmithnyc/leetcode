def binary_search(sorted_elements, target):
    #base case 1 list is empty
    if sorted_elements == []:
        return "value not found"
    mid_idx = len(sorted_elements)//2
    mid_val = sorted_elements[mid_idx]
    #base case 2 vale is in the middle
    if target == mid_val:
        return mid_idx
    #target is greater than mid
    if target < mid_val:
        left_half = sorted_elements[:mid_idx]
        return binary_search(left_half, target)
    #target is less than mid
    if target > mid_val:
        right_half = sorted_elements[mid_idx + 1:]
        result = binary_search(right_half, target)
        if result == 'value not found':
            return result
        else:
            return result + mid_idx + 1

#pointers solution
def pointers(elements, left, right, target):
    if left >= right:
        return 'value not found'
    mid_idx = (left + right) // 2
    mid_val = elements[mid_idx]

    if mid_val == target:
        return mid_idx
    if mid_val > target:
        return pointers(elements, left, mid_idx, target)
    if mid_val < target:
        return pointers(elements, mid_idx + 1, right, target)

def whilePointers(elements, target):
    left_pointer = 0
    right_pointer = len(elements)

    while left_pointer < right_pointer:
        mid_idx = (left_pointer + right_pointer) // 2
        mid_val = elements[mid_idx]
        if mid_val == target:
            return mid_idx
        if mid_val > target:
            right_pointer = mid_idx
        if mid_val < target:
            left_pointer = mid_idx + 1
    
    return "Value not in list"



nums = [1, 2, 3, 4, 5, 6, 7]

print(binary_search(nums, 6))
start = 0
stop = len(nums)
print(pointers(nums, start, stop, 6))
print(whilePointers(nums, 6))