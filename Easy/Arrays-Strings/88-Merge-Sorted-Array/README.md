<a name="readme-top"></a>

# Explanation: Merge Sorted Array

## Problem Description

Given two integer arrays, `nums1` and `nums2`, both sorted in **non-decreasing order**, the task is to merge `nums2` into `nums1` in-place such that `nums1` remains sorted.

### Requirements
- The final sorted array **should not** be returned by the function; instead, it must be **stored inside** `nums1`.
- `nums1` has a length of `m + n`, where:
  - The **first `m` elements** contain the actual values to be merged.
  - The **last `n` elements** are set to `0` and should be ignored.
- `nums2` has a length of `n` and contains `n` elements that need to be merged into `nums1`.

### Constraints
- `1 <= m, n <= 200`
- `nums1.length == m + n`
- `nums2.length == n`
- `-10^9 <= nums1[i], nums2[i] <= 10^9`


### Example 1
**Input:**
```python
nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6], n = 3
```
**Output:**
```python
[1, 2, 2, 3, 5, 6]
```

## Solution Approach

To merge `nums2` into `nums1` efficiently in **O(m + n) time**, we use a **three-pointer approach**:

1. Initialize Three Pointers:
   - `p1` → Points to the last valid element in `nums1` (`m - 1`).
   - `p2` → Points to the last element in `nums2` (`n - 1`).
   - `p` → Points to the last position in `nums1` (`m + n - 1`), where the largest element should be placed.

2. Compare Elements from the End:
   - Iterate while `p1 >= 0` and `p2 >= 0`.
   - If `nums1[p1] > nums2[p2]`, place `nums1[p1]` at `nums1[p]` and decrement `p1`.
   - Otherwise, place `nums2[p2]` at `nums1[p]` and decrement `p2`.
   - Decrement `p` after each placement.

3. Handle Remaining Elements in `nums2`:
   - If any elements remain in `nums2`, copy them into `nums1`.
   - This step is necessary if `nums1` initially had smaller elements and `p1` reached `-1`.

### Key Advantages of This Approach
- In-Place Merge: Modifies `nums1` without using extra space.
- Backward Traversal: Avoids overwriting elements in `nums1` that haven't been processed yet.
- Efficient: Runs in **O(m + n)** time.

By following this method, `nums1` is modified in-place to contain the merged sorted array.

## Time Complexity

O(m + n): We process each element from `nums1` and `nums2` exactly once.

## Space Complexity

O(1): We modify `nums1` in place without using extra space.

## Leetcode Feedback
<img width="714" alt="Leetcode Feedback" src="https://github.com/user-attachments/assets/4e71c8ce-67ca-4c64-8f0e-4c4d58868b22" />

<p align="right">(<a href="#readme-top">back to top</a>)</p>
