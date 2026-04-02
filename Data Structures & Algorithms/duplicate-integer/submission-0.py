class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            current = nums[i]
            count = 0
            for num in nums:
                if num == current:
                    count += 1
                if count > 1:
                    return True
        return False