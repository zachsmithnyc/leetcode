class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #create a hashset
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

        

nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
nums4 = [2, 14, 22, 22]

solution = Solution()

print(solution.containsDuplicate(nums1))
print(solution.containsDuplicate(nums2))
print(solution.containsDuplicate(nums3))
print(solution.containsDuplicate(nums4))