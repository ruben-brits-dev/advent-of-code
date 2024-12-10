# Day 2: Red-Nosed Reports- Star 2
Link to the problem: [Advent of Code 2024, Day 2](https://adventofcode.com/2024/day/2)

 ---
## Problem statement
Given input that represent a report per line:

|     |  | |  |  |
| -------- | ------- | -------- | ------- | ------- |
| 7  | 6 | 4 | 2  | 1 |
| 1  | 2 | 7 | 8  | 9 |
| 9  | 7 | 6 | 2  | 1 |
| 1  | 3 | 2 | 4  | 5 |
|8|  6|  4|  4|  1| 
| 1 | 3 | 6 | 7 | 9 |

thus above is 6 reports each with 5 levels.

A report is considered safe  if both are true:
 - levels are either all increasing or all decreasing
 - adjacent levels may only differ by at least one and at most three
  
Problem Dampener is introduced:
 - everything is the same, however if 1 unsafe level would result in a safe report, the report is considered safe

 ## My solution
Quite a nice challenge - First thought that came to mind is to implement some form of backtracking by using an error index and check around (ie: n-1, n, n+1) to see if removal will give a safe report.