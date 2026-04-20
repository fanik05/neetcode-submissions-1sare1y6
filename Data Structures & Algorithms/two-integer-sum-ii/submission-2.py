class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0 , len(numbers) - 1
        sortedNumbers = sorted(numbers)
        while l < r:
            if sortedNumbers[l] + sortedNumbers[r] > target:
                r -= 1
            elif sortedNumbers[l] + sortedNumbers[r] < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []