class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                idx = stack.pop()[1]
                out[idx] = i - idx
            stack.append((temp, i))
        
        for _, i in stack:
            out[i] = 0

        return out
