#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.minstack = []
        self.minstack_min = []

    def push(self, val: int) -> None:
        self.minstack.append(val)
        lowest_value = min(val, self.minstack_min[-1] if self.minstack_min else val)
        self.minstack_min.append(lowest_value)

    def pop(self) -> None:
        self.minstack.pop()
        self.minstack_min.pop()

    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        return self.minstack_min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

