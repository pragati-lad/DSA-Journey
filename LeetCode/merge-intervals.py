class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # looking at test case 1 we get to know that we have to sort the intervals 
        # sort the intervals by their starting points
        intervals.sort(key = lambda intervals: intervals[0]) # [[1, 3], [2, 6], [8, 10], [9, 12]]


        # Initialize output list with the first interval for storing result
        output = [intervals[0]] #or  merged = [intervel[0]] to avoid egde cases 

        for interval in intervals[1:]: # 0th sublist[1,3] is already added to output list
            current_last_intervals_end_value = output[-1][1] # this will always give the end of current last interval of output list
            
            if interval[0] > current_last_intervals_end_value:

                output.append(interval)

            else: # to updated the current last interval stored in the output list.
                output[-1][1] =  max(output[-1][1],interval[1])

        return output        


"""

# or 

intervals.sort(key = lambda intervals: intervals[0])

output = [intervals[0]]

for i in intervals[1:]:
    current_last = output[-1][1]

    if  i[0] <= current_last :
        output[-1][1] = max(output[-1][1],i[1])

    else:
        output.append(i)     

return output



"""
