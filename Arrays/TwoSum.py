# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy

# Approach:
# - Use hashmap (dictionary)
# - Store number and its index
# - Check if (target - num) exists

# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i , num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i
