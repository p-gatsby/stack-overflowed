<a name="readme-top"></a>

# Explanation: Remove Element

## Problem Description

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The order of elements may change.

### Requirements
- Modify `nums` so that the first `k` elements contain only elements not equal to `val`.
- The remaining elements do not matter.
- Return `k` (the number of elements not equal to `val`).

### Constraints
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100

### Example 1
**Input:**
```python
nums = [3,2,2,3], val = 3
```

**Output:**
```python
2, nums = [2,2,_,_]
```

**Explanation:**
- The function should return k = 2, with the first two elements being 2.
- The underscores represent ignored elements.

## Solution Approach

To efficiently remove all occurrences of `val` from `nums`, a two-pointer approach is used.

### Steps to Solve the Problem
1. Use a pointer `k` to track the index where the next valid element should be placed.
2. Iterate through `nums` using an index `i`:
   - If `nums[i]` is not equal to `val`, place `nums[i]` at `nums[k]` and increment `k`.
   - Otherwise, skip `nums[i]`, effectively removing `val`.
3. Return `k`, which represents the number of elements not equal to `val`.

### Key Advantages of This Approach
- **In-Place Modification:** No extra space is used.
- **Efficient:** Runs in O(n) time, where n is the number of elements in `nums`.
- **Stable:** The first `k` elements in `nums` will contain only values not equal to `val`.

## Time Complexity
- O(n): The algorithm iterates through `nums` exactly once.

## Space Complexity
- O(1): Modifies `nums` in-place without using extra memory.

## Leetcode Feedback
<img width="689" alt="Leetcode Feedback" src="https://github.com/user-attachments/assets/d414055c-fbe5-475e-905e-7d5e237c48c8" />

<p align="right">(<a href="#readme-top">back to top</a>)</p>
