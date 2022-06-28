regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

r"^M{0,3)(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

# Validate mobile number with 10 digits start with 789
import re
pattern = r'^[789]{1}[\d]{9}$'
N = int(input())

for _ in range(N):
    print('YES' if re.match(pattern, input()) else 'NO')


# Enter your code heremail match e. Read input from STDIN. Print output to STDOUT

"""
Sample Input

2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>

Sample Output

DEXTER <dexter@hotmail.com>

"""
import email.utils
import re
pattern = r'^<[a-zA-Z]{1}(\w|\.|-)+@[a-zA-Z]+\.[A-Za-z]{1,3}>$'
N =int(input())
for _ in range(N):
    name, email_ = input().split(' ')
    match = re.match(pattern, email_)
    if match:
        print(name, match.group())



"""
11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   

Sample Output

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = r':?.(#[a-fA-F0-9]{6}|#[a-fA-F0-9]{3})'
N = int(input())
for _ in range(N):
    res = re.findall(pattern,input())
    if res:
        print(*res, sep="\n")