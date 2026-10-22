class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in matching:
                if not stack or stack.pop() != matching[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack
