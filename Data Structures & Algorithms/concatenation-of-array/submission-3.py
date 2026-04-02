class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        result = [0] * (2 * numsLength)
        for i in range(numsLength):
            result[i] = result[i + numsLength] = nums[i]
        return result




