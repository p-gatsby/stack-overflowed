"""
80. Remove Duplicates from Sorted Array II
Medium - Arrays & Strings

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place 
such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it's not possible to change the length of the array in some languages, the result must be stored 
in the first part of nums. More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result.
It does not matter what values are left beyond index k.

Return k after placing the final result in the first k slots of nums.

Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: The function should return k = 5, with the first five elements being 1, 1, 2, 2, 3.
Underscores represent ignored values beyond index k.

Example 2:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: The function should return k = 7, with the first seven elements being 0, 0, 1, 1, 2, 3, 3.
Underscores represent ignored values beyond index k.

Constraints:
1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.
"""


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array in-place such that each unique element appears at most twice.
        Modifies the input list so the first k elements hold the valid result, and returns k — the new length.
        """

        k = 0
        count = 0

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                count = 1
            else:
                count += 1

            if count <= 2:
                nums[k] = nums[i]
                k += 1

        return k


# Testing
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(Solution().removeDuplicates(nums), nums)
