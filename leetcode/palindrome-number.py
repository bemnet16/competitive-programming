class Solution(object):
    def isPalindrome(self, x):
        if x<0:return False
        if x-int(str(x)[::-1])==0:return True
        return False