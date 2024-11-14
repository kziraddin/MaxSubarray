# Maximum Subarray and Subsequence Sum

## Problem Description

This program solves the problem of finding the maximum possible sum among:
1. All nonempty subarrays
2. All nonempty subsequences

of a given array of integers.

A subsequence is defined as any subset of an array, while a subarray is a contiguous subsequence in an array.

## Function: maxSubarray

The `maxSubarray` function takes an array of integers as input and returns two values:
1. The maximum sum of any nonempty subarray
2. The maximum sum of any nonempty subsequence

### Algorithm

- For the maximum subarray sum, we use Kadane's algorithm.
- For the maximum subsequence sum, we sum all positive numbers. If all numbers are negative, we return the maximum value in the array.

## Input Format

- The first line contains an integer `t`, the number of test cases.
- For each test case:
  - The first line contains an integer `n`, the size of the array.
  - The second line contains `n` space-separated integers representing the array elements.

## Output Format

For each test case, the program outputs two space-separated integers:
1. The maximum subarray sum
2. The maximum subsequence sum

## Constraints

- 1 ≤ t ≤ 10
- 1 ≤ n ≤ 10^5
- -10^4 ≤ arr[i] ≤ 10^4
