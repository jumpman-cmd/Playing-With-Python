# 3D Coordinates List Comprehension

## Objective
The goal of this project is to learn and practice list comprehensions in Python by generating a list of all possible coordinates on a 3D grid that do not sum to a specified integer `n`.

## Task Description
You are given three integers `x`, `y`, and `z` representing the dimensions of a cuboid along with an integer `n`. You need to print a list of all possible coordinates `(i, j, k)` on a 3D grid where the sum of `i + j + k` is not equal to `n`. The values of `i`, `j`, and `k` range from `0` to `x`, `0` to `y`, and `0` to `z` respectively.

### Input Format
- Four integers `x`, `y`, `z`, and `n`, each on a separate line.

### Constraints
- The values of `x`, `y`, `z` will be in the range `[0, 100]`.
- The value of `n` will be in the range `[0, 300]`.

### Output Format
- Print the list of coordinates in lexicographic increasing order.

## Examples

### Example 1
**Input:**
1
1
1
2

**Output:**
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

**Explanation:**
Each variable `i`, `j`, `k` will have values of `0` or `1`. All permutations of lists in the form `[i, j, k]` are:
[0, 0, 0]
[0, 0, 1]
[0, 1, 0]
[0, 1, 1]
[1, 0, 0]
[1, 0, 1]
[1, 1, 0]
[1, 1, 1]

We remove all arrays that sum to `2` to leave only the valid permutations.

### Example 2
**Input:**
2
2
2
2

**Output:**
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
