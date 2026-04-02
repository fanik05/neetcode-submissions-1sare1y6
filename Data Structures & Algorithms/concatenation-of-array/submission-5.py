class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        result = [0] * (2 * numsLength)
        for i, num in enumerate(nums):
            result[i] = result[i + numsLength] = num
        return result




