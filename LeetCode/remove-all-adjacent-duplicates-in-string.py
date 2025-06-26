class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = [] # a list so that if our condition satisfy then we will append the chracter
        for i in s:
            if stack and stack[-1] == i:# stack --- checks if the stack is not empty , if its empty why to code !!
                                        # stack[-1] -- the chara which is at top in stack

                stack.pop()
            else:
                stack.append(i)

        return "".join(stack)   # # The join() function is used to combine elements of a list into a single string.
