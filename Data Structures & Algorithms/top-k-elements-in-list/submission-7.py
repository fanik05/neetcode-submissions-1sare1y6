class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}
        for num in nums:
            countNums[num] = 1 + countNums.get(num, 0)

        arr = []
        for num, count in countNums.items():
            arr.append([count, num])
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        return result
