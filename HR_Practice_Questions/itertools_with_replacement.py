"""
Task

You are given a string
.
Your task is to print all possible size

replacement combinations of the string in lexicographic sorted order.

Input Format

A single line containing the string
and integer value

separated by a space.

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the combinations with their replacements of string

on separate lines.

Sample Input

HACK 2

Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

str_, N = input().split()
N = int(N)
str_ = "".join(sorted(str_))
comb_list = combinations_with_replacement(str_, N)
for comb in comb_list:
    print("".join(comb))
