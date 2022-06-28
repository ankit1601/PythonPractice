"""
There is an array of integers. There are also disjoint sets, and , each containing integers. You like all the integers in set and dislike all the integers in set . Your initial happiness is . For each integer in the array, if , you add to your happiness. If , you add

to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since
and

are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints


Input Format

The first line contains integers
and separated by a space.
The second line contains integers, the elements of the array.
The third and fourth lines contain integers, and

, respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7

Sample Output

1

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n, m = list(map(int, input().split(' ')))
    integer_list = list(map(int, input().split(' ')))
    A = set(map(int, input().split(' ')))
    B = set(map(int, input().split(' ')))
    happiness_index = 0

    for i in integer_list:
        if i in A:
            happiness_index += 1
        if i in B:
            happiness_index -= 1

    print(happiness_index)