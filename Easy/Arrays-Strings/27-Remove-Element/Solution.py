"""
27. Remove Element
Easy - Arrays & Strings

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

To get accepted, the function must:
1. Modify nums so that the first k elements contain only elements not equal to val.
2. The remaining elements do not matter.
3. Return k (the number of elements not equal to val).

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: The function should return k = 2, with the first two elements being 2.
The underscores represent ignored elements.

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: The function should return k = 5, with the first five elements being 0, 0, 1, 3, and 4.
Order of elements may vary.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

"""


from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Modify nums so that the first k elements contain only elements not equal to val.
        Return k (the number of elements not equal to val) and Modifies nums in place
        """
        k = 0
        for index, value in enumerate(nums):
            if value != val:
                nums[k] = nums[index]
                k += 1

        return k


# Testing
nums = [3, 2, 2, 3]
print(Solution().removeElement(nums, 3), nums)
