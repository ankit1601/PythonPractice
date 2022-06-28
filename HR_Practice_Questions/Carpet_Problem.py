"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

    Mat size must be

X. ( is an odd natural number, and is times

    .)
    The design should have 'WELCOME' written in the center.
    The design pattern should only use |, . and - characters.

Sample Designs

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

Input Format

A single line containing the space separated values of
and

.

Constraints

Output Format

Output the design pattern.

Sample Input

9 27

Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    input_ = input()
    M = int(input_.split(" ")[0])
    N = int(input_.split(" ")[1])
    mid_row_index = M // 2
    mid_col_index = N // 2
    CENTER_STRING = 'WELCOME'
    center_string_length = len(CENTER_STRING)
    DESIGN_PATTERN = '.|.'
    mid_col_start_index = mid_col_index - center_string_length // 2
    mid_col_end_index = mid_col_index + center_string_length // 2

    for i in range(M):
        if i < mid_row_index:
            mid_design_start_index = mid_col_index - ((i * 2 + 1) * (len(DESIGN_PATTERN)) // 2)
            mid_design_end_index = mid_col_index + ((i * 2 + 1) * (len(DESIGN_PATTERN)) // 2)
        elif i > mid_row_index:
            mid_design_start_index = mid_col_index - (((M - i - 1) * 2 + 1) * (len(DESIGN_PATTERN)) // 2)
            mid_design_end_index = mid_col_index + (((M - i - 1) * 2 + 1) * (len(DESIGN_PATTERN)) // 2)
        for j in range(N):
            if i == mid_row_index:
                if mid_col_start_index <= j <= mid_col_end_index:
                    print(CENTER_STRING[j - mid_col_start_index], end='')
                else:
                    print('-', end='')
            else:
                if mid_design_start_index <= j <= mid_design_end_index:
                    NEW_DESIGN_PATTERN = (DESIGN_PATTERN * (i * 2 + 1))
                    print(NEW_DESIGN_PATTERN[j - mid_design_start_index], end='')
                else:
                    print('-', end='')
        print()
    print("###########################################################################")
    for i in range(M):
        if i < mid_row_index:
            DESIGN_PATTERN_ = DESIGN_PATTERN*(2*i+1)
            print(DESIGN_PATTERN_.center(N, '-'))
        elif i == mid_row_index:
            print('WELCOME'.center(N, '-'))
        else:
            DESIGN_PATTERN_ = DESIGN_PATTERN*((M-i-1)*2+1)
            print(DESIGN_PATTERN_.center(N, '-'))

