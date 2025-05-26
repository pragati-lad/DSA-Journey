class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # nums -- acending 
        # find the squares
        n = len(nums)
        for i in range(n):
           nums[i] = nums[i] * nums[i]
        
        # sort the squares in non - decreasing order
        nums.sort()
        return nums    
        
