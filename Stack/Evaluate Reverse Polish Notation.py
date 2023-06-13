class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for tok in tokens:
            if tok in operators:
                val1 = stack.pop()
                val2 = stack.pop()
                if tok == '+':
                    new = val1 + val2
                if tok == '-':
                    new = val2 - val1
                if tok == '*':
                    new = val1 * val2
                if tok == '/':
                    new = int(val2 / val1)
                stack.append(new)
            else:
                stack.append(int(tok))
        return stack[-1]
