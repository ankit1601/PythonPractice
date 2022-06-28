"""
Input Format

The first line consists of an integer,

, the size of each group.
The second line contains the unordered elements of the room number list.

Constraints

Output Format

Output the Captain's room number.

Sample Input

5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

Sample Output

8

Explanation

The list of room numbers contains
elements. Since is , there must be groups of families. In the given list, all of the numbers repeat times except for room number .
Hence, is the Captain's room number.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
from operator import itemgetter
k = int(input())
c = Counter(input().split()).most_common()
c.sort(key=itemgetter(1))
print(c[0][0])