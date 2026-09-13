class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = set()
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if ((i!=j) and (nums[i] + nums[j] == target)):
                    arr.add(i)
                    arr.add(j)
        return list(arr)