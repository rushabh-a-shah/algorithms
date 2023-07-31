class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = collections.defaultdict(int)
        res = 0
        l = 0
        r = 0
        
        while r < len(s):
            charCount[s[r]] += 1

            while ((r - l + 1) - max(charCount.values())) > k:
                charCount[s[l]] -= 1
                l += 1
                
            res = max(res, (r - l + 1))
            r += 1
        
        return res
