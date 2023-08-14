class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slist = [*s]
        tlist = [*t]

        if sorted(slist) == sorted(tlist):
            return True
        else:
            return False

            

print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram("rat", "car"))

