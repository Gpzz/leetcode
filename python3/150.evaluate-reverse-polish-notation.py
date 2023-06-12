#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:

            # if list entry is a number append it to numbers list and skip
            try:
                float(token)
                stack.append(int(token))
                continue
            except:
                pass

            # apply operation to previous value and top of stack
            if token == "+":
                stack[-2:] = [stack[-2] + stack[-1]]
            if token == "-":
                stack[-2:] = [stack[-2] - stack[-1]]
            if token == "*":
                stack[-2:] = [stack[-2] * stack[-1]]
            if token == "/":
                stack[-2:] = [int(stack[-2] / stack[-1])]

        return stack[0]
# @lc code=end

