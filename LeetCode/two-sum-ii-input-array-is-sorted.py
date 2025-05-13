class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p = 0                                                               # the space complexity is O(n) due to use of two pointer unlike brute force method with O(n^2)
        q = len(numbers) - 1

        while p < q : # as its an sorted array 

            if numbers[p] + numbers[q] == target:
                return [p+1,q+1]

            elif numbers[p] + numbers[q] > target:
                q -= 1

            else : # numbers[p] + numbers[q] < target:
                p += 1


        return[] # incase there is no match

            



"""

can also
        
if numbers[p] + numbers[q] > target:
    q -= 1
elif numbers[p] + numbers[q] < target: 
    p += 1
else: # numbers[p] + numbers[q] == target:
    return[p+1,q+1] 

"""
