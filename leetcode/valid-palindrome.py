import re
class Solution(object):
    def isPalindrome(self, s):
        s=re.sub(r'[\W_]', '',s).lower()
        if s == s[::-1]:
            return True
        return False
        