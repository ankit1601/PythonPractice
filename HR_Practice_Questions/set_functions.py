# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    M = eval(input())
    m_set = set(input().split(' '))
    N = eval(input())
    n_set = set(input().split(' '))

    m_set_intersect = m_set.difference(n_set)
    n_set_intersect = n_set.difference(m_set)
    m_set_intersect.update(n_set_intersect)

    combind_list = list(map(int, list(m_set_intersect)))
    combind_list.sort()
    for i in combind_list:
        print(i)
