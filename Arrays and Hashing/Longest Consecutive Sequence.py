class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 0
        for num in nums:
            curLen = 0
            if num - 1 not in numSet:
                curLen = 1
                i = 1
                while num + i in numSet:
                    curLen += 1
                    i += 1
            length = max(length, curLen)
        return length
