"""
Sample Input

rabcdeefgyYhFjkIoomnpOeorteeeeet

Sample Output

ee
Ioo
Oeo
eeeee

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
str_ = input()
consonants = 'qwrtypsdfghjklzxcvbnm'
pattern = r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])'
res = re.findall(pattern, str_, re.IGNORECASE)
if res:
    print(*res, sep="\n")
else:
    print(-1)
