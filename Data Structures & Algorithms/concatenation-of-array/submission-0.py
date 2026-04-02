class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concatenatedArray = list(nums)
        for num in nums:
            concatenatedArray.append(num)
        return concatenatedArray
