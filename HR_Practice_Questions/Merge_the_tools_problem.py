"""
Consider the following:

    A string,

, of length where
.
An integer,
, where is a factor of

    .

We can split
into substrings where each subtring, , consists of a contiguous block of characters in . Then, use each to create string

such that:

    The characters in

are a subsequence of the characters in
.
Any repeat occurrence of a character is removed from the string such that each character in
occurs exactly once. In other words, if the character at some index in occurs at a previous index in , then do not include the character in string

    .

Given
and , print lines where each line denotes string

.

Example

There are three substrings of length to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so . The second substring has all distinct characters, so . The third substring has different characters, so

. Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.

Function Description

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

    string s: the string to analyze
    int k: the size of substrings to analyze

Prints

Print each subsequence on a new line. There will be

of them. No return value is expected.

Input Format

The first line contains a single string,
.
The second line contains an integer,

, the length of each substring.

Constraints

, where is the length of It is guaranteed that is a multiple of

    .

Sample Input

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

Sample Output

AB
CA
AD

Explanation

Split
into equal parts of length . Convert each to by removing any subsequent occurrences of non-distinct characters in

:

Print each on a new line.
"""


def merge_the_tools(string, k):
    # print(string)
    count = 0
    sub_str = ""
    for index, char in enumerate(string):
        # print(index)
        if k == 1:
            print(char)
            continue
        count += 1
        if count == 1:
            sub_str = char
        elif char == string[index - 1] and count < k:
            continue
        elif char not in sub_str and count < k:
            sub_str += char
        elif char in sub_str and count == k:
            print(sub_str)
            count = 0
            sub_str = ''
        elif char not in sub_str and count == k:
            sub_str += char
            print(sub_str)
            count = 0
            sub_str = ''

    # your code goes here


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)