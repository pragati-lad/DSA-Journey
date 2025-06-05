class Solution:
    def isPerfectSquare(self, num: int) -> bool:
# sq root is always smaller than sq/2 for perfect sqs
# except   
# 0 and 1
# make a condition for these because they are perfect sqs
        if num < 2:
            return True

        start = 0
        end = num//2

        while start <= end:
            mid = (start+end)//2    
            sq = mid*mid

            if sq == num:
                return True
            elif sq < num:
                start = mid + 1
            else:
                end = mid - 1  

        return False      
