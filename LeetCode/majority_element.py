class Solution:
    def majorityElement(self, nums: List[int]) -> int:

  # Boyer-Moore / moore vooting 
  # used to find the majority element in a list — the element that appears more than n / 2 times.
  # Time: O(n)
  
  # find the candidate
  # verify whether the candidate is majority
  
  # assume that 1st element is the majority
        n = len(nums)
        count = 0

        for i in nums:
            if count == 0:
                candidate = i

            if i == candidate:
                count += 1
            else:
                count -= 1

        return candidate                

# or 


"""
        for i in range(n):
            if count == 0:
                candidate = nums[i] 

            if nums[i] == candidate:
                count += 1
            else:
                count -= 1


        return candidate
        
        
   
    
    candidate = 2 , count = 1
    next 2 --- count = 2
    next 1 ---- count = 1 
    next 1 ---- count = 0
    next 1 ---- count = 1 ---- candidate = 1  
    next 2 ---- count = 0 
    next 2 --- count = 1 ---- candidate = 2
"""
