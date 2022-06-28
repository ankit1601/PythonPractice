"""
The first line contains the number of elements in set .
The second line contains the space separated list of elements in set .
The third line contains integer , the number of other sets.
The next lines are divided into

parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.

len(set(A))
len(otherSets)

Output Format

Output the sum of elements in set

.

Sample Input

 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66

Sample Output

38

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
number_of_element_set_a = int(input())
set_a = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    operation, _ = input().split()
    set_b = set(map(int, input().split()))
    if operation == 'intersection_update':
        set_a.intersection_update(set_b)
    elif operation == 'update':
        set_a.update(set_b)
    elif operation == 'symmetric_difference_update':
        set_a.symmetric_difference_update(set_b)
    elif operation == 'difference_update':
        set_a.difference_update(set_b)
print(sum(set_a))