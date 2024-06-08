# Leap Year Checker

This repository contains a solution for determining whether a given year is a leap year in the Gregorian calendar. 

## Problem Explanation

An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

### Leap Year Rules

In the Gregorian calendar, three conditions are used to identify leap years:
1. The year can be evenly divided by 4, is a leap year, unless:
2. The year can be evenly divided by 100, it is NOT a leap year, unless:
3. The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300, and 2500 are NOT leap years.

## Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean `True`, otherwise return `False`.

### Input Format

- An integer `year` representing the year to test.

### Constraints

- `1900 <= year <= 10^5`

### Output Format

- The function must return a Boolean value (`True`/`False`). Output is handled by the provided code stub.

## Example

### Sample Input 0
1990

### Sample Output 0

### Explanation 0

1990 is not a multiple of 4, hence it's not a leap year.

## Steps to Solve the Problem

1. **Read Input Value:**
   - Read the integer `year`.

2. **Check Leap Year Conditions:**
   - If the year is divisible by 4, proceed to the next check.
   - If the year is divisible by 100, proceed to the next check.
   - If the year is divisible by 400, return `True`.
   - Otherwise, return `False`.

In the code section (/folder): The implementation ensures that the function correctly determines whether a given year is a leap year based on the rules of the Gregorian calendar.
