class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}
        for num in nums:
            countNums[num] = 1 + countNums.get(num, 0)

        heap = []
        for num in countNums.keys():
            heapq.heappush(heap, (countNums[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
