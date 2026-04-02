class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in indices and indices[diff] != i:
                return [indices[diff], i]
            indices[num] = i

        return []


