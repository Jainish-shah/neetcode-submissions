class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newset = set()
        for num in nums:
            if num in newset:
                return True
            newset.add(num)
        return False