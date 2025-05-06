class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        s = set(nums)
        return n != len(s) #(false)
        
        
        
        
        
        
        
        
        
        
        
        
        
"""       
# tried         
        n = len(nums)
        s = set(nums)  # SET re............ unique elements OnLy*.*
        if n== len(s):
            print("t")
        else:
            print("f")    

        # so eassy........
"""
