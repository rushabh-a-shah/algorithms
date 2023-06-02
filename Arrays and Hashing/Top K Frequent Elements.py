class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        return [i[0] for i in (sorted(d.items(), key=lambda x:x[1]))[-k:]]
