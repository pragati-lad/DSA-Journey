class Solution:
    def isPalindrome(self, s: str) -> bool:
        # converting all uppercase letters into lowercase letters and 
        # removing all non-alphanumeric characters, it reads the same forward and backward.
        # space are also removed 
        # empty string is panlindromic
        # for alphaanumreic we use variable.isalnum()
       
        left = 0
        right=len(s)- 1
# this is for only considering alphanumeric 
        while left <= right:
            if not s[right].isalnum():
                right-=1
                continue

            if not s[left].isalnum():
                left+=1
                continue
# this is for converting to all lower case
            if s[right].lower() != s[left].lower():
                return False
            
            right-= 1
            left +=1
                
        return True 
        
