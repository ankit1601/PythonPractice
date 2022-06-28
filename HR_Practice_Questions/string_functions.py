"""
Task

You are given a string
.
Your task is to find out if the string

contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string

.

Constraints

Output Format

In the first line, print True if
has any alphanumeric characters. Otherwise, print False.
In the second line, print True if has any alphabetical characters. Otherwise, print False.
In the third line, print True if has any digits. Otherwise, print False.
In the fourth line, print True if has any lowercase characters. Otherwise, print False.
In the fifth line, print True if has any uppercase characters. Otherwise, print False.
"""

if __name__ == '__main__':
    s = input()
    is_aplhanum = False
    is_aphabet = False
    is_digit = False
    is_lower = False
    is_upper = False

    for i in s:

        if i.isalnum() and not is_aplhanum:
            is_aplhanum = True
        if i.isalpha() and not is_aphabet:
            is_aphabet = True
        if i.isdigit() and not is_digit:
            is_digit = True
        if i.islower() and not is_lower:
            is_lower = True
        if i.isupper() and not is_upper:
            is_upper = True
        if all((is_aplhanum, is_digit, is_aplhanum, is_upper, is_lower)):
            break

    print(is_aplhanum)
    print(is_aphabet)
    print(is_digit)
    print(is_lower)
    print(is_upper)
