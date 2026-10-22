# Решение задачи со сложностью O(n), так как выполняется один проход по строке,
# а операции со стеком в среднем O(1)
# Необходимо использовать стек, так как сравниваем закрывающую скобку с последней открывающей (LIFO)

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in brackets:
                stack.append(c)
                continue

            if len(stack) == 0 or brackets[stack[-1]] != c:
                return False

            stack.pop()

        return len(stack) == 0