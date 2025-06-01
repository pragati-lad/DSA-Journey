class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # so keep in mind 
        
        # nums2 len is n 
        # nums1 len is m
        # we have to store in nums1 
        # and nums1 has space for both the arrays (m+n)
        # not to return anything 

        # so lets make 3 pointers 

        # a and c for num1 
        a = m-1 #(this will be at the last offical element of num1)
        c = m+n-1 #(so this will be at last in num1 where there are all zero)
        # b for nums2 
        b = n-1

        while a >= 0 and b >= 0:
            if nums1[a] > nums2[b]: # if a is bigger than b , put it in place of c 
                nums1[c] = nums1[a]
                a -= 1
            else:
                nums1[c] = nums2[b]
                b -= 1
            c -= 1  

        # If any elements left in nums2, copy them
        while b >= 0:
            nums1[c] = nums2[b]
            b -= 1
            c -= 1    
                 
