from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):  # 1
            remaining = target - value  # 2

            if remaining in seen:  # 3
                return [i, seen[remaining]]  # 4
            else:
                seen[value] = i  # 5


if __name__ == '__main__':
    solution = Solution()

    tests = [
        {'nums': [2, 7, 11, 15], 'target': 9},
        {'nums': [3, 2, 4], 'target': 6},
        {'nums': [2, 3], 'target': 6},
        {'nums': [3, 3], 'target': 6}
    ]

    for test in tests:
        result = solution.two_sum(test['nums'], test['target'])
        print(result)
