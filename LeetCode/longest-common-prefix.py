class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # edge cases 
        # out of bounds    eg : flow ,flower
        # no match  eg :
        res = ""

        for i in range(len(strs[0])):
            for s in strs:

                # this to avoid index out of range (eg : strs = ["flow", "flower"]
                if i == len(s)                                                               or s[i] != strs[0][i]:
                    return res # Exit early if mismatch or short word

            res += strs[0][i]
            # If all words had the same character at position `i`, add it to result

        return res # in case like this -- strs = ["car", "car", "car"]   
