"""
You are given a string .
Your task is to find out whether
is a valid regex or not.
Input Format
The first line contains integer
, the number of test cases.
The next lines contains the string
Constraints
Output Format
Print "True" or "False" for each test case without quotes.
Sample Input
2
.*\+
.*+
Sample Output
True
False
Explanation
.*\+ : Valid regex.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
from re import error
if __name__ == '__main__':
    n = eval(input())
    for i in range(n):
        try:
            reg = input()
            text = "hkjaha"
            res = re.findall(reg, text)
            print(True)
        except error as err:
            print(False)