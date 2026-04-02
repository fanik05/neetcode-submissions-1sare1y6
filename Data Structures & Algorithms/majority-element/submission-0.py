class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countNums = {}

        for n in nums:
            if n in countNums:
                countNums[n] += 1
            else:
                countNums[n] = 1
        max = -math.inf
        maxKey = 0
        for n in countNums:
            if countNums[n] > max:
                max = countNums[n]
                maxKey = n

        return maxKey


            
        