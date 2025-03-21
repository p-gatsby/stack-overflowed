<a name="readme-top"></a>

# Explanation: Remove Duplicates from Sorted Array

## Problem Description

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place 
such that each unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in `nums`.

### Requirements
- Modify `nums` so that the first `k` elements contain only the unique elements in their original order.
- The remaining elements do not matter.
- Return `k` (the number of unique elements).

## Constraints
- <= nums.length <= 3 * 10^4
- 100 <= nums[i] <= 100
- `nums` is sorted in non-decreasing order.

## Example 1

**Input:**
```python
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
```

**Output:**
```python
5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
```

**Explanation:**
- The function should return `k = 5`, with the first five elements being `0, 1, 2, 3, 4`.
- The underscores represent values beyond the returned length.

## Solution Approach

To efficiently remove duplicates from `nums`, a **two-pointer approach** is used.

### Steps to Solve the Problem
1. Use two pointers:  
   - `j` → Tracks the index where the next unique element should be placed.
   - `i` → Iterates through `nums` to check for duplicates.

2. Iterate through `nums` starting from index `1`:
   - If `nums[j] != nums[i]`, it means `nums[i]` is a **new unique element**.
   - Move `j` forward and copy `nums[i]` to `nums[j]`.

3. Return `j + 1`, which represents the number of unique elements.

### Key Advantages of This Approach
- **In-Place Modification:** No extra space is used.
- **Efficient:** Runs in **O(n) time**, where `n` is the number of elements in `nums`.
- **Stable:** Keeps unique elements in their **original order**.

## Time Complexity
- **O(n):** The algorithm iterates through `nums` exactly once.

## Space Complexity
- **O(1):** Modifies `nums` in-place without using extra memory.

## Leetcode Feedback
<img width="700" alt="Leetcode Feedback" src="https://github.com/user-attachments/assets/c847cfd9-8ece-4041-be43-03ff6a9c0d80" />

<p align="right">(<a href="#readme-top">back to top</a>)</p>
