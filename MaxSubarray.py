'''We define subsequence as any subset of an array. We define a subarray as a contiguous subsequence in an array.

Given an array, find the maximum possible sum among:

1. all nonempty subarrays.
2. all nonempty subsequences.
Print the two values as space-separated integers on one line.

Note that empty subarrays/subsequences should not be considered.

Example
arr = [-1, 2, 3, -4, 5, 10]
The maximum subarray sum is comprised of elements at inidices [1 - 5]. Their sum is 2 + 3 + -4 + 5 + 10 =16 . 
The maximum subsequence sum is comprised of elements at indices [1, 2, 4, 5] and their sum is 2 + 3 + 5 + 10.

Function Description

Complete the maxSubarray function in the editor below.

maxSubarray has the following parameter(s):

int arr[n]: an array of integers
Returns

int[2]: the maximum subarray and subsequence sums

Input Format

The first line of input contains a single integer t the number of test cases.

The first line of each test case contains a single integer n.
The second line contains n space-separated integers arr[i] where 0 <= i <= n.

Constraints

1 <= t <= 10
1 <= n <= 10^5
-10^4 <= arr[i] <= 10^4
The subarray and subsequences you consider should have at least one element.

Sample Input 0

2
4
1 2 3 4
6
2 -1 2 3 4 -5
Sample Output 0

10 10
10 11

Explanation 0

In the first case: The maximum sum for both types of subsequences is just the sum of all the elements since they are all positive.

In the second case: The subarray  [2, -1, 2, 3, 4] is the subarray with the maximum sum, and [2, 2, 3, 4] is the subsequence 
with the maximum sum.

Sample Input 1

1
5
-2 -3 -1 -4 -6
Sample Output 1

-1 -1
Explanation 1

Since all of the numbers are negative, both the maximum subarray and maximum subsequence sums are made up of one element, -1.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    #1. max_subarray sum
    #2. max_subsequence sum
        #sum all of positives
        #if all negative return max value
    max_subarray_sum = arr[0]
    current_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(num, current_sum + num) 
        max_subarray_sum = max(max_subarray_sum, current_sum) 
        
        max_subsequence_sum = sum(num for num in arr if num > 0) or max(arr)
    return max_subarray_sum, max_subsequence_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    results = []
    
    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)
        results.append(result)
        
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
