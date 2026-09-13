class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 1, len(numbers)
        while l < r:
            sum = numbers[l-1] + numbers[r-1]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l, r]
        return []
        
 
 
 
 
 
 
 
 











 
 
        # mp = defaultdict(int)
        # for i in range(len(numbers)):
        #     temp = target - numbers[i]
        #     if temp in mp:
        #         return [i+1, mp[temp]]
        #     mp[numbers[i]] = i+1 
        # return []