"""
Print True if set is a strict superset of all other

sets. Otherwise, print False.

Sample Input 0

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output 0

False

Explanation 0

Set
is the strict superset of the set but not of the set because is not in set .
Hence, the output is False.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
set_a = set(input().split())
n = int(input())
is_strict_superset = True
for _ in range(n):
    set_ = set(input().split())
    if not set_a.issuperset(set_):
        is_strict_superset = False
        break

print(is_strict_superset)