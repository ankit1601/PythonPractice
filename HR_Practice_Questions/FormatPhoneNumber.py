"""

The given mobile numbers may have , or written before the actual

digit number. Alternatively, there may not be any prefix at all.

Input Format

The first line of input contains an integer
, the number of mobile phone numbers.

lines follow each containing a mobile number.

Output Format

Print

mobile numbers on separate lines in the required format.

Sample Input

3
07895462130
919875641230
9195969878

Sample Output

+91 78954 62130
+91 91959 69878
+91 98756 41230

"""
def wrapper(f):
    def fun(l):
        for i,v in enumerate(l):
            if len(v) == 10:
                l[i] = f'+91 {v[0:5]} {v[5:]}'
            elif len(v) == 11:
                l[i] = f'+91 {v[1:6]} {v[6:]}'
            elif len(v) == 12:
                l[i] = f'+91 {v[2:7]} {v[7:]}'
            else:
                l[i] = f'+91 {v[3:8]} {v[8:]}'
        # print(l)
        return f(l)
        # complete the function
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

