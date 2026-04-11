class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}
        for n in nums:
            countNums[n] = 1 + countNums.get(n, 0)
       
        arr = []
        for n, count in countNums.items():
            arr.append([count, n])
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        return result
        