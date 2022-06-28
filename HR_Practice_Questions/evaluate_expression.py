"""
Task

You are given a polynomial
of a single indeterminate (or variable), .
You are also given the values of and . Your task is to verify if

.

Constraints
All coefficients of polynomial
are integers.
and

are also integers.

Input Format

The first line contains the space separated values of
and .
The second line contains the polynomial

.

Output Format

Print True if

. Otherwise, print False.

Sample Input

1 4
x**3 + x**2 + x + 1

Sample Output

True

Explanation


Hence, the output is True.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = map(int, input().split())
value = eval(input())
if k == value:
    print(True)
else:
    print(False)