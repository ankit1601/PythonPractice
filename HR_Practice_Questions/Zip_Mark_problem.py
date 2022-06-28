"""
Input Format

The first line contains
and separated by a space.
The next

lines contains the space separated marks obtained by students in a particular subject.

Constraints


Output Format

Print the averages of all students on separate lines.

The averages must be correct up to

decimal place.

Sample Input

5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5

Sample Output

90.0
91.0
82.0
90.0
85.5

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split())
subject_list = []
for _ in range(X):
    num_perstd_sub = map(eval, input().split())
    subject_list.append(num_perstd_sub)

for marks_per_std in zip(*subject_list):
    print(sum(marks_per_std)/len(marks_per_std))