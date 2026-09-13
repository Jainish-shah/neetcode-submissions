class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)
        stack = [] # [index, temp]
        for r, t in enumerate(temp):
            while stack and t > stack[-1][1]:
                stackI, stackT = stack.pop()
                res[stackI]=(r - stackI)
            stack.append((r, t))

        return res