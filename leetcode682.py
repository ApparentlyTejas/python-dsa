class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stk = []
        for op in operations:
            if op == '+':
                stk.append(stk[-1]+ stk[-2])
            elif op == 'D':
                stk.append(stk[-1] * 2)
            elif op == 'C':
                stk.pop()
            else:
                stk.append(int(op))
        return sum(stk)
# Time: O(n) Space: O(n)