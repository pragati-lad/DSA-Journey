class Solution(object):
    def maxDepth(self, s):
        """                  # vps -- "()", "()[]{}", "{[()]}"
        :type s: str         # nesting depth -- "(((())))()(())" → Nesting depth = 4
        :rtype: int          
        """
        if not s:  # to handle non-vps
            return 0

        
        current = 0 #for tracking current depth
        result = 0  #for the maximum nesting depth

        for char in s:
            if char == "(":
                current+=1
                if current > result :
                    result = current 
                
            elif char == ")":
                current-=1

        return result 
