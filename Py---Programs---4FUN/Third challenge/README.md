# Day 3 Challenge: Integer and Float Division

## Problem Name
Integer and Float Division

## Problem Explanation

Given two integers, `a` and `b`, you need to:
1. Perform integer division of `a` by `b` and print the result.
2. Perform float division of `a` by `b` and print the result.

### Integer Division
In integer division, the result is the quotient in which the digits after the decimal point are removed. This can be done using the `//` operator in Python.

### Float Division
In float division, the result is the exact quotient including the digits after the decimal point. This can be done using the `/` operator in Python.

## Steps to Solve the Problem

### 1. Read Input Values:
- Read the first integer `a`.
- Read the second integer `b`.

### 2. Perform Divisions:
- Compute the result of integer division `a // b`.
- Compute the result of float division `a / b`.

### 3. Print the Results:
- Print the result of integer division.
- Print the result of float division.

## Example

Let's consider the sample input provided:
- `a = 4`
- `b = 3`

**Calculations**:
- Integer Division: \( 4 // 3 = 1 \)
- Float Division: \( 4 / 3 = 1.33333333333 \)

Thus, the output should be:
1
1.3333333333333333

## Explanation of the Solution

### Input Reading:
- The `input()` function reads a line of input from standard input (STDIN).
- `int(input())` converts the input to an integer.

### Perform Divisions:
- `a // b` performs integer division.
- `a / b` performs float division.

### Print Results:
- The `print()` function outputs the results of the integer and float divisions.

This approach ensures that both types of divisions are correctly calculated and printed as required by the problem statement.

---
