"""
You are given a string .
contains alphanumeric characters only.
Your task is to sort the string
in the following manner:
    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.
Input Format
A single line of input contains the string
Constraints
Output Format
Output the sorted string
Sample Input
Sorting1234
Sample Output
ginortS1324

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    input_string = input()
    lower_string = []
    upper_string = []
    even_string = []
    odd_string = []

    for i in input_string:
        if i.isdigit():
            digit = int(i)
            if digit % 2 == 0:
                even_string.append(digit)
            else:
                odd_string.append(digit)
        elif i.islower():
            lower_string.append(i)
        else:
            upper_string.append(i)

    lower_string.sort()
    upper_string.sort()
    even_string.sort()
    odd_string.sort()
    even_string = list(map(str, even_string))
    odd_string = list(map(str, odd_string))

    all_combined = lower_string + upper_string + odd_string + even_string
    print("".join(all_combined))