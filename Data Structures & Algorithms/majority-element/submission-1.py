class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countNums = {}
        ans, maxCount = 0, 0

        for n in nums:
            countNums[n] = 1 + countNums.get(n, 0)
            ans = n if countNums[n] > maxCount else ans
            maxCount = max(countNums[n], maxCount)

        return ans


            
        