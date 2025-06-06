class Solution:
    def mySqrt(self, x: int) -> int:

        # so we hava eto find the sqroot of x and round it dowm to the nearest integer (don keep it float)
        # x should not be negative
        # the sqroot should also not be negative 
        # if x is 0 or 1 return it (√0 = 0, √1 = 1))
        # our search range would be from 1 to x//2 --- because a sqroot is smaller than x//2

        if x < 2:
            return x

        start = 0 
        end = x//2
        res = 0               # to store our mid becase it is going to be our sqroot
        while start <= end:
            mid = (start+end)//2
            sq = mid*mid
            
            if sq == x:
                return mid 
            
            elif sq < x:
                res = mid
                start = mid+1
            else:
                end = mid-1

        return res
