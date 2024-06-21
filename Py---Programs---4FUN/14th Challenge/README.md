# Happiness Score Calculator

## Objective

This project calculates the total happiness score based on an array of integers and two sets of integers. You gain happiness for elements in one set and lose happiness for elements in the other set.

## Task

Given an array of `n` integers and two disjoint sets, `A` and `B`, each containing `m` integers:
- You like all the integers in set `A` and dislike all the integers in set `B`.
- Your initial happiness is `0`.
- For each integer in the array, if it is in set `A`, you add `1` to your happiness. If it is in set `B`, you subtract `1` from your happiness. Otherwise, your happiness does not change.

### Input Format

1. The first line contains integers `n` and `m` separated by a space.
2. The second line contains `n` integers, the elements of the array.
3. The third line contains `m` integers, the elements of set `A`.
4. The fourth line contains `m` integers, the elements of set `B`.

### Constraints

- \(1 \leq n, m \leq 10^5\)
- \(1 \leq \text{Element in the array}, \text{Element in set } A, \text{Element in set } B \leq 10^9\)

### Output Format

Output a single integer, your total happiness.

### Example

#### Sample Input
3 2
1 5 3
3 1
5 7

#### Sample Output
1

#### Explanation

You gain `1` unit of happiness for elements `1` and `3` in set `A`. You lose `1` unit for `5` in set `B`. The element `7` in set `B` does not exist in the array so it is not included in the calculation.

Hence, the total happiness is `1`.
