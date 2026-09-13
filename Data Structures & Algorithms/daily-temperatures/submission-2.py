class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)
        for i in range(len(temp)):
            for j in range(i+1, len(temp)):
                if temp[i] < temp[j]:
                    res[i] = j - i
                    break
        return res