class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1
            
            while l < r:
                summed = a + nums[l] + nums[r]
                if summed < 0:
                    l += 1
                elif summed > 0:
                    r -= 1
                else:
                    triplets.append([a, nums[l], nums[r]])

                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return triplets
