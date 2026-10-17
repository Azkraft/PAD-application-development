class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        occurrences: dict[int, list[int]] = {}
        for i in range(len(nums)):
            if nums[i] in occurrences:
                occurrences[nums[i]].append(i)
            else:
                occurrences[nums[i]] = [i]

        for i in range(len(nums)):
            current = nums[i]
            complement = target - current
            if current * 2 != target and complement in occurrences or complement in occurrences and len(occurrences[complement]) >= 2:
                return [occurrences[current][0], occurrences[complement][-1]]


# Часть 1
#     a. Решение в лоб two_sum_dummy.py
#     b. Решение с HashMap two_sum_smart.py

#     Решение с HashMap выигрывает у решения в лоб, так как в решении в лоб сложность O(n^2),
#     потому что для каждого элемента из списка происходит итерация по всему списку.
#     В решении с HashMap используется предобработка для каждого элемента и итерация по списку.
#     С учётом того, что добавление и поиск в HashMap в среднем O(1), то сложность выходит O(n + n) = O(2n) = O(n).
#     На LeetCode время работы решений 4164 ms у решения в лоб и 3 ms у решения с HashMap.

# Часть 2
#     Агент отлично справился с задачей и написал решения (two_sum_dummy_ai.py и two_sum_smart_ai.py),
#     а также верно определил их сложность. Время работы 1716 ms и 1 ms соответственно.
    