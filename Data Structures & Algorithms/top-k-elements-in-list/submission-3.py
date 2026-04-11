class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}
        for num in nums:
            countNums[num] = 1 + countNums.get(num, 0)

        frequencyList = []
        for num, count in countNums.items():
            frequencyList.append([count, num])
        frequencyList.sort()

        result = []
        while len(result) < k:
            result.append(frequencyList.pop()[1])
        
        return result


