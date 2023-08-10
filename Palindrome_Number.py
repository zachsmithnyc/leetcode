class Solution(object):
    def isPalindrome(self, x):
        """
        :type x:int
        :rtype: bool
        """
        palindrome = False
        string = str(x)
        if string == string[::-1]:
            palindrome = True
            return palindrome
        else:
            return palindrome
        
print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))
