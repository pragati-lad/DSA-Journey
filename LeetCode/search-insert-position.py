class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # of O(log n) algorithm ------------- Binary Search
        # mid ,high ,low

        
        l = 0 
        h = len(nums)-1
# exists in array
        while l <= h:
            mid = (h+l)//2 # / returns float 
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target: # right side 
                h = mid-1
            elif nums[mid] < target: # left side 
                l = mid+1
            
# does not exists in array 

        return l
