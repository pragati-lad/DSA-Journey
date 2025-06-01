class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j = m + n - 1 # think bitch!!!!!!!!!!!!!!!!!
        k = m-1 # point to last element 
        i = n-1 # point to last element

        while i >= 0 and k >= 0 :                         # i of nums2 because this will go on till all element of nums2 is  finished
            if  nums1[k] > nums2[i]:
                nums1[j] = nums1[k]
                k -= 1
            else:
                nums1[j] = nums2[i]
                i -= 1
            j -= 1
 

 # if there are still elements left in nums2 that need to be placed.
        

        while i >= 0:                      # nums1 = [7, 8, 9, 0, 0, 0]
                                           # nums2 = [1, 2, 3]
            nums1[j] = nums2[i]  
            i -= 1
            j -= 1

        return nums1 
