"""
Input Format

The first line contains an integer,
, the number of students who have subscribed to the English newspaper.
The second line contains space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains

space separated roll numbers of those students.

Constraints

Output Format

Output the total number of students who have at least one subscription.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output

13

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
E = int(input())
e_set = set(input().split())

F = int(input())
f_set = set(input().split())

print(len(e_set.union(f_set)))
print(len(e_set.intersection(f_set)))
print(len(e_set.difference(f_set)))
print(len(e_set.symmetric_difference(f_set))) # give all apart from  common