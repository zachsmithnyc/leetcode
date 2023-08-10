class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for p in range(1, len(nums)):
                if i == p:
                    continue
                if nums[i] + nums[p] == target:
                    solution = [i, p]
                    break

        return solution
    
list = [2, 4, 11, 3]

print(Solution().twoSum(list, 6))

        
