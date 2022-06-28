# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = r'^[\+\-\d]{1}\d*\.{1}\d+$'
N = int(input())

for _ in range(N):
    str_ = input()
    print(bool(re.match(pattern, str_)))
