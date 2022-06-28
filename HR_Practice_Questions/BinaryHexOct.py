"""
Given an integer, , print the following values for each integer from to

:

    Decimal
    Octal
    Hexadecimal (capitalized)
    Binary

Function Description

Complete the print_formatted function in the editor below.

print_formatted has the following parameters:

    int number: the maximum value to print

Prints

The four values must be printed on a single line in the order specified above for each
from to . Each value should be space-padded to match the width of the binary value of

and the values should be separated by a single space.

Input Format

A single integer denoting

.

Constraints

Sample Input

17

Sample Output

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001

Language
Python 3
1
4
17
18
19
20
21
5
16
2
7
8
3
15
9
10
11
12
13
14
6
22

Line: 14 Col: 46
Test against custom input
17

Compilation Successful :)

Click the Submit Code button to run your code against all the test cases.
Input (stdin)

    17

Your Output (stdout)

        1     1     1     1

        2     2     2    10

        3     3     3    11

        4     4     4   100

        5     5     5   101

        6     6     6   110

        7     7     7   111

        8    10     8  1000

        9    11     9  1001

       10    12     A  1010

       11    13     B  1011

       12    14     C  1100

       13    15     D  1101

       14    16     E  1110

       15    17     F  1111

       16    20    10 10000

       17    21    11 10001


"""


def print_formatted(number):
    max_length = len(bin(number).split('b')[1])
    max_space = max_length + 1
    for i in range(1, number + 1):
        dec = str(i)
        dec_length = len(dec)
        oct_ = oct(i).split('o')[1]
        oct_length = len(oct_)
        hex_ = hex(i).split('x')[1]
        hex_length = len(hex_)
        bin_ = bin(i).split('b')[1]
        bin_length = len(bin_)

        print(end=' ' * (max_space - dec_length - 1))
        print(i, end=' ' * (max_space - oct_length))
        print(oct_, end=' ' * (max_space - hex_length))
        print(hex_.upper(), end=' ' * (max_space - bin_length))
        print(bin_, end='\n')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)