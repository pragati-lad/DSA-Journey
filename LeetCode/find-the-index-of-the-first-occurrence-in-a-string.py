class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # two pointers i for neddle and j for haystack 
# strings : haystack and needle
# return the index of the first occurrence of needle in haystack. 
# or -1 if needle is not part of haystack

        for i in range(len(haystack)-len(needle)+1):
        # we want the range to be equal to the len of needle         
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
