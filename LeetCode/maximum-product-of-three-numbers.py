class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        

        n = len(nums)
        i = 0
        j = 1
        for i in range(n):             # sort the array 
            for j in range(i+1,n):
                if nums[i] > nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]

        producti = nums[-1]*nums[-2]*nums[-3]  # take 3 largest numbers  eg :[1,2,3,4 ] ,[1,2,3,-5] [-1,-2,-3,-4]

        productii = nums[0]*nums[1]*nums[-1]    # 1 largest and two -ve smallest eg:  [1,2,-3,-4]

        return max(producti,productii)          
