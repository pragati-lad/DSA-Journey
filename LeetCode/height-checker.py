
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = 1
        count = 0
        expected = heights.copy()    # made a copy as we can't modifiy heights inorder compare later
        for i in range(n):              # sorrted the array
            for j in range(i+1,n):
                if expected[i] > expected[j]:
                    expected[i],expected[j] = expected[j],expected[i]

        for i in range(n):    # compairing
            if heights[i] != expected[i]:
                count += 1
            
        return count    
      







"""

heights = [1,2,3,4,5]
n = len(heights)
i = 0
j = 1
count = 0
expected =heights.copy()
for i in range(n):
    for j in range(i+1,n):
        if expected[i] >expected[j]:
           expected[i],expected[j] =expected[j],expected[i]
            
print(expected)

for i in range(n):
    if heights[i] != expected[i]:
        count += 1

print(count)        

"""