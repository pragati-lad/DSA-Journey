class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotated array -- 
        # sorrted 
        # unique elements 

#start <= end---You need to check every index, especially mid == start == end. Used in binary search  #               for target value or math problems.

#start < end----You're narrowing down to a single answer, like min/max in rotated array. Once narrowed, #               that one value is the answer.

        start = 0 
        end = len(nums)-1

        while start < end:  # Continue until start meets end, which will be the min element's index 
            mid = (start+end)//2

            if nums[mid] > nums[end]:
                start = mid + 1

            else: #nums[mid] < nums[end]
                #end = mid-1   # what if mid is smallest so had to do... end = mid 
                end = mid  

        return nums[end]    # stops when start == end  therefore we can return any start or end 
                     
#We don’t need a third case (elif) or == check, because:

#In this problem’s logic, the else already handles nums[mid] < nums[end] and the edge case where mid == end.
