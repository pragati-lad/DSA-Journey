class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        
        # sorted the array 
        
        nums.sort()

        # calculate
        max_pro = (nums[-1]*nums[-2])-(nums[0]*nums[1])
                   # substracting smallest product from the largest product
                      # smallest product will be the product of numbers on 0th and 1st index of sorted array
                          # largest will  be the product of numbers at -1th and -2th  index of sorredt array
        return max_pro

        
