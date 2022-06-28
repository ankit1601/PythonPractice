"""
Neo has a complex matrix script. The matrix script is a X

grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

[Capture.JPG]

To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input Format

The first line contains space-separated integers
(rows) and (columns) respectively.
The next

lines contain the row elements of the matrix script.

Constraints

Note: A

score will be awarded for using 'if' conditions in your code.

Output Format

Print the decoded matrix script.

Sample Input 0

7 3
Tsi
h%x
i #
sM
$a
#t%
ir!

Sample Output 0

This is Matrix#  %!

Explanation 0

The decoded script is:

This$#is% Matrix#  %!

Neo replaces the symbols or spaces between two alphanumeric characters with a single space   ' ' for better readability.

So, the final decoded script is:

This is Matrix#  %!

Language
Python 3
5
6
7
8
9
10
11
13
12
14
15
4
16
17
18
19
20
21
22
23
24
25
26
27
28
29
3
1
2

Line: 1 Col: 1
Test against custom input

Wrong Answer :(

1/1 test case failed
Compiler Message

Wrong Answer

Input (stdin)

    7 3

    Tsi

    h%x

    i #

    sM

    $a

    #t%

    ir!

Your Output (stdout)

    This is Matrix#  %!

Expected Output

    This is Matrix#  %!


"""
import re
from collections  import OrderedDict

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

transpose = OrderedDict()
for item in matrix:
    for index, char in enumerate(item):
        cur_str = transpose.get(index,'')
        transpose[index] = cur_str+char

final_str = ''
for key in transpose.keys():
    final_str+=transpose[key]

# print(final_str)

pattern = r'(?<=\w)[!@#$%&\s]+(?=\w)'
# print(re.findall(pattern, final_str))
res= re.sub(pattern,' ', final_str)
# res = final_str.replace(pattern, '\s')
print(res)