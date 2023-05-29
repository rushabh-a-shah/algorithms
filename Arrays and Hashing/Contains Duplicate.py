class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {i for i in nums}
        return not (len(d) == len(nums))
