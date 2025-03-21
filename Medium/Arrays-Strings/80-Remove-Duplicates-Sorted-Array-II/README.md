<a name="readme-top"></a>

# Explanation: Remove Duplicates from Sorted Array II

## Problem Description

Given an integer array `nums` sorted in non-decreasing order, remove some duplicates in-place 
such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it's not possible to change the length of the array in some languages, the result must be stored 
in the first part of `nums`. More formally, if there are `k` elements after removing the duplicates, 
then the first `k` elements of `nums` should hold the final result.
It does not matter what values are left beyond index `k`.

The function should return `k` after modifying `nums` in place.

## Constraints

- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- `nums` is sorted in non-decreasing order.

## Example 1

**Input:**  
```python
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
```

**Output:**
```python
7, nums = [0, 0, 1, 1, 2, 3, 3, _, _]
```

**Explanation:**  
- The function should return `k = 7`, with the first seven elements being `0, 0, 1, 1, 2, 3, 3`.  
- The underscores represent values beyond the returned length.

## Solution Approach

To efficiently remove duplicates while ensuring each unique element appears at most twice, a **two-pointer approach** is used.

### Steps to Solve the Problem
1. Use two variables:  
   - `k` → Tracks the index where the next valid element should be placed.  
   - `count` → Counts occurrences of the current element.  

2. Iterate through `nums`:  
   - If `nums[i]` is different from `nums[i - 1]`, reset `count = 1`.  
   - Otherwise, increment `count`.  
   - If `count <= 2`, copy `nums[i]` to `nums[k]` and increment `k`.  

3. Return `k`, which represents the number of elements in `nums` after removing extra duplicates.

## Key Advantages of This Approach

- **In-Place Modification:** No extra space is used.  
- **Efficient:** Runs in **O(n) time**, where `n` is the number of elements in `nums`.  
- **Stable:** Keeps elements **in their original order**, while ensuring no more than two duplicates remain.  

## Time Complexity

- **O(n):** The algorithm iterates through `nums` exactly once.

## Space Complexity

- **O(1):** Modifies `nums` in-place without using extra memory.

## Leetcode Feedback

<img width="618" alt="Leetcode Feedback" src="https://github.com/user-attachments/assets/4b6c1d57-d057-4ba2-8fb9-e3fd86dbef9c" />

<p align="right">(<a href="#readme-top">back to top</a>)</p>
