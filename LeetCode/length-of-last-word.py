class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # string functions 
        # strip
        st = s.strip() # # removes leading (starting) and trailing (ending) whitespace characters from a string.
        # split 
        sp = st.split(" ") # by defsult so can use st.split(),will do the same 
        
        return len(sp[-1])
