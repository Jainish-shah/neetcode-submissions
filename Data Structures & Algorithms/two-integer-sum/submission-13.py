class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, need in enumerate(nums):
            needed = target - need
            if needed in seen:
                return [seen[needed], i]
            seen[need] = i