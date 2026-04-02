class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for _, num in enumerate(nums):
            if num in count:
                return True
            count[num] = 1
        return False
        