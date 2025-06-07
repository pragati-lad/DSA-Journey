class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

# need to use bs twice for the 1st occurence and the last occurence
# to find 1st occ -- after finding target search left side 
# to find last occ -- after finding target search right side 
        start = 0
        end = len(nums) - 1
        res1 = -1

        #for 1st occurence
        while start <= end:
            mid = (start+end)//2

            if nums[mid] == target:
                res1 = mid
                end = mid - 1  # go left to find earlier occurrence

            elif nums[mid] > target:
                end = mid-1

            else:
                start = mid+1


        start = 0
        end = len(nums) - 1
        res2 = -1        

        #for last  occurence
        while start <= end:
            mid = (start+end)//2

            if nums[mid] == target:
                res2 = mid
                start = mid+1  # go right to find further occurrence

            elif nums[mid] > target:
                end = mid-1

            else:
                start = mid+1

        return [res1,res2]
