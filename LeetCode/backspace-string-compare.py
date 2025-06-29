class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stack1 = []
        stack2 = []
        for i in s :
            if i != "#":
                stack1.append(i)
            elif stack1:
                stack1.pop()    
# if i != "#":
#        stack1.append(i)
#    else:
#        stack1.pop()    # this will cause problem if string is "#ab"


        for j in t:
            if j != "#":
                stack2.append(j)
            elif stack2:
                stack2.pop()
                    
        return stack1 == stack2
        
        # time com : O(n+m)
