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



nums = [1, 2, 3, 4, 5, 6, 7]

print(binary_search(nums, 6))