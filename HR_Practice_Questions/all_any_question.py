""" if all integers are positive and any integer is palindrome"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
in_list = list(map(int, input().split()))
# print(in_list)
# print([str(x)==str(x)[::-1] for x in in_list])
# print([x>0 for x in in_list])
print(all([x>0 for x in in_list]) and any([str(x)==str(x)[::-1] for x in in_list]))