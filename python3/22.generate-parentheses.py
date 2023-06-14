#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        answer = []

        def recursion(open, closed):

            # If open brackets = closed brackets then finish this function call
            if open == closed == n:
                answer.append("".join(stack))
                return
            
            # If open brackets < n then we can always add more open brackets
            if open < n:
                # We append the stack and pop it but function call in between
                # Thus allowing it to be used in multiple function calls
                stack.append("(")
                recursion(open + 1, closed)
                stack.pop()
            
            # If open brackets > closed brackets then we can always add more closed brackets
            if open > closed:
                stack.append(")")
                recursion(open, closed + 1)
                stack.pop()

        # Call the function with 0,0 to begin recursion 
        recursion(0,0)
        return answer

# @lc code=end

