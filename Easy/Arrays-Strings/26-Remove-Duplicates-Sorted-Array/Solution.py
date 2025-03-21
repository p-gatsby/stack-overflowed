"""
26. Remove Duplicates from Sorted Array
Easy - Arrays & Strings

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
such that each unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

To get accepted, the function must:
1. Modify nums so that the first k elements contain the unique elements in the original order.
2. The remaining elements do not matter.
3. Return k (the number of unique elements).

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: The function should return k = 2, with the first two elements being 1 and 2.
Underscores represent ignored values beyond index k.

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: The function should return k = 5, with the first five elements being 0, 1, 2, 3, and 4.
Underscores represent values beyond the returned length.

Constraints:
1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array in-place so that each unique element appears only once.
        Modifies the input list so the first k elements are the unique values in original order,
        and returns k — the number of unique elements.
        """

        j = 0

        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j + 1


# Testing
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(Solution().removeDuplicates(nums), nums)
