"""
Input Format

The first line contains the string
.
The second line contains the string

.

Constraints


Output Format

Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

Sample Input

aaadaa
aa

Sample Output

(0, 1)
(1, 2)
(4, 5)

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
str_ = input()
k = input()
pattern = re.compile(r'('+k+')')
match = pattern.search(str_)
if not match:
    print('(-1, -1)')
else:
    while match:
        print('({0}, {1})'.format(match.start(), match.end()-1))
        match = pattern.search(str_, match.start()+1)